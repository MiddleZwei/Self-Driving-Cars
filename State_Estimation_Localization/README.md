Python version: Python 3.7.4

### General notes !

Before blindly applying maximum likelihood estimation or the method of least 
squares, it is important to quantify errors (uncertainties, a.k.a. outliers of 
a PDF).

Reason why? Self-driving cars' sensors may notice objects other than expected, 
like pedestrians or barriers and that may cause uncertainties in measurements.
Outliers affect the least squares and maximum likelihood methods.

Reference to quantification of uncertainties: 
https://en.wikipedia.org/wiki/Uncertainty_quantification
 

## (Batch) Least Squares Method
All the measurements are available to us at once (as a batch).

## Recursive Least Squares
Estimation based on new measurements streaming in.
No need to recompute every time a new measurement is received.
Includes time series in the observations so each observation is assigned to a 
particular time step.

Make updated optimal estimation (kind of a prediction) of a current timestep 
given current measurement and the previous estimate.

Forms the update step of the linear Kalman filter.

## Maximum likelihood estimation

Looking at the probability density function of a measurement,
the value of a measurement that is most likely to happen is located at the 
mean whereas the variance is the noise.