import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

dcc_graph_config={'responsive':True,
                  'displaylogo':False}


#dummy hires per month per TA from YTD
cv_sources_df = pd.read_csv("pages/cv_sources.csv", encoding='utf-8')
cv_sources_fig = px.pie(cv_sources_df, names='CV Source', 
                    values='CVs', 
                    color='CV Source', 
                    title='CV Source Locations')

roles_per_TA_df = pd.read_csv("pages/roles_per_TA.csv", encoding='utf-8')
roles_per_TA_fig = px.bar(roles_per_TA_df, x="TA", y="Roles", title='Roles per TA', color="TA")
roles_per_TA_fig.update_layout(showlegend=False)

roles_per_unit_df = pd.read_csv("pages/roles_per_unit.csv", encoding='utf-8')
roles_per_unit_fig = px.bar(roles_per_unit_df, x="Unit", y="Roles", title='Roles per Unit', color="Unit")
roles_per_unit_fig.update_layout(showlegend=False)

hires_month_TA_df = pd.read_csv("pages/TA_hires_month.csv", encoding='utf-8')
hires_month_TA_fig = px.line(hires_month_TA_df, 
                                     x='Month', 
                                     y="Hires", 
                                     color="TA",
                                     title="Hires per month per TA")
hires_TA_df = pd.read_csv("pages/TA_hires.csv", encoding='utf-8')
hires_TA_fig = px.bar(hires_TA_df,
                             x="TA",
                             y="Hires",
                             color="TA",
                             title="Hires per TA")
hires_TA_fig.update_layout(showlegend=False)

hires_month_unit_df = pd.read_csv("pages/Unit_hires_month.csv", encoding='utf-8')
hires_month_unit_fig = px.line(hires_month_unit_df,
                             x="Month",
                             y="Hires",
                             color="Unit",
                             title="Hires per month per Unit")
hires_unit_df = pd.read_csv("pages/Unit_hires.csv", encoding='utf-8')
hires_unit_fig = px.bar(hires_unit_df,
                             x="Unit",
                             y="Hires",
                             color="Unit",
                             title="Hires per Unit")
hires_unit_fig.update_layout(showlegend=False)

applications_YTD_df = pd.read_csv("pages/applications_YTD.csv", encoding='utf-8')
applications_YTD_fig = px.bar(applications_YTD_df,
                             x="Days",
                             y="Applications",
                             color="Days",
                             title="Days Taken YTD Single TA")
applications_YTD_fig.update_layout(showlegend=False)

current_month_TA_fig = px.bar(applications_YTD_df,
                             x="Days",
                             y="Applications",
                             color="Days",
                             title="Current Month - December 2023")
current_month_TA_fig.update_layout(showlegend=False)

average_per_month_df = pd.read_csv("pages/average_per_month_TA.csv", encoding='utf-8')
average_per_month_fig = px.line(average_per_month_df,
                             x="Month",
                             y="Average Days",
                             title="Average Days taken per month")
average_per_month_fig.update_layout(showlegend=False)

applications_YTD_multiple_df = pd.read_csv("pages/applications_YTD_multiple.csv", encoding='utf-8')
applications_YTD_multiple_fig = px.bar(applications_YTD_multiple_df,
                             x="Days",
                             y="Applications",
                             color="TA",
                             barmode='group',
                             title="Days Taken YTD Multiple TAs")

current_month_YTD_multiple_fig = px.bar(applications_YTD_multiple_df,
                             x="Days",
                             y="Applications",
                             color="TA",
                             barmode='group',
                             title="Current Month - December 2023")

average_days_per_month_mutiple_df = pd.read_csv("pages/average_days_per_month_multiple.csv", encoding='utf-8')
average_days_per_month_multiple_fig = px.line(average_days_per_month_mutiple_df,
                                     x="Month",
                                     y="Average Days",
                                     color="TA",
                                     title="Average time per Month")

average_days_per_vacancy_multiple_df = pd.read_csv("pages/average_per_vacancy_multiple.csv", encoding='utf-8')
average_days_per_vacancy_multiple_fig = px.bar(average_days_per_vacancy_multiple_df,
                                     x="Vacancy",
                                     y="Average Days",
                                     color="TA",
                                     title="Average time per Vacancy")
vacancies_split_df = pd.read_csv("pages/vacancies_split.csv", encoding='utf-8')
vacancies_split_fig = px.box(vacancies_split_df,
                                     x="Vacancy",
                                     y="Days",
                                     title="Data by Vacancy")

multiple_per_month_per_vacancy_df = pd.read_csv("pages/per_month_per_vacancy_multiple.csv", encoding='utf-8')
multiple_per_month_per_vacancy_fig = px.box(multiple_per_month_per_vacancy_df,
                                     x="Month",
                                     y="Days",
                                     color="Vacancy",
                                     title="Data by Vacancy per Month")

dataframes = {
    "cv_source" : cv_sources_df,
    "roles_per_TA" : roles_per_TA_df,
    "roles_per_unit"         : roles_per_unit_df, 
    "applications_YTD"      : applications_YTD_df,
    "average_per_month"   : average_per_month_df,
    "applications_multiple_YTD"    : applications_YTD_multiple_df,
    "average_per_month_multiple"    : average_days_per_month_mutiple_df,
    "average_per_vacancy_multiple" : average_days_per_vacancy_multiple_df,
    "vacancy_split"   : vacancies_split_df,
    "multiple_per_month_per_vacancy"   : multiple_per_month_per_vacancy_df
}

graphs = {
    "hires_month_TA_graph" : dcc.Graph(id="hires-month-TA", figure=hires_month_TA_fig, config=dcc_graph_config),
    "hires_month_unit_graph" : dcc.Graph(id="hires-month-unit", figure=hires_month_unit_fig, config=dcc_graph_config),
    "hires_TA_graph" : dcc.Graph(id="hires-TA", figure=hires_TA_fig, config=dcc_graph_config),
    "hires_unit_graph" : dcc.Graph(id="hires-unit", figure=hires_unit_fig, config=dcc_graph_config),

    "offers_month_TA_graph" : dcc.Graph(id="offers-month-TA", figure=hires_month_TA_fig, config=dcc_graph_config),
    "offers_month_unit_graph" : dcc.Graph(id="offers-month-unit", figure=hires_month_unit_fig, config=dcc_graph_config),
    "offers_TA_graph" : dcc.Graph(id="offers-TA", figure=hires_TA_fig, config=dcc_graph_config),
    "offers_unit_graph" : dcc.Graph(id="offers-unit", figure=hires_unit_fig, config=dcc_graph_config),

    "cv_sources_graph": dcc.Graph(id="cv-sources", figure=cv_sources_fig, config=dcc_graph_config),
    "roles_per_TA": dcc.Graph(id="roles-per-TA", figure=roles_per_unit_fig, config=dcc_graph_config),
    "roles_per_unit": dcc.Graph(id="roles-per-unit", figure=roles_per_TA_fig, config=dcc_graph_config),

    "applications_YTD": dcc.Graph(id="applications-ytd", figure=applications_YTD_fig, config=dcc_graph_config),
    "applications_multiple_YTD": dcc.Graph(id="applications-ytd-multiple", figure=applications_YTD_multiple_fig, config=dcc_graph_config),
    "average_per_month_multiple": dcc.Graph(id="average-month-multiple", figure=average_days_per_month_multiple_fig, config=dcc_graph_config),
    "average_per_month": dcc.Graph(id="average-month-ta", figure=average_per_month_fig, config=dcc_graph_config),
    "average_per_vacancy_multiple": dcc.Graph(id="average-vacancy-ta", figure=average_days_per_vacancy_multiple_fig, config=dcc_graph_config),
    "vacancy_split": dcc.Graph(id="vacancy-split", figure=vacancies_split_fig, config=dcc_graph_config),
    "multiple_per_month_per_vacancy": dcc.Graph(id="", figure=multiple_per_month_per_vacancy_fig, config=dcc_graph_config),

    "current_month" : dcc.Graph(id="", figure=current_month_TA_fig, config=dcc_graph_config),
    "current_month_multiple" : dcc.Graph(id="", figure=current_month_YTD_multiple_fig, config=dcc_graph_config),
}

custom_report_options = [
    "CV sent",
    "1st IV booked",
    "2nd IV booked",
    "3rd IV booked",
    "1st IV completed",
    "2nd IV completed",
    "3rd IV completed",
    "Feedback on CV",
    "Verbal offer/Rejected",
    "Join date given"
]

def dataframe_to_csv(df:pd.DataFrame, filename):
    return df.to_excel("downloaded_data/" + filename)

def generate_download_button(id):
    return html.Div([dbc.Button("Download Report", id=id), dcc.Download(id="download-report")])


