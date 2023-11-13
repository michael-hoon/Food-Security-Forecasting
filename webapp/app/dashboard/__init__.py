"""Instantiate a Dash app."""
import dash
from dash import dcc, html
from dash.dash_table import DataTable
from flask import Flask
from pandas import DataFrame
import plotly.express as px

from .data import create_dataframe
from .layout import html_layout


def init_dashboard(app: Flask):
    """
    Create a Plotly Dash dashboard within a running Flask app.

    :param Flask app: Top-level Flask application.
    """
    dash_module = dash.Dash(
        server=app,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    df = create_dataframe()

    # Custom HTML layout
    dash_module.index_string = html_layout
    
    #create graph
    fig = px.scatter_matrix(df, dimensions = ["Population", "GDP", "Infant mortality"])

    # Create Layout
    dash_module.layout = html.Div(
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure=fig,
            ),
            create_data_table(df),
        ],
        id="dash-container",
    )
    return dash_module.server


def create_data_table(df: DataFrame) -> DataTable:
    """
    Create Dash DataTable object from Pandas DataFrame.

    :param DataFrame df: Pandas DataFrame from which to build a Dash table.

    :returns: DataTable
    """
    table = DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table
