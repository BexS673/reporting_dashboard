
from dash import Dash, dcc, html, Input, Output, State
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from figures import graphs, custom_report_options, dataframe_to_csv, dataframes, generate_download_button

app = Dash(__name__, external_stylesheets=[dbc.themes.LITERA], suppress_callback_exceptions=True)

#STYLES
SUMMARY_STYLE = {"margin":"2rem"}
CARD_STYLE = {"margin":"1rem"}
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 59,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

#Functions
def generate_navbar(title):
    return dbc.NavbarSimple(

        [
            sidebar
        ],
    color="dark",
    dark=True,
    id="nav-title",
    brand=title
)

sidebar_tabs = dbc.Nav(
        [
            dbc.NavLink("Dashboard", href="/", active="extract"),
            dbc.NavLink("Start Dates", href="/start_dates", active="extract"),
            dbc.NavLink("Gannt Chart", href="/gannt", active="extract"),
            dbc.NavLink("Custom Reports", href="/generate", active="extract"),
        ],
        vertical=True,
        pills=True
    )
        
sidebar = html.Div([

    dbc.Button("Reporting Menu", id="open-sidebar", n_clicks=0),
    dbc.Offcanvas(
        [
            html.H2("Reporting", className="display-4"),
            html.Hr(),
            sidebar_tabs,   
        ],    
        id="sidebar",
        title="ReportingMenu",
        is_open=False,
        )
    ]
)

average_TA_hire = [
    html.H3("Hired"),
    html.Hr(),
    html.H4(0)     
]

average_unit_hire = [
    html.H3("Hired"),
    html.Hr(),
    html.H4(0)  
]

average_unit_offer = [
    html.H3("Offered"),
    html.Hr(),
    html.H4(0)  
]

average_TA_offer = [
    html.H3("Offered"),
    html.Hr(),
    html.H4(0)  
]
    
total_rejected_content = [
        html.H3("Total Rejected"),
        html.Hr(),
        html.H4(0)        
    ]

total_offered_content = [
        html.H3("Total Offered"),
        html.Hr(),
        html.H4(0),
    ]

total_hired_content = [
        html.H3("Total Hired"),
        html.Hr(),
        html.H4(0),
    ]

more_details_summary_TA = dbc.Card(
    [
        dbc.CardHeader(children=[html.H2("TA Averages")], className="text-center"),
        dbc.Row(
            [
                dbc.Col(average_TA_offer, style=SUMMARY_STYLE),
                dbc.Col(average_TA_hire, style=SUMMARY_STYLE),
            ],
            className="text-center",
        ),
    ],
    style=SUMMARY_STYLE,
)

more_details_summary_unit = dbc.Card(
    [
        dbc.CardHeader(children=[html.H2(" Unit Averages")], className="text-center"),
        dbc.Row(
            [
                dbc.Col(average_unit_offer, style=SUMMARY_STYLE),
                dbc.Col(average_unit_hire, style=SUMMARY_STYLE)
            ],
            className="text-center",
        ),
    ],
    style=SUMMARY_STYLE,
)


summary_group = html.Div([
    dbc.Row([
        dbc.Col(more_details_summary_TA),
        dbc.Col(more_details_summary_unit)
    ])
])

hires_grouping = html.Div([
    dbc.Row([
        dbc.Col(graphs["hires_month_TA_graph"]),
        dbc.Col(graphs["hires_TA_graph"])
        ]),
    dbc.Row([
        dbc.Col(graphs["hires_month_unit_graph"]),
        dbc.Col(graphs["hires_unit_graph"])
    ]),
])

homepage_summary = dbc.Card(
    [
        dbc.CardHeader(children=[html.H2("Summary from YTD")], className="text-center"),
        dbc.Row(
            [
                dbc.Col(total_rejected_content, style=SUMMARY_STYLE),
                dbc.Col(total_offered_content, style=SUMMARY_STYLE),
                dbc.Col(total_hired_content, style=SUMMARY_STYLE)
            ],
            className="text-center",
        ),
        dbc.CardLink("More details", href="/more_detail")
    ],
    style=SUMMARY_STYLE,
)

new_starters_current_month = dbc.Card(
    [
        dbc.CardHeader("New starters this month", className="text-center"),
        dbc.CardBody(html.H3("0"), className="text-center")
    ],
    style=CARD_STYLE
)

active_roles = dbc.Card(
    [
        dbc.CardHeader("Active Roles", className="text-center"),
        dbc.CardBody(html.H3("0"), className="text-center")
    ],
    style=CARD_STYLE
)
 
dashboard_card_grouping = html.Div([
    dbc.Row([
        dbc.Col(graphs["cv_sources_graph"]),
        dbc.Col([
            dbc.Row(dbc.Col(active_roles)),
            dbc.Row(dbc.Col(new_starters_current_month))
            ]),
    ],
    className=""),
    dbc.Row([
        dbc.Col(graphs["roles_per_TA"]),
        dbc.Col(graphs["roles_per_unit"])
    ]),
])

more_detail_layout =html.Div(children=[
    html.Hr(),
    summary_group,
    hires_grouping
])

homepage_content = html.Div(children=[
    homepage_summary,
    dashboard_card_grouping,
    ],
    id="homepage-content",
)

custom_report_sidebar = html.Div(
    [
        html.P("Select from:"),
        dcc.Dropdown(custom_report_options[:-1]),
        html.Hr(),
        html.P("Select to:"),
        dcc.Dropdown(custom_report_options[1:]),
        html.Hr(),
        html.P("Filter by:"),
        dcc.Dropdown(["TA", "TA team", "HM", "Unit"],
            id="filter-report",
            value="TA"
        ),
        html.Hr(),
        html.P("Choose:"),
        dcc.Dropdown(options=[], multi=True, id='choose-report'),
        html.Hr(),
        dbc.Button("Generate Report")
    ],
    style=SIDEBAR_STYLE
)

averages_custom_report = html.Div(
    [
        dbc.Row([
            dbc.Col(dbc.Card(
                [   
                    dbc.CardHeader("Average YTD"),
                    dbc.CardBody("0")
                ],
                style=CARD_STYLE
            )),
            dbc.Col(dbc.Card(
                [
                    dbc.CardHeader("Average Current Month"),
                    dbc.CardBody("0")
                ],
                style=CARD_STYLE
            ))
    ]),
    ]
)

download_button = dbc.Button("Download Report", id="download")

single = [
        dbc.Row(
            [
                dbc.Col(dbc.Card([graphs["average_per_month"], 
                                  generate_download_button(id="single-average-per-month")],
                                  style=CARD_STYLE)),
                dbc.Col(dbc.Card([graphs["applications_YTD"], 
                                  generate_download_button(id="applications-YTD"),
                                  ]),
                                  style=CARD_STYLE),              
            ]),
        dbc.Row(
            [
                dbc.Col(dbc.Card([dcc.Dropdown(placeholder="Open Since", options=["Jan", "Feb", "March"]),
                                 graphs["vacancy_split"],
                                  generate_download_button(id="vacancy-split")],
                                  style=CARD_STYLE)),
                dbc.Col(dbc.Card([
                    graphs["current_month"],
                    generate_download_button(id="current-month")]),
                    style=CARD_STYLE),
            ]
        )
        ]

all = [
        dbc.Row(
            [
                dbc.Col(graphs["average_per_month_multiple"]),
                dbc.Col(graphs["applications_multiple_YTD"]),
            ]),
        dbc.Row(
            [
                # dbc.Col(graphs["average_per_vacancy_multiple"]),
                dbc.Col(dbc.Card([
                    dcc.Dropdown(placeholder="Open Since", options=["Jan 2023", "March 2023", "March"]),
                        graphs["multiple_per_month_per_vacancy"]],
                        style=CARD_STYLE)
                ),

                dbc.Col(dbc.Card([graphs["current_month_multiple"]],
                                 style=CARD_STYLE)
                )
            ]
        )
        ]
custom_report_graphs = html.Div(
    children=[],
    id="custom-report-graphs"
)

custom_report_content = html.Div(
    [
        averages_custom_report,
        custom_report_graphs
    ],
    style=CONTENT_STYLE
)

custom_reports_layout = html.Div(children=
        [
            custom_report_sidebar,
            custom_report_content
        ],
        id="report-page-content"                
    )

content = html.Div(id="page-content", children=[])

app.layout = html.Div(children=[dcc.Location(id="url"), generate_navbar("Main Dashboard"), content])

##########################CALLBACKS#################################
@app.callback(
        Output("nav-title", component_property="brand"),
        [Input("url", "pathname")]
)
def update_navbar(pathname):
    if pathname == "/":
        return "Main Dashboard"
    elif pathname == "/more_detail":
        return "More Details"
    elif pathname == "/generate":
        return "Custom Reports"

@app.callback(
    Output("page-content", component_property="children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return homepage_content
    elif pathname=="/start_dates":
        return html.P("Start dates spreadsheet (Requirement 16)")
    elif pathname== "/gannt":
        return html.P("Gannt chart (Requirement 14)")
    elif pathname == "/generate":
        return custom_reports_layout
    elif pathname == "/more_detail":
        return more_detail_layout
       
@app.callback(
    Output("sidebar", "is_open"),
    Input("open-sidebar", "n_clicks"),
    [State("sidebar", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open

@app.callback(
    Output("choose-report", "options"),
    [Input("filter-report", "value")]
)
def generate_list(filter_option):
    if filter_option == "Select":
        return
    if filter_option == "TA":
        return ["All", "Becky", "John", "Joe", "Harry"]
    if filter_option == "TA team":
        return ["All", "Mine"]
    if filter_option == "Unit":
        return ["All", "Unit1", "Unit2", "Unit3", "Unit4"]
    if filter_option == "HM":
        return ["All", "Keith", "Ronald"]
    
@app.callback(
    Output("custom-report-graphs", "children"),
    [Input("choose-report", "value")]
)    
def generate_graphs(filter_option):
    if filter_option == ["All"]:
        return all
    else:
        return single
    
@app.callback(
    Output("download-report", "data"),
    [Input("single-average-per-month", "n_clicks")]
)
def download_report(n):
    if n:
        return dataframe_to_csv(dataframes["average_per_month"], filename="downloaded_data.xlsx")

if __name__ == '__main__':
    app.run(debug=True)
