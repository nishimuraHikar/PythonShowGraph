import graph
import numpy as np

# -------------w/, w/o assistant system--------------------------
datafile = ''

# ---------------------------------------------------------------

# ---------------------crlnn--------------------------------------
# datafile = '../../CLionProjects/crlnn_for_task/Result/predict.csv'
# timedata = graph.ReadColumn(datafile, 0)
# actualx = graph.ReadColumn(datafile, 1)
# predictx = graph.ReadColumn(datafile, 2)
# errorx = graph.ReadColumn(datafile, 11)
# actualy = graph.ReadColumn(datafile, 3)
# predicty = graph.ReadColumn(datafile, 4)
# errory = graph.ReadColumn(datafile, 19)
# gain = graph.ReadColumn(datafile, 21)
#
# # graph.multiplot_2and1(timedata,
# #                       actualx, predictx, actualy, predicty,
# #                       1.5, 50.0, 60.0,
# #                       "Actual", "Predict", "Actual", "Predict")
#
# graph.multiplot_2and2(timedata,
#                       actualx, predictx,
#                       errorx,
#                       actualy, predicty,
#                       errory,
#                       gain,
#                       0.0, 60.0, 2.0,
#                       "Actual", "Predict", "Actual", "Predict")
# ---------------------------------------------------------------


# -------------------------RMSE---------------------------------
# datafile = "rms of rfob.csv"
# # data1 = graph.ReadColumn(datafile, 3)
# # data2 = graph.ReadColumn(datafile, 4)
#
# data1 = [0.017021652, 0.014626248, 0.01620128, 0.013319736, 0.012920719, 0.01497583, 0.016604496, 0.011281695, 0.023799976, 0.014142109]
# data2 = [0.004067754, 0.00401095, 0.003602331, 0.002941454, 0.003990596, 0.004687634, 0.0055581, 0.002696973, 0.005786211, 0.00290697]
# # print(type(data2.T[0]))
#
# # ddata1 = data1.T[0]
# # ddata2 = data2.T[0]
# # print(ddata1.tolist())
# # print(data2)
# # graph.ErrorBar("W/OAssist", "W/Assist", ddata1.tolist(), ddata2.tolist())
# graph.ErrorBar("W/OAssist", "W/Assist", data1, data2)
#
# # data3 = [0.015489, 0.004025]
# # graph.ErrorBar("aaa", "aa", data3, data3)
# --------------------------------------------------------------


# --------------------correlation------------------------------
# datafile = '../../CLionProjects/crlnn_for_task/Result/predict.csv'
# timedata = graph.ReadColumn(datafile, 0)
# actualx = graph.ReadColumn(datafile, 1)
# predictx = graph.ReadColumn(datafile, 2)
# errorx = graph.ReadColumn(datafile, 11)
# actualy = graph.ReadColumn(datafile, 3)
# predicty = graph.ReadColumn(datafile, 4)
# errory = graph.ReadColumn(datafile, 19)
#
# skip_value = 50
# time_start = 15.0
# time_end = 20.0
#
#
# cut_predictx = graph.Edited(timedata, predictx, time_start, time_end)
# cut_actualx = graph.Edited(timedata, actualx, time_start, time_end)
# cut_predicty = graph.Edited(timedata, predicty, time_start, time_end)
# cut_actualy = graph.Edited(timedata, actualy, time_start, time_end)
# cut_errorx = graph.Edited(timedata, errorx, time_start, time_end)
# cut_errory = graph.Edited(timedata, errory, time_start, time_end)
#
# reliancex = np.abs(cut_predictx[1::skip_value]) - np.abs(cut_actualx[1::skip_value])
# reliancey = np.abs(cut_predicty[1::skip_value]) - np.abs(cut_actualy[1::skip_value])
# cut_errorx = cut_errorx[1::skip_value]
# cut_errory = cut_errory[1::skip_value]
# # cut_errorx = np.abs(cut_errorx[1::skip_value])
# # cut_errory = np.abs(cut_errory[1::skip_value])
#
# graph.Scatter(reliancex, cut_errorx)