from time import time
import graph
import numpy as np

datafile = 'predict.csv'

timedata = graph.ReadColumn(datafile,0)
forcedatax = graph.ReadColumn(datafile, 1)
predictdatax = graph.ReadColumn(datafile, 2)
forcedatay = graph.ReadColumn(datafile, 3)
predictdatay = graph.ReadColumn(datafile, 4)

# graph.graph_1data(timedata, rawdata, "Raw Data")
# graph.graph_2data(timedata, rawdata, predictdata, "Raw Data", "Predict Data")
# graph.multiplot_2and1(timedata, forcedatax, predictdatax, forcedatay,predictdatay, "Actual X", "Predict X", "Actual Y", "Predict Y")
graph.histgram(forcedatax-predictdatax, 1000000, 100)