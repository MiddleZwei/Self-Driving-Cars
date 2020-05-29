Python version: Python 3.7.4

#### (Batch) Least Squares Method
All the measurements are available to us at once (as a batch).

#### Recursive Least Squares
Estimation based on new measurements streaming in.
No need to recompute every time a new measurement is received.
Includes time series in the observations so each observation is assigned to a particular time step..

Make updated optimal estimation (kind of a prediction) of a current timestep given current measurement and the previous estimate.

Forms the update step of the linear Kalman filter.



