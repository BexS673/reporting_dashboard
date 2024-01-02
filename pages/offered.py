from dash import register_page, dcc, Output, Input, callback
from dash import html
import pandas as pd
import plotly.express as px
from calendar import month_name

register_page(__name__)

hires_month_TA_df = pd.read_csv("src/pages/test_data.csv", encoding='utf-8')
hires_month_TA_fig = px.line(hires_month_TA_df, 
                                     x='Month', 
                                     y="Hires", 
                                     color="TA",
                                     title="Hires per month per TA")
months = list(hires_month_TA_df['Month'])
month_YTD = [month for month in list(month_name) if month in months]


x_from = dcc.Dropdown([html.Option(month) for month in month_YTD], month_YTD[0], id="month-from")
x_to = dcc.Dropdown([html.Option(month) for month in month_YTD], month_YTD[-1], id="month-to")

hires_month_TA_graph = dcc.Graph(id="hires-month-TA", figure=hires_month_TA_fig)

def layout():
    return html.Div([
        html.P("Select month from"),
        x_from,
        html.P("Select month to"),
        x_to,
        hires_month_TA_graph,
])

@callback(
    Output("hires-month-TA", 'figure'),
    [Input('month-from', 'value'),
     Input('month-to', 'value')]
)
def select_range(selected_month_from, selected_month_to):
    hires_month_TA_fig.update_layout(xaxis_range=[selected_month_from, selected_month_to])
