from time import time
import graph
import numpy as np

# datafile1 = 'tozuka1.csv'
# datafile = 'false.csv'
datafile = 'predict.csv'

# timedata = graph.ReadColumn(datafile1,0)
# forcedatax = graph.ReadColumn(datafile1, 14)
# forcedatax_ = graph.ReadColumn(datafile1, 31)
# forcedatay = graph.ReadColumn(datafile1, 29)
# forcedatay_ = graph.ReadColumn(datafile1, 32)

timedata = graph.ReadColumn(datafile, 0)
inputdatax = graph.ReadColumn(datafile, 1)
predictdatax = graph.ReadColumn(datafile, 2)
inputdatay = graph.ReadColumn(datafile, 3)
predictdatay = graph.ReadColumn(datafile, 4)


# graph.graph_1data(timedata, rawdata, "Raw Data")
# graph.graph_2data(timedata, rawdata, predictdata, "Raw Data", "Predict Data")
# graph.multiplot_2and1(timedata, forcedatax, predictdatax, forcedatay,predictdatay, "Actual X", "Predict X", "Actual Y", "Predict Y")
# graph.histgram(forcedatax-predictdatax, 1000, 100)
graph.multiplot_2and1(timedata, inputdatax, predictdatax, inputdatay, predictdatay, "Actual", "Predict", "Actual", "Predict")
# graph.multiplot_2and1(timedata, forcedatax, forcedatax_, forcedatay, forcedatay_, "W/O Assist", "W/ Assist", "W/O Assist", "W/ Assist")
# graph.multiplot_2and1(timedata, forcedatax, predictdatax, forcedatay,predictdatay, "Actual X", "Predict X", "Actual Y", "Predict Y")
