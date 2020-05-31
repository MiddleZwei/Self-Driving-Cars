## Kalman filter

Keywords: sensor fusion, motion and measurement model

Motion model: previous estimate, input(external signal like wheel torque), noise
Linear measurement model: outputted measurement based on parameter estimate and noise

Kalman filter is the recursive least squares method that includes a motion model.

Stages:
1. Prediction
2. Measurement
3. Correction (fusion)

##### Sources
Explained on matrices: https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/