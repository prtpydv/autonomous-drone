# Autonomous Drone
An autonomous drone localization and navigation software

![](https://github.com/prtpydv/autonomous-drone/blob/main/gif/nav.gif)

### About the Project
We built a framework to localize, navigate and track an autonomous drone using Particle Filters.

Particle Filters are a type of Bayes Filters using a predict/update cycle to estimate the state 
of a dynamical system from sensor measurements. Particle Filters scale more easily to higher dimensions
than some other methods such as Kalman Filters as PFs attempt to find only an approximate solutions which
are computationally more tractable. The key idea behind PF is that by creating a broad
space of several hypotheses, called "particles," we can narrow down the space to an approximate solution by 
continuously measuring and updating our estimates.

### Built With
* Python 3.8

### Demo
* Localization
Our drone was successfully able to determine its current location with respect to the environment 
in less than 30 seconds on 95% of test cases. 
Robot localization is an important precursor to navigation as without knowing its current position,
the robot cannot make good decisions about future actions.

![](https://github.com/prtpydv/autonomous-drone/blob/main/gif/loc_trac.gif)

* Tracking
Once the drone was able to localize accurately, our software was able to keep track of the drone's location
with 100% probability, without ever losing it.

* Navigation
The final task left for our drone was to navigate itself toward a target destination. We demonstrate
navigating the drone toward the center of the screen at (0,0). The target destination can be updated
to make the drone follow a certain path.

![](https://github.com/prtpydv/autonomous-drone/blob/main/gif/nav.gif)
