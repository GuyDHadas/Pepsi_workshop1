import numpy as np
from consts import *


def which_event_uniform(length, l_mean, p_abs):

    mu_sca = (1-p_abs)/l_mean

    rnd_uni = np.random.uniform()
    if rnd_uni < p_abs:
        return "abs"
    elif rnd_uni < p_abs + mu_sca * length:
        return "sca"
    else:
        return ""
