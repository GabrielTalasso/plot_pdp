from dash_interface.my_dash_components import ScatterplotComponent, LinearplotComponent, HistogramplotComponent, LinearHistComponent
from dash import dcc, html, Input, Output
import pandas as pd
from jupyter_dash import JupyterDash

def plot_comparative_pdp_dash(data, pdp_results, feature, models_name):

    pdp_dicts = []

    for i, pdp_result in enumerate(pdp_results):
        pdp_dict = {}
        pdp_dict['x'] = pdp_result['values'][0]
        pdp_dict['y'] = pdp_result['average'][0]
        pdp_dict['name'] = models_name[i]
        pdp_dicts.append(pdp_dict)

    app = JupyterDash(__name__)

    app.layout = html.Div([
    dcc.Graph(
        figure=dict(
            data=pdp_dicts,
            layout=dict(
                title='Comparative PDP between models',
                showlegend=True,
                legend=dict(
                    x=0,
                    y=1.0
                ),
                margin=dict(l=40, r=0, t=40, b=20)
            )
        ),
        style={'height': 300},
        id='comparative_pdp'
    )
])
    app.run_server(mode="inline")