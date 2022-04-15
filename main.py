import graph

datafile = 'csv/predict_kotaro.csv'

timedata = graph.ReadColumn(datafile, 0)
inputdatax = graph.ReadColumn(datafile, 1)
# inputdatax2 = graph.MeticulousReadColum(datafile, 1, 100, 110)
predictdatax = graph.ReadColumn(datafile, 2)
inputdatay = graph.ReadColumn(datafile, 3)
predictdatay = graph.ReadColumn(datafile, 4)

# print(inputdatax2)

graph.multiplot_2and1(timedata,
                      inputdatax, predictdatax,
                      inputdatay, predictdatay,
                      1.5, 15.0, 60.0,
                      "Actual X", "Predict X", "Actual Y", "Predict Y")