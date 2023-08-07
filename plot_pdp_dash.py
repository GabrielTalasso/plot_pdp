from dash_interface.my_dash_components import ScatterplotComponent, LinearplotComponent, HistogramplotComponent, LinearHistComponent
from dash import dcc, html, Input, Output
import pandas as pd
from jupyter_dash import JupyterDash

def plot_pdp_dash(data, pdp_results, feature):
    pdp_df = pd.DataFrame({'x': pdp_results['values'][0], 'y': pdp_results['average'][0]})
    pdp_dict = pdp_df.to_dict(orient='records')

    app = JupyterDash(__name__)

    app.layout = html.Div([
        LinearHistComponent(
            id='linear-hist',
            data=pdp_dict,
            histData=data.to_dict(orient='records'),
            x_axis='x',
            y_axis='y',
            histValue=feature
        ),
    ])
    app.run_server(mode="inline")