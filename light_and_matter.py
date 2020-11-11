import random
import math
import numpy as np
from get_next_loc import *
from which_event import *
from consts import *
from check_in_block import in_which_block


def throw_photon(L, l_mean, p_abs):
    cur_x = 0
    cur_y = 0
    cur_theta = 0
    while True:
        cur_x, cur_x, length = get_next_loc(cur_x, cur_y, cur_theta, l_mean)
        what_happens = which_event_uniform(L, l_mean, p_abs)
        if in_which_block(cur_y) == -2:
            return "Reflected"
        elif in_which_block(cur_y) == -1:
            return "Transmitted"
        if what_happens == 'abs':
            return "Absorbed"
        if what_happens == 'sca':
            cur_theta = np.random.uniform(0, 2 * math.pi)


print(throw_photon(blocks[0], l_mean, p_abs))

