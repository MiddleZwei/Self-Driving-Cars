# Visual perception

This module covered 3 topics: [***Environment perception***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/environment_perception/Environment%20Perception%20For%20Self-Driving%20Cars.ipynb), [***Stereo depth***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/stereo_depth/Applying%20Stereo%20Depth%20to%20a%20Driving%20Scenario.ipynb) and [***Visual odometry***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/visual_odometry/Visual%20Odometry%20for%20Localization%20in%20Autonomous%20Driving.ipynb). 

! Accesses each folder here to find relevant Jupyter Notebook with detailed explanations and visualizations.

-> [Certificate](https://www.coursera.org/verify/C3LPCT2Z5MA6)

## Environment perception

The main goal of this submodule is the extraction of useful information to allow self-driving cars to safely and reliably traverse their environment.

##### Tools

*Python 3.7, Numpy, OpenCV, Metplotlib, Jupyter Notebook, matrices.*

##### The course of work

Given a colormap, a segmentation map, a category table do the following:

1. Estimate (x, y, z) coordinates of every pixel using formulas and a camera calibration matrix.
2. Estimate the ground plane (estimate the parameters) using *RANSAC* for outlier rejection. 
3. Estimate lane boundary proposals with OpenCV and *Canny edge detection* together with Hough transform.
4. Merge and filter lane lines to leave just horizontal lines bounded to the road lanes.
5. Compute minimum distance to impact (how far or close an obstacle is).
6. Filter out bad detections and estimate the distance

Source file: [***Jupyter Notebook***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/environment_perception/Environment%20Perception%20For%20Self-Driving%20Cars.ipynb)

## Stereo depth

The main goal of this submodule is the estimation of distance to an obstacle on a stereo input (left and right images).

##### Tools

*Python 3.7, Numpy, OpenCV, Metplotlib, Jupyter Notebook, matrices.*

#### The course of work

1. Compute the disparity by using OpenCV's *StereoSGBM*
2. Decompose projection matrices to get translation and rotation parameter as well as the camera calibration matrix.
3. Get the depth map from the above parameters using formulas.
4. Find the distance to the collision with OpenCV's *minMaxLoc* and draw a bounding box.

Source file: [***Jupyter Notebook***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/stereo_depth/Applying%20Stereo%20Depth%20to%20a%20Driving%20Scenario.ipynb)

## Visual odometry for localization

The main goal of this submodule is the estimation of trajectory based on an input from a monocular camera.

##### Tools

*Python 3.7, Numpy, OpenCV, Metplotlib, Jupyter Notebook, matrices*.

#### The course of work

1. Extract features from an image that will be tracked for trajectory estimation. I used OpenCVs *SURF*, but *FAST, SIFT, ORB* can also be used.
2. Repeat the extraction for all the images in a dataset.
3. Match the features for subsequent images to define the change for each move by using OpenCV's *Flann Based Matcher* and *KNN Match*.
4. Draw the matches for the dataset.
5. Estimate the motion by using *Essential Matrix Decomposition*.
6. Visualize.

Source file: [***Jupyter Notebook***](https://github.com/eli-halych/self-driving-cars-specialization/blob/master/visual_perception/visual_odometry/Visual%20Odometry%20for%20Localization%20in%20Autonomous%20Driving.ipynb).