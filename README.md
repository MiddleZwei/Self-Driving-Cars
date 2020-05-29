# Self-Driving-Cars

### Path Tracking
![CARLA](https://gist.github.com/eli-halych/850a3bab978bc0fd169e56e159824fba/raw/8e61fdb2fae61b1a72582219d419ecd245e7c94f/carla_res.jpg)

This is part of my thesis I am working on till Feb 2020.
The main goal is go let the car follow the given path itself by making geometrical calculations on a 2D plane.
#### Technologies and environments used 
Python, CARLA simulator, PowerShell with Bash enabled and Windows 10
#### Main components
Stanley controller: converts heading error and cross track error to steering output (Lateral control)
PI controller: adjusts the current speed to the desired speed.
#### Upcoming experiments
1. Implemeting a Pure Pursuit controller which uses rear axel of the care and comparing it with the Stanely controller.
2. Adding state estimation and localiation methods to the project and a CNN and seeing how well the car performs after that.
#### Coursera
I am also taking a Specialization courses on Coursera
#### Future plans
In addition to that I am planning on using NIDIA's paper on a CNN architecture which also steers the car, but based on the view from the camera without providing the car with waypoints and the desired speed
#### Detailed explanation
More details are evailable in my presentation vie the link: <a href="https://drive.google.com/open?id=1Fb7CKlScm2huQBaP5_efO-Dg1dQln_am">Presentation</a><br><br>


### Lane recognition
<a href="https://www.instagram.com/p/BmCuaS4hw-y/">Link to the result(video)</a><br><br>
This was my first experience with technologies regarding self-driving cars. There're 2 approaches: robotic and deep learning. The technique in the video belongs to the former.<br><br>

Firstly I was trying to recognize lanes by color in the video and applying region of interest mask then. The problem #1: lanes can change color, therefore hardcoring colors is a really bad idea. Instead, we can use a technique called "Canny Edge Detection", which simply applies a gradient to an image(each frame of the video), then we black out pixels outside the desired range.<br><br>

Then as soon as we got the dotted image with Canny Edge Detection, we need a model of a line to be found and recognized. The model is y=mx+b in the usual Image Space. Next it should be translated into another coordinate plane called Hough Space. The model will look like b=-mx+y. A dot in Image space is gonna be a line in Hough Space. A line(a sequence of dots) in Image Space will be an intersection of many lines in Hough Space. The problem #2: vertical lines(lanes) have infinite slopes. Solution: another parameters and another formula are needed. We can use xcos(t)+ysin(t)=p. We still need the intersection, but this time curves will make it.<br><br>

At this point the lines can be found. Changing parameters' values will adjust the result. Then the region mask of interest is gonna be applied(assuming the camera on the car was fixed). And that's it.<br><br>
