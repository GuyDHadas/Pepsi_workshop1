import random
import math
import numpy as np
from get_next_loc import *
from which_event import *
from consts import *
from matplotlib import pyplot as plt
from light_and_matter import *
import scipy.stats


def simulation():
    results = []

    blocks = [5]
    l_mean = [3]
    p_abs = [1/3]


    pabs = []
    ptrans = []
    pref = []
    pabs_err = []
    ptrans_err = []
    pref_err = []
    for N in range(1, 6):
        for j in range(20):
            for i in range(0, 10**N):
                results.append(throw_photon(blocks, l_mean, p_abs))
            tran = results.count("Transmitted")
            abs = results.count("Absorbed")
            ref = results.count("Reflected")
            results = []
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
        print("abs", np.average(pabs1), scipy.stats.sem(pabs1))
        print("trans", np.average(ptrans1), scipy.stats.sem(ptrans1))
        print("ref", np.average(pref1), scipy.stats.sem(pref1))
        pabs_err.append(scipy.stats.sem(pabs1))
        ptrans_err.append((scipy.stats.sem(ptrans1)))
        pref_err.append(scipy.stats.sem(pref1))
    plt.loglog([10**N for N in range(1, 6)], pref_err, label=r'$p_ref$ error')
    plt.loglog([10**N for N in range(1, 6)], ptrans_err, label=r'$p_trans$ error')
    plt.loglog([10**N for N in range(1, 6)], pabs_err, label=r'$p_abs$ error')
    plt.xlabel("Number of photons thrown")
    plt.ylabel("Statistical error")
    plt.title("Convergence check - statistical errors")
    plt.show()



simulation()
