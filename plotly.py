import pandas as pd
# import plotly.graph_objects as go


def ReadColumn(csv, line_num): #csvと列番号を指定
    #csvからndarray型に変換
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num])
    # csvから読んだデータをnumpyの行列に入れる
    array = csvdata.values
    return array

# def showgraph(x_data, y_data):
#     fig = go.Figure([go.Scatter(x_data, y_data)])
#     fig.show()