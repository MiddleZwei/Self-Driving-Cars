# Self-Driving-Cars

<h3> Lane recognition </h3>
This is my first experience with programming self-driving cars. There're 2 approaches: robotic and deep learning. The technique in the video belongs to the former.<br><br>

Firstly I was trying to recognize lanes by color in the video and applying region of interest mask then. The problem #1: lanes can change color, therefore hardcoring colors is a really bad idea. Instead, we can use a technique called "Canny Edge Detection", which simply applies a gradient to an image(each frame of the video), then we black out pixels outside the desired range.<br><br>

Then as soon as we got the dotted image with Canny Edge Detection, we need a model of a line to be found and recognized. The model is y=mx+b in the usual Image Space. Next it should be translated into another coordinate plane called Hough Space. The model will look like b=-mx+y. A dot in Image space is gonna be a line in Hough Space. A line(a sequence of dots) in Image Space will be an intersection of many lines in Hough Space. The problem #2: vertical lines(lanes) have infinite slopes. Solution: another parameters and another formula are needed. We can use xcos(t)+ysin(t)=p. We still need the intersection, but this time curves will make it.<br><br>

At this point the lines can be found. Changing parameters' values will adjust the result. Then the region mask of interest is gonna be applied(assuming the camera on the car was fixed). And that's it.<br><br>


<h3> Iris dataset </h3>
<a href="https://github.com/MiddleZwei/Self-Driving-Cars/blob/master/KerasIrisDataset-NeuralNetwork/Iris%20Dataset-Keras.ipynb">Link to Iris dataset classification Jupyter Notebook</a> <br><br>
Used Sequential model and Dense layers<br>
Keras neural network models with scikit-learn<br>
Defined a neural network using Keras for multi-class classification <br>
Evaluated a Keras neural network model
