# Autonomous Drone
An autonomous drone localization and navigation software

![](https://github.com/prtpydv/autonomous-drone/blob/main/gif/wander.gif)

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

### Usage
![](https://github.com/prtpydv/autonomous-drone/blob/main/gif/loc_trac.gif)

![](https://github.com/prtpydv/autonomous-drone/blob/main/gif/nav.gif)
