from time import time
import graph

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