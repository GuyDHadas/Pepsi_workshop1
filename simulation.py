import random
import math
import numpy as np
from get_next_loc import *
from which_event import *
from consts import *
from matplotlib import pyplot as plt
from light_and_matter import *


def simulation():
    results = []

    L = 5
    l_mean = 3
    p_abs = 1/3

    for i in range(0, 10**5):
        results.append(throw_photon(L, l_mean, p_abs))

    plt.figure()
    plt.hist(results, bins = 3)
    plt.show()


simulation()
