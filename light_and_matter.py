import random
import math
import numpy as np
from get_next_loc import *
from which_event import *
from consts import *
from check_in_block import *


def throw_photon(blocks, l_mean, p_abs):
    cur_x = 0
    cur_y = 0
    cur_theta = 0
    cur_block = 0
    while True:
        cur_x, cur_y, length = get_next_loc(cur_x, cur_y, cur_theta, l_mean[cur_block])
        cur_block = in_which_block(cur_y)
        if cur_block == -2:
            return "Reflected"
        elif cur_block == -1:
            return "Transmitted"
        what_happens = which_event_uniform(length, cur_block, l_mean, p_abs)
        if what_happens == 'abs':
            return "Absorbed"
        elif what_happens == 'sca':
            cur_theta = np.random.uniform(0, 2 * math.pi)


print(throw_photon(blocks[0], l_mean, p_abs))

