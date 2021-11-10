from tkinter import *
from tkinter.filedialog import askopenfile
import tkinter as tk

import nn_hw1test2
import store_data

window = tk.Tk()
window.title("HW1")
window.geometry('400x300')
header_label = tk.Label(window, text='作業1')
header_label.pack()
inbtn = tk.Button(window, text='file', width=10, command=lambda: upload())
inbtn.pack()

ad_frame = tk.Frame(window)
ad_frame.pack(side=tk.TOP)
ad_lable = tk.Label(ad_frame, text='')
ad_lable.pack(side=tk.LEFT)


acc_frame = tk.Frame(window)
acc_frame.pack(side=tk.TOP)
acc_label = tk.Label(acc_frame, text='準確率')
acc_label.pack(side=tk.LEFT)
acc_entry = tk.Entry(acc_frame)
acc_entry.pack(side=tk.LEFT)


train_frame = tk.Frame(window)
train_frame.pack(side=tk.TOP)
train_label = tk.Label(train_frame, text='訓練數')
train_label.pack(side=tk.LEFT)
train_entry = tk.Entry(train_frame)
train_entry.pack(side=tk.LEFT)


learn_frame = tk.Frame(window)
learn_frame.pack(side=tk.TOP)
learn_label = tk.Label(learn_frame, text='學習率')
learn_label.pack(side=tk.LEFT)
learn_entry = tk.Entry(learn_frame)
learn_entry.pack(side=tk.LEFT)

start_btn = tk.Button(window, text='計算', command=lambda: str_butclick())
start_btn.pack()

w_frame = tk.Frame(window)
w_frame.pack(side=tk.TOP)
w_lable = tk.Label(w_frame, text='鍵結值:')
w_lable.pack(side=tk.LEFT)

trac_frame = tk.Frame(window)
trac_frame.pack(side=tk.TOP)
trac_lable = tk.Label(trac_frame, text='訓練辨識率:')
trac_lable.pack(side=tk.LEFT)

teac_frame = tk.Frame(window)
teac_frame.pack(side=tk.TOP)
teac_lable = tk.Label(teac_frame, text='測試辨識率:')
teac_lable.pack(side=tk.LEFT)


def str_butclick():
    nn_hw1test2.start(acc_entry.get(), train_entry.get(),
                      learn_entry.get(), filename)


def upload():
    global filename
    global ad_lable
    filename = tk.filedialog.askopenfilename(filetypes=[('file', '.txt')])
    ad_lable['text'] = filename
    # print(filename)


def setdata():
    w_lable['text'] = '鍵結值:'+str(store_data.w)
    trac_lable['text'] = '訓練辨識率:'+str(store_data.train_ac)
    teac_lable['text'] = '測試辨識率:'+str(store_data.test_ac)


window.mainloop()
