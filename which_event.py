import numpy as np
from consts import *


def which_event_uniform(length):
    rnd_uni = np.random.uniform()
    if rnd_uni < p_abs:
        return "abs"
    elif rnd_uni < p_abs + mu_sca * length:
        return "sca"
    else:
        return ""


print(which_event_uniform(1))
