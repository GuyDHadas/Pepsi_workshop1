import numpy as np
from math import *


def get_next_loc(current_x, current_y, theta, l_mean):
    """returns the next location of proton"""
    l = np.random.exponential(l_mean, 1)
    new_y = l * cos(theta) + current_y
    new_x = l * sin(theta) + current_x
    return new_x, new_y, l
