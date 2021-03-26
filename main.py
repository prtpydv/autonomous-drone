from glider import *


def Gaussian(mu, sigma, x):
    # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
    return exp(- ((mu - x) ** 2.0) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))


def estimate_next_pos(height, radar, mapFunc, OTHER=None):
    """Estimate the next (x,y) position of the glider."""

    # Create N particles randomly distributed in -250,250 x&y range
    if OTHER is None:
        t = 0
        p_dict = {}
        OTHER = [t, p_dict]
        # Initialize 30k particles
        N = 30000
        p = []
        for i in range(N):
            g = glider()
            g.x = random.random() * 500 - 250
            g.y = random.random() * 500 - 250
            g.heading = random.gauss(0,pi/4)
            p.append(g)
    else:
        # Fetch particles from previous time step
        p = OTHER[1][OTHER[0]]
        # Increment time step
        OTHER[0] += 1

    # N
    N = len(p)

    # Importance weights
    w = []
    for i in range(N):
        prob = Gaussian(height - radar, 15, mapFunc(p[i].x, p[i].y))
        w.append(prob)

    # Resampling Wheel
    p3 = []
    index = int(random.random() * N)
    beta = 0.0
    mw = max(w)
    for i in range(N):
        beta += random.random() * 2.0 * mw
        while beta > w[index]:
            beta -= w[index]
            index = (index + 1) % N
        p3.append(p[index])
    p = p3

    # Reduce N from 30000 to 3000
    p = p[:2000]
    N = len(p)

    # Fuzz particles
    pFuzz = []
    for i in range(500):
        p[i].x += random.gauss(0,5)
        p[i].y += random.gauss(0,5)
        p[i].heading += random.gauss(0,pi/16)
        pFuzz.append(p[i])

    # Glide the particles
    p2 = []
    for i in range(N):
        p2.append(p[i].glide())
    p = p2

    # Update OTHER
    OTHER[1][OTHER[0]] = p

    # xy
    x_sum = 0
    y_sum = 0
    for i in range(N):
        x_sum += p[i].x
        y_sum += p[i].y
    x = x_sum/N
    y = y_sum/N

    xy_estimate = (x,y)

    optionalPointsToPlot = []
    for i in range(N):
        optionalPointsToPlot.append((p[i].x, p[i].y))

    return xy_estimate, OTHER, optionalPointsToPlot


def truncate_angle(t):
    return ((t + pi) % (2 * pi)) - pi


def next_angle(height, radar, mapFunc, OTHER=None):

    xy, OTHER, optP = estimate_next_pos(height, radar, mapFunc, OTHER)

    x = xy[0]
    y = xy[1]
    if OTHER[0] < 30:
        steering_angle = 0.0
    else:
        desired_angle = atan2(0 - y, 0 - x)
        vx = 0.0
        vy = 0.0
        n = len(OTHER[1][OTHER[0]])
        for i in range(n):
            vx += cos(OTHER[1][OTHER[0]][i].heading)
            vy += sin(OTHER[1][OTHER[0]][i].heading)
        vx /= n
        vy /= n
        current_heading = atan2(vy,vx)

        steering_angle = desired_angle - current_heading

        steering_angle = max(-pi / 8.0, steering_angle)
        steering_angle = min(steering_angle, pi / 8.0)

        for i in range(len(OTHER[1][OTHER[0]])):
            OTHER[1][OTHER[0]][i].heading += steering_angle
            OTHER[1][OTHER[0]][i].heading = angle_trunc(OTHER[1][OTHER[0]][i].heading)

    p = OTHER[1][OTHER[0]]
    optionalPointsToPlot = []
    for i in range(len(p)):
        optionalPointsToPlot.append((p[i].x, p[i].y))

    return steering_angle, OTHER, optionalPointsToPlot
