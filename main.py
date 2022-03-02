from time import time
import graph

<<<<<<< HEAD
datafile = 'predict.csv'

timedata = graph.ReadColumn(datafile,0)
forcedatax = graph.ReadColumn(datafile, 1)
predictdatax = graph.ReadColumn(datafile, 2)
forcedatay = graph.ReadColumn(datafile, 3)
predictdatay = graph.ReadColumn(datafile, 4)

# graph.graph_1data(timedata, rawdata, "Raw Data")
# graph.graph_2data(timedata, rawdata, predictdata, "Raw Data", "Predict Data")
graph.multiplot_2and1(timedata, forcedatax, predictdatax, forcedatay,predictdatay, "Actual X", "Predict X", "Actual Y", "Predict Y")
=======
datafile = 'predict_badassist.csv'

timedata = graph.ReadColumn(datafile,0)
teachdatax = graph.ReadColumn(datafile, 1)
predictdatax = graph.ReadColumn(datafile, 2)
seconddatax = graph.ReadColumn(datafile, 3)
Reliancex = graph.ReadColumn(datafile, 4)
teachdatay = graph.ReadColumn(datafile, 5)
predictdatay = graph.ReadColumn(datafile, 6)
seconddatay = graph.ReadColumn(datafile, 7)
Reliancey = graph.ReadColumn(datafile, 8)

# graph.graph_1data(timedata, rawdata, "Raw Data")
graph.graph_2data(timedata, teachdatax, predictdatax, "Teach_Forcex", "Predictionx")
graph.graph_2data(timedata, teachdatay, predictdatay, "Teach_Forcey", "Predictiony")
graph.graph_2data(timedata, seconddatax, predictdatax, "w/Assistx", "predictionx")
graph.graph_2data(timedata, seconddatay, predictdatay, "w/Assisty", "predictiony")
graph.graph_1data(timedata, Reliancex, "Reliancex")
graph.graph_1data(timedata, Reliancey, "Reliancey")
>>>>>>> b9eaac676acfc1c66dcc4038d5f1e117d2488184
