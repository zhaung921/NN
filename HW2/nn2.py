from os import close, times
import random
import math
from tkinter.constants import W
from matplotlib import colors

import matplotlib.pyplot as plt
import numpy as np

start_deg = 90
# edge=[[-6,3],[6,3],[-6,22],[6,10],[18,22],[30,10],[18,50],[30,50]]


def detection(x, y):
    # area1
    if x > -6 and x < 6 and y < 10 and y > -3:
        print('move,area1')
        left_dis = x-(-6)
        right_dis = 6-x
        front_dis = 22-y
        return left_dis, right_dis, front_dis
    # area2
    elif x > -6 and x < 6 and y < 22 and y >= 10:
        print('move,area2')
        left_dis = x-(-6)
        right_dis = 6-x
        front_dis = 22-y
        return left_dis, right_dis, front_dis
    # area3
    elif x >= 6 and x < 18 and y < 22 and y > 10:
        print('move,area3')
        left_dis = x-(-6)
        right_dis = 30-x
        front_dis = 22-y
        return left_dis, right_dis, front_dis
    # area4
    elif x >= 18 and x < 30 and y < 22 and y > 10:
        print('move,area4')
        left_dis = x-(-6)
        right_dis = 30-x
        front_dis = 50-y
        return left_dis, right_dis, front_dis
    # area5
    elif x > 18 and x < 30 and y < 50 and y >= 22:
        print('move,area5')
        left_dis = x-18
        right_dis = 30-x
        front_dis = 50-y
        return left_dis, right_dis, front_dis
    else:
        print('collision')
        return-1, -1, -1


def move(x, y, pos_deg, hand_deg):
    x = x+math.cos(pos_deg+hand_deg)+math.sin(hand_deg)*math.sin(pos_deg)
    y = y+math.sin(pos_deg+hand_deg)-math.sin(hand_deg)*math.cos(pos_deg)
    pos_deg = pos_deg-np.arcsin((2*math.sin(hand_deg))/6)
    return x, y, pos_deg


left_dis, right_dis, front_dis = detection(28, 22)
print(left_dis, right_dis, front_dis)
