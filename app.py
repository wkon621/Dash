import pandas as pd
from pandas import DataFrame
import plotly
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

newlocationsdf = pd.read_csv('./data/covid19.csv')

newlocationsdf['text'] = newlocationsdf['province'] + '<br>' + newlocationsdf['country'] + '<br>' + newlocationsdf['confirmed'].astype(str)
                                                                                                                  
fig = go.Figure(data=go.Scattergeo(
        locationmode = 'country names',
        lon = newlocationsdf['longitude'],
        lat = newlocationsdf['latitude'],
        text = newlocationsdf['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = False,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Reds',
            cmin = newlocationsdf['confirmed'].min(),
            color = newlocationsdf['confirmed'],
            cmax = newlocationsdf['confirmed'].max(),
            colorbar_title="Total Number Confirmed Cases"
        )))

fig.update_layout(
        title = 'Countries Affected by SARS-COV-2',
        geo = dict(
            scope='world',
            projection_type='natural earth',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
