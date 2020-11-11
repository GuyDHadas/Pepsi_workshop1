import numpy as np
import matplotlib.pyplot as plt
from consts import *


def in_which_block(cur_y):
    if cur_y < 0:
        return -2
    else:
        last_height = 0
        block_num = 0
        for i in range(len(blocks)):
            if cur_y < last_height + blocks[i]:
                return block_num
            block_num += 1
            last_height += blocks[i]
    return -1

