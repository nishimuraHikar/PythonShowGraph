import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

from scipy.stats import norm


def ReadColumn(csv, line_num):  # csvと列番号を指定
    # csvからndarray型に変換
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num], sep=',')
    # csvから読んだデータをnumpyの行列に入れる
    array = csvdata.values
    return array


# 使う行を選択
def MeticulousReadColum(csv, line_num, StartLine, EndLine):
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num])
    SpecificLine = csvdata.loc[StartLine:EndLine]
    array = SpecificLine.values
    return array


# 使う範囲を選択(時間ベース)
def Edited(time, data, time_start, time_end):
    trashdata = 0.0
    time_start_num = 0.0
    time_end_num = 0.0
    num = 0
    # 要素数算出
    for i in range(len(data)):
        if time[i] >= time_start and time_start_num == 0.0: # [time_start]秒のときの要素を保存
            time_start_num = i
        elif time[i] >= time_end and time_end_num == 0.0: # [time_end]秒のときの要素を保存
            time_end_num = i

    # 空のリストを作成
    cutdata = [0.0] * (time_end_num - time_start_num)

    # 空リストに格納
    while num < time_end_num:
        if (time_start <= time[num]) and (time[num] <= time_end):
            cutdata[num - time_start_num] = data[num - time_start_num].T[0]
            # print("i : ", num, " , time : ", time[num], " , cutdata : ", cutdata[num - time_start_num])
        elif (time_start > time[num]) or (time[num] > time_end):
            trashdata = data[num]
        num += 1
    return cutdata


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
    plt.xlabel("Time[sec]", fontname='Times New Roman')
    plt.ylabel("Force[N]", fontname='Times New Roman')
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
    plt.figure(figsize=[10, 6])

    plt.plot(x_data, y1_data, c="darkorange", label=labelname1)
    plt.plot(x_data, y2_data, c="blue", label=labelname2)
    # np.linspace(min(x_data), max(x_data), 100)
    plt.xlim(0, 60)
    plt.ylim(-1.5, 1.5)
    # plt.ylim(min(y_data), max(y_data))
    plt.xlabel("Time[sec]", fontname='Times New Roman')
    plt.ylabel("Force[N]", fontname='Times New Roman')
    plt.axvspan(50, 60, color="gray", alpha=0.3)
    plt.legend(loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)
    plt.savefig('NNresult.png')  # PNGファイル生成
    plt.show()


# マルチプロット2行1列
def multiplot_2and1(x_data,
                    y_data1a, y_data1b, y_data2a, y_data2b,
                    ylim, backdroung_start, background_end,
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
    # plt.fill_between(x_data.T[0], y_data1a.T[0], y_data1b.T[0], where >= backdroung_start, facecolor="lime", alpha=0.5)
    # plt.xlabel("subject1", fontname = 'Times New Roman')
    plt.ylabel("Force[N]", fontname='Times New Roman')
    plt.xlim(0, 60)
    plt.ylim(-ylim, ylim)
    plt.xlabel("X axis", fontname='Times New Roman')
    plt.axvspan(backdroung_start, background_end, color="gray", alpha=0.3)
    # plt.legend(loc = 'upper left', bbox_to_anchor = (0.5, 1.0), borderaxespad=0, ncol=2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    plt.subplot(212)
    plt.plot(x_data, y_data2a, c="darkorange", label=labelname3)
    plt.plot(x_data, y_data2b, c="blue", label=labelname4)
    # plt.fill_between(x_data.T[0], y_data2a.T[0], y_data2b.T[0], facecolor="lime", alpha=0.5)
    # plt.xlabel("subject2", fontname='Times New Roman')
    plt.ylabel("Force[N]", fontname='Times New Roman')
    plt.xlim(0, 60)
    plt.ylim(-ylim, ylim)
    plt.xlabel("Y axis", fontname='Times New Roman')
    plt.axvspan(backdroung_start, background_end, color="gray", alpha=0.3)
    # plt.yticks(np.arange(-ylim, ylim, ystep))
    plt.legend(loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    np.linspace(min(x_data), max(x_data), 100)

    plt.tight_layout()
    plt.savefig("predict.png")
    now = datetime.datetime.now()
    print(now)
    plt.show()


# オブジェクト指向型
def obj_multiplot_2and1(x_data,
                        y_data1a, y_data1b, y_data2a, y_data2b,
                        ylim, backdroung_start, background_end,
                        labelname1, labelname2, labelname3, labelname4):
    fig = plt.figure(figsize=[10, 8])
    font = {'family': 'Times New Roman', 'size': 16}

    # 2行1列のグラフ
    ax1 = fig.add_subplot(211, xlim=(15, 60), ylim=(-ylim, ylim), ylabel="Force[N]")
    ax2 = fig.add_subplot(212, xlim=(15, 60), ylim=(-ylim, ylim), ylabel="Force[N]")
    fig.subplots_adjust(wspace=0.5, hspace=0.5)

    # １つ目のグラフ
    ax1.plot(x_data, y_data1a, c="darkorange", label=labelname1)
    ax1.plot(x_data, y_data1b, c="blue", label=labelname2)
    ax1.set_ylabel("Force[N]", fontdict=font)
    ax1.tick_params(direction="in", width="1.5")
    ax1.fill_between(x_data.T[0], y_data1a.T[0], y_data1b.T[0], facecolor="lime", alpha=0.5)
    # for i in range(len(y_data1a)):
    #     if(y_data1a[i] - y_data1b[i] > 0):
    #         ax1.fill_between(x_data.T[0], y_data1a[i].T[0], y_data1b[i].T[0], facecolor="lime", alpha=0.5)
    #     elif(y_data1a[i] - y_data1b[i] <= 0):
    #         ax1.fill_between(x_data.T[0], y_data1a[i].T[0], y_data1b[i].T[0], facecolor="deepskyblue", alpha=0.5)
    # ax1.axvspan(backdroung_start, background_end, color="gray", alpha=0.3)
    ax1.legend(fontsize=15, loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    # ２つ目のグラフ
    ax2.plot(x_data, y_data2a, c="darkorange", label=labelname3)
    ax2.plot(x_data, y_data2b, c="blue", label=labelname4)
    ax2.set_ylabel("Force[N]", fontdict=font)
    ax2.tick_params(direction="in", width="1.5")
    ax2.fill_between(x_data.T[0], y_data2a.T[0], y_data2b.T[0], facecolor="lime", alpha=0.5)
    # if(np.all(np.abs(y_data2a > y_data2b))):
    #     ax2.fill_between(x_data.T[0], y_data2a.T[0], y_data2b.T[0], where=x_data.T[0] >= backdroung_start,
    #                      facecolor="lime", alpha=0.5)
    # elif(np.all(np.abs(y_data2a < y_data2b))):
    #     ax2.fill_between(x_data.T[0], y_data2a.T[0], y_data2b.T[0], where=x_data.T[0] >= backdroung_start,
    #                      facecolor="deepskyblue", alpha=0.5)
    # ax2.axvspan(backdroung_start, background_end, color="gray", alpha=0.3)
    ax2.legend(fontsize=15, loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    fig.tight_layout()
    fig.savefig("predict.pdf")
    plt.show()


# マルチプロット2行2列
def multiplot_2and2(x_data,
                    y_data10, y_data11,
                    y_data20,
                    y_data30, y_data31,
                    y_data40,
                    assist,
                    x_start, x_end, ylim,
                    labelname10, labelname11, labelname20, labelname21):
    fig = plt.figure(figsize=[16, 8])
    font = {'family': 'Times New Roman', 'size': 16}

    # 2行2列のグラフ
    ax1 = fig.add_subplot(221, xlim=(x_start, x_end), ylim=(-ylim, ylim))
    ax2 = fig.add_subplot(223, xlim=(x_start, x_end), ylim=(-0.04, 0.04))
    ax3 = fig.add_subplot(222, xlim=(x_start, x_end), ylim=(-ylim, ylim))
    ax4 = fig.add_subplot(224, xlim=(x_start, x_end), ylim=(-0.04, 0.04))

    # １つ目のグラフ
    ax1.plot(x_data, y_data10, c="darkorange", label=labelname10)
    ax1.plot(x_data, y_data11, c="blue", label=labelname11)
    ax1.plot(x_data, assist, c="green", label="Assist gain")
    ax1.set_xlabel("X axis", fontdict=font)
    ax1.set_ylabel("Force[N]", fontdict=font)
    ax1.hlines(y=0, xmin=x_start, xmax=x_end, color='gray', linestyle='dashed', linewidth=2)
    ax1.tick_params(direction="in", width="1.5")
    # ax1.fill_between(x_data.T[0], y_data10.T[0], y_data11.T[0], facecolor="lime", alpha=0.5)
    ax1.legend(fontsize=15, loc='upper center', bbox_to_anchor=(0.6, 1.0), borderaxespad=0, ncol=3)

    # ２つ目のグラフ
    ax2.plot(x_data, y_data20, c="red")
    ax2.set_xlabel("Time[sec]", fontdict=font)
    ax2.set_ylabel("Error[m]", fontdict=font)
    ax2.hlines(y=0, xmin=x_start, xmax=x_end, color='gray', linestyle='dashed', linewidth=2)
    ax2.tick_params(direction="in", width="1.5")

    # ３つ目のグラフ
    ax3.plot(x_data, y_data30, c="darkorange", label=labelname20)
    ax3.plot(x_data, y_data31, c="blue", label=labelname21)
    ax3.plot(x_data, assist, c="green", label="Assist gain")
    ax3.set_xlabel("Y axis", fontdict=font)
    ax3.set_ylabel("Force[N]", fontdict=font)
    ax3.hlines(y=0, xmin=x_start, xmax=x_end, color='gray', linestyle='dashed', linewidth=2)
    ax3.tick_params(direction="in", width="1.5")
    # ax3.fill_between(x_data.T[0], y_data30.T[0], y_data31.T[0], facecolor="lime", alpha=0.5)
    ax3.legend(fontsize=15, loc='upper center', bbox_to_anchor=(0.6, 1.0), borderaxespad=0, ncol=3)

    # ４つ目のグラフ
    ax4.plot(x_data, y_data40, c="red")
    ax4.set_xlabel("Time[sec]", fontdict=font)
    ax4.set_ylabel("Error[m]", fontdict=font)
    ax4.hlines(y=0, xmin=x_start, xmax=x_end, color='gray', linestyle='dashed', linewidth=2)
    ax4.tick_params(direction="in", width="1.5")

    plt.tight_layout()
    plt.savefig("Reliance.png")
    plt.show()


def Scatter(data1, data2):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 18
    plt.rcParams["axes.linewidth"] = 1.5
    plt.figure(figsize=[10, 8])

    np.linspace(min(data1), max(data1), 100)
    plt.xlabel("Reliance[N]", fontname='Times New Roman')
    plt.ylabel("Error[m]", fontname='Times New Roman')
    plt.scatter(data1, data2, s=10, c="blue", alpha=0.8, linewidths=2, edgecolors="blue")
    plt.savefig('correlation.png')
    plt.show()


def multiplot_3and1(x_data,
                    y_data11, y_data12, labelname11, labelname12,
                    y_data21, y_data22, labelname21, labelname22,
                    y_data31, y_data32, labelname31, labelname32,
                    ylim):
    fig = plt.figure(figsize=[10, 8])
    font = {'family': 'Times New Roman', 'size': 16}

    # 3行1列のグラフ
    ax1 = fig.add_subplot(311, xlim=(15, 60), ylim=(-ylim, ylim), ylabel="Force[N]")
    ax2 = fig.add_subplot(312, xlim=(15, 60), ylim=(-ylim, ylim), ylabel="Force[N]")
    ax3 = fig.add_subplot(313, xlim=(15, 60), ylim=(-ylim, ylim), ylabel="Force[N]")
    fig.subplots_adjust(wspace=0.5, hspace=0.5)

    # １つ目のグラフ
    ax1.plot(x_data, y_data11, c="darkorange", label=labelname11)
    ax1.plot(x_data, y_data12, c="blue", label=labelname12)
    ax1.set_ylabel("Force[N]", fontdict=font)
    ax1.tick_params(direction="in", width="1.5")
    ax1.legend(fontsize=15, loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    # ２つ目のグラフ
    ax2.plot(x_data, y_data21, c="darkorange", label=labelname21)
    ax2.plot(x_data, y_data22, c="blue", label=labelname22)
    ax2.set_ylabel("Force[N]", fontdict=font)
    ax2.tick_params(direction="in", width="1.5")
    ax2.legend(fontsize=15, loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    # 3つ目のグラフ
    ax3.plot(x_data, y_data31, c="darkorange", label=labelname31)
    ax3.plot(x_data, y_data32, c="blue", label=labelname32)
    ax3.set_ylabel("Force[N]", fontdict=font)
    ax3.tick_params(direction="in", width="1.5")
    ax3.legend(fontsize=15, loc='upper center', bbox_to_anchor=(0.21, 1.0), borderaxespad=0, ncol=2)

    fig.tight_layout()
    fig.savefig("predict.pdf")
    plt.show()


def ErrorBar(labelname1, labelname2,
             data1, data2):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 16
    plt.rcParams["axes.linewidth"] = 1.5
    plt.figure(figsize=[8, 8])

    # num = [1, 2]
    width = 0.4
    x = np.arange(1, 11)
    # label = ["W/O Assist", "W/ Assist"]
    plt.ylabel("RMSE [m]")
    plt.ylim(0, 0.025)
    plt.xticks(x)
    plt.bar(x - width, data1, align="edge", label=labelname1, width=width)
    plt.bar(x, data2, align="edge", label=labelname2, width=width)
    # plt.legend(loc=2)
    plt.savefig("rms3.png")
    plt.show()
    # plt.bar(len(data2), data2, align="center")


# ヒストグラム
def histgram(data, binsnum, scale):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["font.size"] = 16
    plt.rcParams["axes.linewidth"] = 1.5
    fig = plt.figure(figsize=[5, 5])
    ax = fig.add_subplot(111)
    ax.hist(data, bins=binsnum, density=True)
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
    fig = plt.figure(figsize=[10, 5])
    ax = fig.add_subplot(121)
    ax.hist(data1, bins=binsnum, density=True)
    X = np.linspace(-0.1, 0.1, 50)
    Y = norm.pdf(X, loc=0, scale=scale)
    plt.xlim(-0.02, 0.02)
    plt.ylim(0, 120)
    plt.xlabel("Error X")
    plt.ylabel("Frequency")

    bx = fig.add_subplot(122)
    bx.hist(data2, bins=binsnum, density=True)
    plt.ylim(0, 120)
    plt.xlim(-0.02, 0.02)
    plt.xlabel("Error Y")
    plt.ylabel("Frequency")
    # ax.plot(X, Y, c="red")
    plt.savefig("histgram.pdf")
    plt.show()
