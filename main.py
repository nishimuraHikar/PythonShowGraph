import graph
import matplotlib.pyplot as plt

datafile = 'csv/kotaro_predict.csv'

# timedata = graph.ReadColumn(datafile, 0)
# inputdatax = graph.ReadColumn(datafile, 1)
# # inputdatax2 = graph.Edited(timedata, timedata, 15)
# predictdatax = graph.ReadColumn(datafile, 2)
# inputdatay = graph.ReadColumn(datafile, 3)
# predictdatay = graph.ReadColumn(datafile, 4)
# reliancex = inputdatax - predictdatax
# reliancey = inputdatay - predictdatay

timedata = graph.MeticulousReadColum(datafile, 0, 14500, 62527)
inputdatax = graph.MeticulousReadColum(datafile, 1, 14500, 62527)
predictdatax = graph.MeticulousReadColum(datafile, 2, 14500, 62527)
inputdatay = graph.MeticulousReadColum(datafile, 3, 14500, 62527)
predictdatay = graph.MeticulousReadColum(datafile, 4, 14500, 62527)
reliancex = inputdatax - predictdatax
reliancey = inputdatay - predictdatay
rx = predictdatax / inputdatax
ry = predictdatay / inputdatay
perfomancex = graph.MeticulousReadColum(datafile, 7, 14500, 62527)
perfomancey = graph.MeticulousReadColum(datafile, 8, 14500, 62527)

# Editeddata = []
# for i in range(len(timedata)):
#     Editeddata[i] = graph.Edited(timedata[i], timedata[i], 15)
#     print(Editeddata[i])
# print(inputdatax2)

# graph.obj_multiplot_2and1(timedata,
#                       inputdatax, predictdatax,
#                       inputdatay, predictdatay,
#                       1.5, 15.0, 60.0,
#                       "Actual X", "Predict X", "Actual Y", "Predict Y")

graph.multiplot_2and2(timedata,
                      inputdatax, predictdatax,
                      reliancex,
                      inputdatay, predictdatay,
                      reliancey,
                      15, 60, 1.5,
                      "Actual x", "Predict x", "Actual y", "Predict y")

# print(type(reliancex))
# graph.Scatter(reliancex.T[0], perfomancex.T[0])
# plt.scatter(reliancex.T[0], perfomancex.T[0])
# plt.show()