import random
import math
import numpy as np
from get_next_loc import *
from which_event import *
from consts import *


def throw_photon(L, l_mean, p_abs):
    p = [0,0]
    theta = 0

    while True:
        p[0], p[1], length = get_next_loc(p[0], p[1], theta, l_mean)
        what_happens = which_event_uniform(length);
        if p[0] <= 0:
            return 0
        if p[0] >= L:
            return -1
        if what_happens == 'abs':
            return 1
        if what_happens == 'sca':
            theta = np.random.uniform(0, 2 * math.py)

check_in_block()

