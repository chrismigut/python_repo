"""
Generate equally spaced floating point
numbers between two give values
"""

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers


#Drawing the trajectory
#vy = u*sin(ϴ) - gt 
# peak time -> t = u*sin(ϴ) / g
# total time -> t = 2(u*sin(ϴ) / g)
# hight -> u*sin(ϴ)t - (1/2)gt**2
# distance -> u*cos(ϴ)t

import matplotlib.pyplot as plt
import math


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
    #plt.axis(ymin=0)
    #plt.axis(xmin=0)

def draw_trjectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    #Time of flight 
    t_flight = 2*u*math.sin(theta)/g
    #Find time intervals
    intervals = frange(0, t_flight, 0.001)

    #List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5*g*t**2)

    draw_graph(x, y)


if __name__ == '__main__':
    # try:
    #     u = float(input('Enter the initial velocity (m/s): '))
    #     theta = float(input("Enter the angle of projection (degrees): "))
    # except ValueError:
    #     print('You entered an invalid input')
    # else:
    #     draw_trjectory(u, theta)
    #     plt.show()

    # List of three different initial velocities
    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        draw_trjectory(u, theta)

    #Add a legend and show the graph
    plt.legend(['20', '40', '60'])
    plt.show()