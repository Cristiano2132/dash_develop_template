import dash
import dash_bootstrap_components as dbc
from dash import html

from dash import html, Dash, dcc
import dash_mantine_components as dmc


app_dash = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    requests_pathname_prefix='/dash/',
    external_stylesheets=[
        'https://use.fontawesome.com/releases/v5.8.1/css/all.css'
    ]
)



app_dash.layout = html.Div([
    dmc.MediaQuery([dmc.Navbar(
        fixed=True,
        width={"base": 250},
        height="100%",
        style={"top": 0},
        children=[
            dmc.Group(
                position="column",
                grow=True,
                spacing="xl",
                children=[
                    dmc.List(
                        center=True,
                        children=[
                            dmc.ListItem(
                                dcc.Link('Home', href='/'),
                                icon=[
                                    html.I(className='fas fa-home fa-fw fa-lg')],
                                className='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('Data', href='/analytics'),
                                icon=[
                                    html.I(className='fas fa-chart-bar fa-fw fa-lg')],
                                className='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('Map', href='/map'),
                                icon=[
                                    html.I(className='fas fa-map fa-fw fa-lg')],
                                className='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('More Maps',
                                         href='/distro'),
                                icon=[
                                    html.I(className='fas fa-map-marker fa-fw fa-lg')],
                                className='nav-list-items'),
                        ])
                ])
        ])], smallerThan="md", styles={'display': 'none'}),
    dmc.MediaQuery([dmc.Navbar(
        fixed=True,
        width={"base": 60},
        height="100%",
        style={"top": 0},
        children=[
            dmc.List(
                center=True,
                children=[
                    dmc.ListItem(
                        dcc.Link(
                            html.I(className='fas fa-home fa-fw fa-lg'), href='/'),
                        className='nav-list-items'
                    ),
                    dmc.ListItem(
                        dcc.Link(
                            html.I(className='fas fa-chart-bar fa-fw fa-lg'), href='/'),
                        className='nav-list-items'
                    ),
                    dmc.ListItem(
                        dcc.Link(
                            html.I(className='fas fa-map fa-fw fa-lg'), href='/'),
                        className='nav-list-items'
                    ),
                    dmc.ListItem(
                        dcc.Link(
                            html.I(className='fas fa-map-marker fa-fw fa-lg'), href='/'),
                        className='nav-list-items'
                    )
                ])
        ])], largerThan="md", styles={'display': 'none'})
])

if __name__ == '__main__':
    app_dash.run_server(
        host='0.0.0.0',
        port=8050,
        debug=True,
        dev_tools_props_check=True
    )
