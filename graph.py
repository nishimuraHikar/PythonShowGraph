import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def ReadColumn(csv, line_num): #csvと列番号を指定
    #csvからndarray型に変換
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num])
    # csvから読んだデータをnumpyの行列に入れる
    array = csvdata.values
    return array

# グラフ表示
# 1つのグラフ
def graph_1data(x_data, y_data, labelname):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 14
    plt.rcParams["axes.linewidth"] = 1.5

    plt.plot(x_data, y_data, c="darkorange", label=labelname)
    np.linspace(min(x_data), max(x_data), 100)
    # plt.ylim(-1.55, 1.55)
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
<<<<<<< HEAD
    plt.savefig('NNresult.png') #PNGファイル生成
    plt.show()

# マルチプロット2行1列
def multiplot_2and1(x_data, y_data1a, y_data1b, y_data2a, y_data2b, labelname1, labelname2, labelname3, labelname4):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 16
    plt.rcParams["axes.linewidth"] = 1.5

    plt.figure(figsize=[9, 7])
    # ax1 = fig.add_subplot(2, 1, 1)
    # ax2 = fig.add_subplot(2, 1, 2)

    plt.subplot(211)
    plt.plot(x_data, y_data1a, c="darkorange", label=labelname1)
    plt.plot(x_data, y_data1b, c="blue", label=labelname2)
    plt.ylabel("Force[N]", fontname = 'Times New Roman')
    plt.xlim(0, 60)
    plt.ylim(-0.1, 0.2)
    plt.axvspan(40, 60, color="gray", alpha=0.3)
    plt.legend(loc = 'upper left')

    plt.subplot(212)
    plt.plot(x_data, y_data2a, c="darkorange", label=labelname3)
    plt.plot(x_data, y_data2b, c="blue", label=labelname4)
    plt.ylabel("Force[N]", fontname = 'Times New Roman')
    plt.xlim(0, 60)
    plt.ylim(-0.1, 0.2)

    np.linspace(min(x_data), max(x_data), 100)
    plt.xlabel("Time[sec]", fontname = 'Times New Roman')
    plt.axvspan(40, 60, color="gray", alpha=0.3)
    plt.legend(loc = 'upper left')

    plt.tight_layout()
=======
    # plt.savefig('NNresult.png') #PNGファイル生成
>>>>>>> b9eaac676acfc1c66dcc4038d5f1e117d2488184
    plt.show()