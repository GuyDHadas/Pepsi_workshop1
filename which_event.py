import numpy as np
from consts import *


def which_event_uniform(length, cur_block, l_mean, p_abs):

    mu_sca = (1-p_abs[cur_block])/l_mean[cur_block]

    rnd_uni = np.random.uniform()
    if rnd_uni < p_abs[cur_block]:
        return "abs"
    elif rnd_uni < p_abs[cur_block] + mu_sca * length[cur_block]:
        return "sca"
    else:
        return ""
