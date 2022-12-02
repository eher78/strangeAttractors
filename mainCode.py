# Code for Strange Attractors

import random
from matplotlib import pyplot


found = False

while not found:
    converging = False

    # random starting point

    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)

    # random parameter vector 
    a = [random.uniform(-2, 2) for i in range(12)]

    # lists to store the entire path
    x_list = [x]
    y_list = [y]


    # iteratively pass (x,y) into the quadratic map
    for i in range(10000):

        # compute next point (using the quadratic map)
        xnew = a[0] + a[1]*x + a[2]*x*x + a[3]*y + a[4]*y*y + a[5]*x*y
        ynew = a[6] + a[7]*x + a[8]*x*x + a[9]*y + a[10]*y*y + a[11]*x*y

        # check if we converge to infinity
        if xnew > 1e10 or ynew > 1e10 or xnew < -1e10 or ynew < -1e10:
            converging = True
            break

        # check if we converge to a single point
        if abs(x - xnew) < 1e-10 and abs(y - ynew) < 1e-10:
            converging = True
            break

        # update (x, y)
        x = xnew
        y = ynew

        # store (x,y) in our path lists
        x_list.append(x)
        y_list.append(y)

    if not converging:
        found = True

print(len(x_list))
pyplot.scatter(x_list[100:], y_list[100:], s=0.1)
pyplot.show()
