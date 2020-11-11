import random
import math
import numpy as np

def check_in_block(L, l_mean, p_abs):
    p = [0,0]
    teta = 0

    while True:
        p[0], p[1], length = get_next_location(p, teta, l_mean)
        what_happ = wich_event_uniform(length)
        if p[0] <= 0:
            return 0
        if p[0] >= L:
            return -1
        if what_happ == 'abs':
            return 1
        if what_happ == 'sca':
            teta = np.random.uniform(0, 2 * math.py)



#def photon_throw(L, l_mean, p_abs):


