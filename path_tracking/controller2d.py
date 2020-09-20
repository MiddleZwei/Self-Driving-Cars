#!/usr/bin/env python3

"""
2D Controller Class to be used for the CARLA waypoint follower.
"""

import cutils
from scipy import spatial
import numpy as np
from angles import normalize, r2d, d2r

k = 0.5  # control gain
Kp = 1.0  # speed proportional gain
Ki = 1.0  # speed integral gain
Kd = 1.0  # speed derivative gain
Ks = 20  # softening constant
dt = 0.03300000000000036  # [s] time difference
L = 2.9  # [m] Wheel base of vehicle


class Controller2D(object):
    def __init__(self, waypoints):
        self.vars = cutils.CUtils()
        self._current_x = 0
        self._current_y = 0
        self._current_yaw = 0
        self._current_speed = 0
        self._desired_speed = 0
        self._current_frame = 0
        self._current_timestamp = 0
        self._start_control_loop = False
        self._set_throttle = 0
        self._set_brake = 0
        self._set_steer = 0
        self._waypoints = waypoints
        self._conv_rad_to_steer = 180.0 / 70.0 / np.pi
        self._pi = np.pi
        self._2pi = 2.0 * np.pi
        self._integral = 0
        self.counter = 0

        # print(waypoints[0])

    def update_values(self, x, y, yaw, speed, timestamp, frame):
        self._current_x = x
        self._current_y = y
        self._current_yaw = yaw
        self._current_speed = speed
        self._current_timestamp = timestamp
        self._current_frame = frame
        if self._current_frame:
            self._start_control_loop = True

    def update_desired_speed(self):
        min_idx = 0
        min_dist = float("inf")
        desired_speed = 0
        for i in range(len(self._waypoints)):
            dist = np.linalg.norm(np.array([
                self._waypoints[i][0] - self._current_x,
                self._waypoints[i][1] - self._current_y]))
            if dist < min_dist:
                min_dist = dist
                min_idx = i
        if min_idx < len(self._waypoints) - 1:
            desired_speed = self._waypoints[min_idx][2]
        else:
            desired_speed = self._waypoints[-1][2]
        self._desired_speed = desired_speed

    def update_waypoints(self, new_waypoints):
        self._waypoints = new_waypoints

    def get_commands(self):
        return self._set_throttle, self._set_steer, self._set_brake

    def set_throttle(self, input_throttle):
        # Clamp the throttle command to valid bounds
        throttle = np.fmax(np.fmin(input_throttle, 1.0), 0.0)
        self._set_throttle = throttle

    def set_steer(self, input_steer_in_rad):
        # Convert radians to [-1, 1]
        input_steer = self._conv_rad_to_steer * input_steer_in_rad

        # Clamp the steering command to valid bounds
        steer = np.fmax(np.fmin(input_steer, 1.0), -1.0)
        self._set_steer = steer

    def set_brake(self, input_brake):
        # Clamp the steering command to valid bounds
        brake = np.fmax(np.fmin(input_brake, 1.0), 0.0)
        self._set_brake = brake

    def update_controls(self):
        ######################################################
        # RETRIEVE SIMULATOR FEEDBACK
        ######################################################
        x = self._current_x
        y = self._current_y
        yaw = self._current_yaw
        v = self._current_speed
        integral = self._integral
        self.update_desired_speed()
        v_desired = self._desired_speed
        t = self._current_timestamp
        waypoints = self._waypoints
        throttle_output = 0
        steer_output = 0
        brake_output = 0
        counter = self.counter

        """
            Use 'self.vars.create_var(<variable name>, <default value>)'
            to create a persistent variable (not destroyed at each iteration).
            This means that the value can be stored for use in the next
            iteration of the control loop.

            Example: Creation of 'v_previous', default value to be 0
            self.vars.create_var('v_previous', 0.0)

            Example: Setting 'v_previous' to be 1.0
            self.vars.v_previous = 1.0

            Example: Accessing the value from 'v_previous' to be used
            throttle_output = 0.5 * self.vars.v_previous 
        """

        # Skip the first frame to store previous values properly
        if self._start_control_loop:
            """
                Controller iteration code block.

                Controller Feedback Variables:
                    x               : Current X position (meters)
                    y               : Current Y position (meters)
                    yaw             : Current yaw pose (radians)
                    v               : Current forward speed (meters per second)
                    t               : Current time (seconds)
                    v_desired       : Current desired speed (meters per second)
                                      (Computed as the speed to track at the
                                      closest waypoint to the vehicle.)
                    waypoints       : Current waypoints to track
                                      (Includes speed to track at each x,y
                                      location.)
                                      Format: [[x0, y0, v0],
                                               [x1, y1, v1],
                                               ...
                                               [xn, yn, vn]]
                                      Example:
                                          waypoints[2][1]: 
                                          Returns the 3rd waypoint's y position

                                          waypoints[5]:
                                          Returns [x5, y5, v5] (6th waypoint)
                Controller Output Variables:
                    throttle_output : Throttle output (0 to 1)
                    steer_output    : Steer output (-1.22 rad to 1.22 rad)
                    brake_output    : Brake output (0 to 1)
            """

            throttle_output = self.pi_control(v_desired, v)

            # current x, current y, current yaw
            cx = self._current_x
            cy = self._current_y
            cyaw = self._current_yaw

            steer_output = self.stanley_control(cx, cy, cyaw)

            self.set_throttle(throttle_output)  # in percent (0 to 1)
            self.set_steer(steer_output)  # in rad (-1.22 to 1.22)
            self.set_brake(brake_output)  # in percent (0 to 1)

            # self.log_x_y_speed(cx=cx, cy=cy, throttle_output=throttle_output, v=v, v_desired=v_desired)

    def stanley_control(self, cx, cy, cyaw):

        cyaw = cyaw + d2r(90)

        closest_point = self.closest_node([cx, cy], self._waypoints)

        for i in range(len(self._waypoints)):
            if self._waypoints[i][0] == closest_point[0] and self._waypoints[i][1] == closest_point[1] and i not in (
            range(0, 10)):
                desired_yaw = np.arctan2(closest_point[1] - self._waypoints[i - 10][1],
                                         closest_point[0] - self._waypoints[i - 10][0]) + d2r(90)
                cross_track_error = self.cross_track_error(cx, cy, self._waypoints[i], self._waypoints[i - 10])
                crosstrack_error_dot = k * cross_track_error  # e_dot
                cross_track_steering = np.arctan2(crosstrack_error_dot,
                                                  Ks + self._current_speed)  # corrects cross track error
                # normalized_desired_yaw = self.normalize_angle(desired_yaw)
                normalized_desired_yaw = desired_yaw
                break

        heading_error = normalized_desired_yaw - cyaw  # corrects the heading error
        delta = heading_error + cross_track_steering
        normalized_delta = (1.22 if delta >= 1.22 else (-1.22 if delta <= -1.22 else delta))

        # self.log_stanley(cross_track_error=cross_track_error, cross_track_steering=cross_track_steering,
        #                  heading_error=heading_error,
        #                  desired_yaw=desired_yaw,
        #                  current_yaw=cyaw,
        #                  delta=delta,
        #                  normalized_delta=normalized_delta)
        # self.end_logging()

        return normalized_delta

    def pi_control(self, target, current):

        error = (target - current)
        self._integral += (error * dt)
        # derivative = (error - self.vars.v_error_previous) / dt
        # self.vars.v_error_previous = error
        u = (Kp * error) + (Ki * self._integral)
        return u

    def normalize_angle(self, angle):
        """
            Normalize an angle to [-pi, pi].
            :param angle: (float)
            :return: (float) Angle in radian in [-pi, pi]
            """
        while angle > np.pi:
            angle -= self._2pi
            print("subtracted pi/2")

        while angle < -np.pi:
            angle += self._2pi
            print("added pi/2")

        return angle

    @staticmethod
    def cross_track_error(cx, cy, next, prev):
        # trajectory line: point1(x_prev, y_prev), point2(x_curr, y_curr)
        a = -(prev[1] - next[1])
        b = (prev[0] - next[0])
        c = -(prev[0] * next[1] - next[0] * prev[1])

        try:
            cross_track_error = (a * cx + b * cy + c) / np.sqrt(a ** 2 + b ** 2)
        except ZeroDivisionError:
            return 0

        return cross_track_error

    @staticmethod
    def log_x_y_speed(cx, cy, throttle_output, v, v_desired):
        print("\n")
        print("desired speed = {}, current speed = {}, throttle = {}".format(v_desired, v, throttle_output))
        print("current x: {}, current y: {}".format(cx, cy))

    @staticmethod
    def log_stanley(cross_track_error, cross_track_steering, heading_error, desired_yaw, current_yaw, delta,
                    normalized_delta):
        print("cross track error: {}, heading error: {}".format(cross_track_error, r2d(heading_error)))
        print("cross track steering: {}".format(r2d(cross_track_steering)))
        print("desired yaw: {}".format(r2d(desired_yaw)))
        print("current yaw: {}".format(r2d(current_yaw)))
        print("steering angle: {}".format(r2d(delta)))
        print("normalized steering angle [-1.22, 1.22]: {}".format(r2d(normalized_delta)))

    @staticmethod
    def end_logging():
        print("-----------------------------------------------------------")

    @staticmethod
    def closest_node(node, waypoints):
        nodes = np.array([i[0:2] for i in waypoints])
        distance, index = spatial.KDTree(nodes).query(node)
        closest_point = nodes[index]
        return closest_point
