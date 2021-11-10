from os import times
import random

import matplotlib.pyplot as plt
import numpy as np

success = 1


def train(w, tran_data, traing_ans, rate, endup, test_endtimes):
    print(np.size(tran_data, 0))

    n = 0
    times = 0
    actime = 0
    find_ = 0
    train_ac = 0

    # 開始找w值(training)
    while(train_ac < endup and times < test_endtimes):
        out = np.dot(w, tran_data[n])
        #print('oldw', w)
        if out >= 0:
            vj = 1
        elif out < 0:
            vj = 0
        if vj != traing_ans[n]:  # 要找到好的w
            # print("fail")
            if vj > traing_ans[n]:  # 我需要負的
                for i in range(3):
                    w[i] = w[i]-(rate*tran_data[n][i])
            elif vj < traing_ans[n]:
                for i in range(3):
                    w[i] = w[i]+(rate*tran_data[n][i])
        else:
            #print('traindata', tran_data[n])
            #print(vj, traing_ans[n], w)
            find_ += 1
        n += 1
        actime += 1
        if n >= np.size(tran_data, 0):
            times += 1
            train_ac = find_/actime
            find_ = 0
            n = 0
            actime = 0

    #print("endtrain", train_ac)
    return w, train_ac
