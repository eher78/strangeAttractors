# Code for Strange Attractors

from matplotlib import pyplot
from time import time


def draw(parameters):

    # unpack the parameters
    x, y, a = parameters

    # lists to store the entire path
    x_list = [x]
    y_list = [y]


    # iteratively pass (x,y) into the quadratic map
    for i in range(10000):

        # compute next point (using the quadratic map)
        xnew = a[0] + a[1]*x + a[2]*x*x + a[3]*y + a[4]*y*y + a[5]*x*y
        ynew = a[6] + a[7]*x + a[8]*x*x + a[9]*y + a[10]*y*y + a[11]*x*y

        # update (x, y)
        x = xnew
        y = ynew

        # store (x,y) in our path lists
        x_list.append(x)
        y_list.append(y)


    # clear figure
    pyplot.clf()

    # plot design
    pyplot.style.use("dark_background")
    pyplot.axis("off")

    #create the plot
    pyplot.scatter(x_list[100:], y_list[100:], s=0.1, c="white", linewidth = 0)

    #save the figure
    #pyplot.savefig("search/" + str(time) + ".png", dpi = 200)
    pyplot.savefig("gallery/" + "image.png", dpi = 200)
        

parameters = (0.2493215101235945, 0.040522862396523696, [0.9519762850997111, -0.30186386934628207, 1.9184522449084773, -1.9393458312245864, -1.2624463733517262, -0.7591625564104558, 0.09491195901780802, 1.215318161209535, 0.5183738662469501, -1.6267219553565733, -0.587972763195129, -0.5901108524880909])

draw(parameters)