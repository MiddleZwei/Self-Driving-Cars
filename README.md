# [Self-Driving-Cars Specialization](https://www.coursera.org/specializations/self-driving-cars)

This is the specialization I took when I was an ***undergraduate student in Robotics***. I was interested in ***autonomous driving*** and how it will benefit the society.

The specialization consists of ***4 advanced courses***: [Path Tracking](https://www.coursera.org/learn/intro-self-driving-cars), [State Estimation and Localization](https://www.coursera.org/learn/state-estimation-localization-self-driving-cars), [Perception](https://www.coursera.org/learn/visual-perception-self-driving-cars), [Motion Planning](https://www.coursera.org/learn/motion-planning-self-driving-cars). Each consists of a variety of quizzes, Jupyter Notebooks for you to practice. Path Tracking and Motion Planning each ends with a final project that requires you to use [CARLA simulator](https://carla.org/), skeleton code and what you've learnt during the course.

The Path Tracking course and its final project became the basis for my **Bachelor thesis** at [PJAIT](https://www.pja.edu.pl/en/) with the topic: Effect of lookahead distance on the ***Pure pursuit controller***'s cross-track error and comparison with ***the Stanley controller***. Graduated in Feb 2020.

-> [Certificate](https://www.coursera.org/verify/specialization/JMHJVBRLHZMJ)

## 1. Path Tracking - final project, thesis basis
#### todo: VIDEO/GIF DEMO of the final project


The main goal is go let the car follow the given path itself by making geometrical calculations on a 2D plane.

#### Technologies and environments used 
Python, CARLA simulator, PowerShell with Bash enabled and Windows 10
#### Main components
Stanley controller: converts heading error and cross track error to steering output (Lateral control).
PI controller: adjusts the current speed to the desired speed (Longitudinal control).

#### Major key points
Major key points are available in my presentation: <a href="https://drive.google.com/open?id=1Fb7CKlScm2huQBaP5_efO-Dg1dQln_am">Presentation</a>

## 2. State Estimation and Localization

todo: materials and techniques covered

## 3. Perception

I learnt and applied solutions to the main autonomous driving perception tasks based on monocular and stereo cameras to estimate the depth of an image and estimate the trajectory of a vehicle.

Main topics covered are [***Environment perception***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/environment_perception/Environment%20Perception%20For%20Self-Driving%20Cars.ipynb), [***Stereo depth***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/stereo_depth/Applying%20Stereo%20Depth%20to%20a%20Driving%20Scenario.ipynb) and [***Visual odometry***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/visual_odometry/Visual%20Odometry%20for%20Localization%20in%20Autonomous%20Driving.ipynb).

For the description of each topic I worked on and technologies used, please visit [this README](./visual_perception/README.md). There you will also find Jupyter Notebooks that were the basis for implementing the solutions in the tasks.

## 4. Motion Planning

#### todo: VIDEO/GIF DEMO of the final project

The main goal of the project is to implement a state machine to complete several tasks using specific methods. The description of these tasks can be found [HERE](./motion_planning/final_project/README.md)

#### Technologies and environments used 

Python, CARLA simulator, PowerShell with Bash enabled and Windows 10

#### An opportunity!

After successfully completing the course I was in touch with a guy from Germany and we agreed to collaboration on our own project to grow our skills in motion planning. Most likely it will be implementation of various maneuver test cases in CARLA simulator.


## Lane recognition as a the beginning of my interest in AV
<a href="https://www.instagram.com/p/BmCuaS4hw-y/">Link to the result(video)</a>

This was my first experience with technologies regarding self-driving cars. 

There're 2 approaches: geometric and deep learning. The technique in the video belongs to the geometric approach.

Firstly I was trying to recognize lanes by color in the video and then applying region of interest mask. 

***The problem #1***: lanes can change color, therefore hardcoding colors is a really bad idea. 

Instead, we can use a technique called "*Canny Edge Detection*", which simply applies a gradient to an image(each frame of the video), then we black out pixels outside the desired range.

Then as soon as we got the dotted image with *Canny Edge Detection*, we need a model of a line to be found and recognized. 

The model is *y=mx+b* in the usual *Image Space*. Next it should be translated into another coordinate plane called *Hough Space*. The model will look like b=-mx+y. 

A dot in Image space is gonna be a line in *Hough Space*. A line(a sequence of dots) in *Image Space* will be an intersection of many lines in *Hough Space*. 

***The problem #2***: vertical lines (lanes) have infinite slopes. 

Solution: another parameters and another formula are needed. We can use *xcos(t)+ysin(t)=p*. We still need the intersection, but this time curves will make it.

At this point the lines can be found. Changing parameters' values will adjust the result. Then the region mask of interest is gonna be applied (assuming the camera on the car was fixed).
