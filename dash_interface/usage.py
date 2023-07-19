import os
import my_dash_components
from dash import Dash, dcc, callback, html, Input, Output
import pandas as pd

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'src/demo/data.tsv')
iris = pd.read_csv(filename,sep="\t")
iris_array_of_dicts = iris.to_dict(orient='records')

app = Dash(__name__)

app.layout = html.Div([
    my_dash_components.ScatterplotComponent(
        id='input',
        data=iris_array_of_dicts
    ),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])

@app.callback(
    Output("input", "data"), 
    Input("range-slider", "value"))
def update_bar_chart(value):
    low, high = value
    mask = (iris['petalWidth'] > low) & (iris['petalWidth'] < high)
    res = iris[mask].to_dict(orient='records')
    return res

if __name__ == '__main__':
    app.run_server(debug=True)
