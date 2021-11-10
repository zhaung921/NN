from os import close, times
import random
import math
from tkinter.constants import W
from matplotlib import colors

import matplotlib.pyplot as plt
import numpy as np

import train
import store_data
import gui


def choose_batch(rows, batch_size, input_data, traing_ans, test_ans):
    #print(x22, x33)
    choose_ = []
    choose_.append(random.sample(range(0, rows), batch_size))
    choose_ = np.array(choose_)
    choose_ = choose_.astype(int)
    choose_.sort()

    # 設定train
    traing_ans = []
    test_ans = []
    train_data = np.array(input_data[choose_])
    for i in choose_[0]:
        if input_data[i][3] > 1:
            traing_ans.append(0)
        else:
            traing_ans.append(input_data[i][3])
    traing_ans = np.array(traing_ans)
    traing_ans = traing_ans.astype(float)
    train_data = train_data.astype(float)
    train_data = np.delete(train_data[0], 3, 1)
    print('train_data', train_data)
    print('traing_ans', traing_ans)

    # 設定test
    #print('input_data', input_data)
    print()
    input_data = np.delete(input_data, choose_[0], axis=0)
    #print('input_data after delete', input_data)
    test_data = input_data.astype(float)
    for i in range(np.size(test_data, 0)):
        if test_data[i][3] > 1:
            test_ans.append(0)
        else:
            test_ans.append(test_data[i][3])
    test_data = np.delete(test_data, 3, 1)
    test_ans = np.array(test_ans)
    #print('test_ans', test_ans)
    #print('test_data', test_data)
    #print('size', np.size(test_data, 0))
    return train_data, traing_ans, test_data, test_ans


def start(endup, test_endtimes, rate, fliename):
    # 檔案資料處理
    endup = float(endup)
    test_endtimes = int(test_endtimes)
    rate = float(rate)
    with open(fliename, "r")as f1:
        # C:\Program Files (x86)\py
        # D:\py\perceptron1.txt
        # ‪D:\py\perceptron1.txt

        test = []
        ans1 = []
        traing_ans = []
        test_ans = []
        choose_ = []
        #rate = 1.8
        #endup = 1.0
        #test_endtimes = 500
        x22 = []
        x33 = []
        o22 = []
        o33 = []
        for line in f1:
            line = line.strip().split()
            test.append(line)
        input_data = np.array(test)
        input_data = input_data.astype(float)
        nagtive = np.full((np.size(input_data, 0), 1), -1)
        input_data = np.hstack((nagtive, input_data))
        rows = np.size(input_data, 0)
        clo = np.size(input_data, 1)
        batch_size = math.ceil(rows*2/3)
        for i in range(rows):
            if input_data[i][3] == 0 or input_data[i][3] == 2:
                x22.append(input_data[i][1])
                x33.append(input_data[i][2])
            else:
                o22.append(input_data[i][1])
                o33.append(input_data[i][2])
        x22 = np.array(x22)
        x22 = x22.astype(float)
        x33 = np.array(x33)
        x33 = x33.astype(float)
        o22 = np.array(o22)
        o22 = o22.astype(float)
        o33 = np.array(o33)
        o33 = o33.astype(float)
        train_data, traing_ans, test_data, test_ans = choose_batch(
            rows, batch_size, input_data, traing_ans, test_ans)
        #print('input_data', input_data)
        #w = np.array(([[0], [0], [0], [0]]))
        w = np.array([random.random(),
                      random.random(), random.random()])
        w, train_ac = train.train(w, train_data, traing_ans,
                                  rate, endup, test_endtimes)
        #print('out:', type(traing_ans), type(test_ans))

        # test 開始
        test_ac = 0
        n = 0
        times = 0
        actime = 0
        find_ = 0
        while(test_ac < endup and times < np.size(test_data, 0)*6):
            out = np.dot(w, test_data[n])
            if out >= 0:
                vj = 1
            elif out < 0:
                vj = 0
            if vj != test_ans[n] and n == (np.size(test_data, 0)-1) and test_ac < endup:
                # print()
                # print(w)
                #print(vj, test_ans)
                # print('retrain')
                traing_ans = traing_ans.tolist()
                test_ans = test_ans.tolist()
                train_data, traing_ans, test_data, test_ans = choose_batch(
                    rows, batch_size, input_data, traing_ans, test_ans)
                w, train_ac = train.train(w,
                                          train_data, traing_ans, rate, endup, test_endtimes)
            elif vj == test_ans[n]:
                find_ += 1
            n += 1
            times += 1
            actime += 1
            if n >= np.size(test_data, 0):
                test_ac = find_/actime
                find_ = 0
                actime = 0
                n = 0

            #print(times, test_ac)
        #print(find_, times, actime)
        #print('testdata:', test_data)
        print('w:', w)
        store_data.w = w
        print("training accuracy:", train_ac)
        store_data.train_ac = train_ac
        print("test accuracy:", test_ac)
        store_data.test_ac = test_ac

        # 繪圖開始
        x2 = np.linspace(min(min(x22), min(o22)), max(max(x22), max(o22)), 5)
        x3 = np.linspace(min(min(x33), min(o33)), max(max(x33), max(o33)), 5)
        x3 = (w[0]*(-1)+w[1]*x2)/(-1*w[2])
        #x3 = (1.28+2.234*x2)/5.302
        plt.plot(x2, x3, 'g', linewidth=1)
        d1 = plt.scatter(x22, x33, marker='x')
        d2 = plt.scatter(o22, o33, marker='o')
        gui.setdata()
        plt.show()
