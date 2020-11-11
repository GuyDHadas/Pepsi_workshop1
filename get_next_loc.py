import numpy as np
from math import *


def get_next_loc(current, theta, l_mean):
    l = np.random.exponential(l_mean, 1)
    new_y = l * sin(theta) + current[1]
    new_x = l * cos(theta) + current[0]
    return new_x, new_y