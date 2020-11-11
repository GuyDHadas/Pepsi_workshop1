import random
import math
import numpy as np
from get_next_loc import *
from which_event import *
from consts import *
from check_in_block import *

import matplotlib.pyplot as plt

def const(x):
    return 2
def draw_path(loc_list, L):
    data = np.array(loc_list)
    plt.plot(data[:, 0], data[:, 1], color = 'b')
    plt.plot([-100, 100], [0, 0], marker = 'o', color = 'r')
    plt.plot([-100, 100], [L, L], marker = 'o', color = 'r')
    plt.plot([0, 0], [-2, 0], marker = 'o', color = 'b')

    for p in data:
        plt.scatter(p[0], p[1], s=25, color = 'b')
    plt.xlim(-10, 10)
    plt.ylim(8, -1)
    plt.title("Photon Trajectories")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.show()

def throw_photon(blocks, l_mean, p_abs):
    cur_x = 0
    cur_y = 0
    cur_theta = 0
    cur_block = 0
    #loc_list = [[0, 0]]
    while True:
        cur_x, cur_y, length = get_next_loc(cur_x, cur_y, cur_theta, l_mean[cur_block])
        #loc_list.append([cur_x[0], cur_y[0]])
        cur_block = in_which_block(cur_y)
        if cur_block == -2:
            #draw_path(loc_list, blocks[0])
            return "Reflected"
        elif cur_block == -1:
            #draw_path(loc_list, blocks[0])
            return "Transmitted"
        what_happens = which_event_uniform(length, cur_block, l_mean, p_abs)
        if what_happens == 'abs':
            #draw_path(loc_list, blocks[0])
            return "Absorbed"
        elif what_happens == 'sca':
            cur_theta = np.random.uniform(0, 2 * math.pi)
        #print(loc_list)

if __name__ == "__main__":
    print(throw_photon([5], l_mean, p_abs))

