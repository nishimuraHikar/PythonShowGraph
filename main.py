import graph

datafile = 'oct.csv'

timedata = graph.ReadColumn(datafile,0)
rawdata = graph.ReadColumn(datafile, 1)
predictdata = graph.ReadColumn(datafile, 2)

# graph.graph_1data(timedata, rawdata, "Raw Data")
graph.graph_2data(timedata, rawdata, predictdata, "Raw Data", "Predict Data")