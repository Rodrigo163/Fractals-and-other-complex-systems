#Using only NumPy
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib.animation import FuncAnimation


def lorenz(x, y, z, s=10, r=28, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

num_steps = 10000

# Need one more for the initial values
xs = [0.0]
ys = [1.0]
zs = [1.05]


fig = plt.figure()
ax = fig.gca(projection='3d')
plot, = ax.plot(0, 1, 1.05) #initial datapoint in the plot
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

def animation_frame(i):
    global xs
    global ys
    global zs
    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    dt = 0.01

    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs.append(xs[i] + (x_dot * dt))
    ys.append(ys[i] + (y_dot * dt))
    zs.append(zs[i] + (z_dot * dt))

    plot.set_data((xs, ys,zs))

    
    return plot,

anim = FuncAnimation(fig, func = animation_frame, frames=45, interval=120, blit=True)
plt.show()

