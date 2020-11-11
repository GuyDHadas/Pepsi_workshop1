import random
import math
import numpy as np
from get_next_loc import *
from which_event import *
from consts import *
from check_in_block import in_which_block


def throw_photon(L, l_mean, p_abs):
    p = [0,0]
    theta = 0

    while True:
        p[0], p[1], length = get_next_loc(p[0], p[1], theta, l_mean)
        what_happens = which_event_uniform(L, l_mean, p_abs);
        if in_which_block(p[1]) == -2 or in_which_block(p[1]) == -1
            return in_which_block(p[1])
        if what_happens == 'abs':
            return 1
        if what_happens == 'sca':
            theta = np.random.uniform(0, 2 * math.pi)

def simulation():
    results = []

    L = 5
    l_mean = 3
    p_abs = 1/3
    mu_sca = 2/9

    for i in range (0,10**5):
        results.append(throw_photon



print(throw_photon(blocks[0], l_mean, p_abs))

