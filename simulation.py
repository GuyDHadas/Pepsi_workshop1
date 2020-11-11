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

    blocks = [5]
    l_mean = [3]
    p_abs = [1/3]


    pabs = []
    ptrans = []
    pref = []
    for N in range(1, 7):
        for i in range(0, 10**N):
            results.append(throw_photon(blocks, l_mean, p_abs))
        tran = results.count("Transmitted")
        abs = results.count("Absorbed")
        ref = results.count("Reflected")
        pabs.append(abs/10**N)
        ptrans.append(tran/10**N)
        pref.append((ref/10**N))
    pabs1 = np.array(pabs)
    ptrans1 = np.array(ptrans)
    pref1 = np.array(pref)
    #plt.figure()
    #plt.hist(results, bins = 3)
    #plt.title("Histogram of photons' results")
    #plt.ylabel("Number of photons")
    #plt.show()
    print("abs", np.average(pabs1), np.err



simulation()
