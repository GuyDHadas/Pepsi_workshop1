import numpy as np
import math
from check_in_block import *


def get_next_loc(current_x, current_y, theta, l_mean, blocks):
    """returns the next location of proton"""
    block_index = in_which_block(current_y)
    l = np.random.exponential(l_mean[block_index], 1)
    new_y = l * math.cos(theta) + current_y
    new_x = l * math.sin(theta) + current_x
    if in_which_block(current_y) != block_index:
        new_y = block_index_2_y_value(block_index, blocks)
        return get_next_loc(new_x, new_y, theta, l_mean, blocks)
    return new_x, new_y, l


def block_index_2_y_value(block_index, blocks):
    """Returns the y of the bottom of the given block"""
    y = 0
    for i in range(block_index + 1):
        y += blocks[i]
    return y
