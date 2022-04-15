import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

def ReadColumn(csv, line_num): #csvと列番号を指定
    #csvからndarray型に変換
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num])
    # csvから読んだデータをnumpyの行列に入れる
    array = csvdata.values
    return array

## 1つのグラフ
def graph_1data(x_data, y_data, ylim, labelname):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 14
    plt.rcParams["axes.linewidth"] = 1.5

    plt.plot(x_data, y_data, c="darkorange", label=labelname)
    np.linspace(min(x_data), max(x_data), 100)
    plt.ylim(-ylim, ylim)
    # plt.ylim(min(y_data), max(y_data))
    plt.xlabel("Time[sec]", fontname = 'Times New Roman')
    plt.ylabel("Force[N]", fontname = 'Times New Roman')
    plt.legend()
    # plt.savefig('NNresult.png') #PNGファイル生成
    plt.show()


# 2つのグラフ
def graph_2data(x_data, y1_data, y2_data, labelname1, labelname2):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 14
    plt.rcParams["axes.linewidth"] = 1.5
    
    plt.plot(x_data, y1_data, c="darkorange", label=labelname1)
    plt.plot(x_data, y2_data, c="blue", label=labelname2)
    np.linspace(min(x_data), max(x_data), 100)
    # plt.ylim(-0.01, 0.01)
    # plt.ylim(min(y_data), max(y_data))
    plt.xlabel("Time[sec]", fontname = 'Times New Roman')
    plt.ylabel("Force[N]", fontname = 'Times New Roman')
    plt.legend()
#     plt.savefig('NNresult.png') #PNGファイル生成
#     plt.show()

# マルチプロット2行1列
def multiplot_2and1(x_data,
                    y_data1a, y_data1b, y_data2a, y_data2b,
                    ylim,backdroung_start,background_end,
                    labelname1, labelname2, labelname3, labelname4):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 16
    plt.rcParams["axes.linewidth"] = 1.5
    plt.figure(figsize=[10, 8])

    plt.subplot(211)
    plt.plot(x_data, y_data1a, c="darkorange", label=labelname1)
    plt.plot(x_data, y_data1b, c="blue", label=labelname2)
    # plt.xlabel("subject1", fontname = 'Times New Roman')
    plt.ylabel("Force[N]", fontname = 'Times New Roman')
    plt.xlim(0, 60)
    plt.ylim(-ylim, ylim)
    plt.axvspan(backdroung_start, background_end, color="gray", alpha=0.3)
    # plt.legend(loc = 'upper left', bbox_to_anchor = (0.5, 1.0), borderaxespad=0, ncol=2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    plt.subplot(212)
    plt.plot(x_data, y_data2a, c="darkorange", label=labelname3)
    plt.plot(x_data, y_data2b, c="blue", label=labelname4)
    # plt.xlabel("subject2", fontname='Times New Roman')
    plt.ylabel("Force[N]", fontname = 'Times New Roman')
    plt.xlim(0, 60)
    plt.ylim(-ylim, ylim)
    plt.axvspan(backdroung_start, background_end, color="gray", alpha=0.3)
    # plt.yticks(np.arange(-ylim, ylim, ystep))
    plt.legend(loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    np.linspace(min(x_data), max(x_data), 100)
    plt.xlabel("Time[sec]", fontname = 'Times New Roman')

    plt.tight_layout()
    plt.savefig("predict.pdf")
    plt.show()


# ヒストグラム
def histgram(data, binsnum, scale):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 16
    plt.rcParams["axes.linewidth"] = 1.5
    fig = plt.figure(figsize = [5,5])
    ax = fig.add_subplot(111)
    ax.hist(data, bins = binsnum, density = True)
    X = np.linspace(-0.1, 0.1, 50)
    Y = norm.pdf(X, loc=0, scale=scale)
    plt.ylabel("Frequency")
    plt.show()


def histgram2(data1, data2, binsnum, scale):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 16
    plt.rcParams["axes.linewidth"] = 1.5
    fig = plt.figure(figsize = [10,5])
    ax = fig.add_subplot(121)
    ax.hist(data1, bins = binsnum, density = True)
    X = np.linspace(-0.1, 0.1, 50)
    Y = norm.pdf(X, loc=0, scale=scale)
    plt.xlim(-0.02, 0.02)
    plt.ylim(0, 120)
    plt.xlabel("Error X")
    plt.ylabel("Frequency")

    bx = fig.add_subplot(122)
    bx.hist(data2, bins = binsnum, density = True)
    plt.ylim(0, 120)
    plt.xlim(-0.02, 0.02)
    plt.xlabel("Error Y")
    plt.ylabel("Frequency")
    # ax.plot(X, Y, c="red")
    plt.savefig("histgram.pdf")
    plt.show()