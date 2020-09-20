## Kalman filter

#### Linear Kalman Filter

Keywords: sensor fusion, motion and measurement model

Motion model: previous estimate, input(external signal like wheel torque), noise
Linear measurement model: outputted measurement based on parameter estimate and noise

Kalman filter is the recursive least squares method that includes a motion model.

Stages:
1. Prediction
2. Measurement
3. Correction (fusion)

##### Kalman filter is BLUE
Best Linear Unbiased Estimator meaning it is:
- unbiased
- consistent
- has the lowest variance estimator using linear combination of measurements

But most systems are not linear. Autonomous cars need to estimate non linear 
quantities like position and orientation in 2D and 3D.

##### Sources
Explained on matrices: https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/

#### Nonlinear (extended) Kalman Filter - EKF

IDEA: linearization of nonlinear systems similar to the rising resistance with 
the a resistor heating up (rising exponentially).

Ways:
- in 2D finding tangent lines (slopes) using for example Tailor's series, only
the first order

Notes:
- Jacobian matrix tells how fast each output of the function is changing along 
each input dimension. Having 2 inputs and 3 outputs, the Jacobian matrix will
have dimensions (2, 3). It contains 1st order partial derivatives.


Orientation for example is not linear and in 3D lives on a sphere.


