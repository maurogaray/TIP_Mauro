import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import requests
import json
from dash.dependencies import Input, Output
from flask_login import login_required

#GET KPI1
KPI1 = "https://HWKY9DC1AQ0HOOB-DB202101281644.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi1/incvol/"
r = requests.get(KPI1)
KPI1JSON = r.json()["items"]



k1_months = []
k1_incidences_numbers = []
k1_priorities = []

for dict in KPI1JSON:
    k1_months.append(dict["month"])
    k1_incidences_numbers.append(dict["incidences_code"])
    k1_priorities.append(dict["priority"])

k1_df = pd.DataFrame({
    "Months": k1_months,
    "Number of incidents": k1_incidences_numbers,
    "Priority": k1_priorities
})

def create_kpi1(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi1", url_base_pathname='/kpi1/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi1-graph',
            figure= px.bar(k1_df, x="Months", y="Number of incidents", color="Priority", barmode="group")
        )  
        
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(dash_app.server.view_functions[view_function])

    return dash_app


#KPI3
KPI3 = "https://HWKY9DC1AQ0HOOB-DB202101281644.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi3/sla/"
r3 = requests.get(KPI3)
KPI3JSON = r3.json()["items"]

#KPI3
kpi3_months = []
kpi3_brbaja=[]
kpi3_brmedia=[]
kpi3_bralta=[]
kpi3_brcritica=[]
kpi3_mtbaja=[]
kpi3_mtmedia=[]
kpi3_mtalta=[]
kpi3_mtcritica=[]

for dict in KPI3JSON:
    kpi3_months.append(dict["month"])
    kpi3_brbaja.append(dict["brbaja"])
    kpi3_brmedia.append(dict["brmedia"])
    kpi3_bralta.append(dict["bralta"])
    kpi3_brcritica.append(dict["brcritica"])
    kpi3_mtbaja.append(dict["mtbaja"])
    kpi3_mtmedia.append(dict["mtmedia"])
    kpi3_mtalta.append(dict["mtalta"])
    kpi3_mtcritica.append(dict["mtcritica"])

kpi3_df = pd.DataFrame({
    "Months": kpi3_months,
    "Breach fuera del SLA, cat = Baja ": kpi3_brbaja,
    "Breach fuera del SLA, cat = Media": kpi3_brmedia,
    "Breach fuera del SLA, cat = Alta": kpi3_bralta,
    "Breach fuera del SLA, cat = Crítico":kpi3_brcritica,
    "Dentro del SLA, cat = Baja": kpi3_mtbaja,
    "Dentro del SLA, cat = Media": kpi3_mtmedia,
    "Dentro del SLA, cat = Alta": kpi3_mtalta,
    "Dentro del SLA, cat = Crítico":kpi3_mtcritica,
})

def create_kpi3(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi3", url_base_pathname='/kpi3/')
    
    dash_app.layout = html.Div(children=[
        # BAJA
        html.Div([
            html.Div(children='''
                Nivel Bajo 
            '''),

            dcc.Graph(                              #Breach dentro de del SLA, cat = Baja 
            id='kpi3-graph1',
            figure= px.bar(kpi3_df, x="Months", y=["Breach fuera del SLA, cat = Baja ", "Dentro del SLA, cat = Baja"], barmode="group")
            )  
        ]),
        # MEDIA
        html.Div([
            html.Div(children='''
                Nivel Medio
            '''),

            dcc.Graph(
            id='kpi3-graph2',                       #Breach fuera del SLA, cat = Media  
            figure= px.bar(kpi3_df, x="Months", y=["Breach fuera del SLA, cat = Media", "Dentro del SLA, cat = Media"], barmode="group")
            )
        ]),
        # Nivel ALTO
        html.Div([
            html.Div(children='''
                Nivel Alto
            '''),

            dcc.Graph(
            id='kpi3-graph3',                       #Breach fuera del SLA, cat = Alta 
            figure= px.bar(kpi3_df, x="Months", y=["Breach fuera del SLA, cat = Alta", "Dentro del SLA, cat = Alta"], barmode="group")
            ) 
        ]),
        # Nivel CRITICO
        html.Div([
            html.Div(children='''
                Nivel Crítico
            '''),

            dcc.Graph(
            id='kpi3-graph4',
            figure= px.bar(kpi3_df, x="Months", y=["Breach fuera del SLA, cat = Crítico", "Dentro del SLA, cat = Crítico"], barmode="group")
            ) 
        ])
    ])

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(dash_app.server.view_functions[view_function])

    return dash_app

#KPI4
KPI4 = "https://HWKY9DC1AQ0HOOB-DB202101281644.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi4/BL/"
r4 = requests.get(KPI4)
KPI4JSON = r4.json()["items"]


k4_months = []
k4_incident_code = []

for dict in KPI4JSON:
    k4_months.append(dict["month"])
    k4_incident_code.append(dict["incident_code"])


k4_df = pd.DataFrame({
    "Months": k4_months,
    "Number of incidents": k4_incident_code,
})

def create_kpi4(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi4", url_base_pathname='/kpi4/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi4-graph',
            figure= px.bar(k4_df, x="Months", y="Number of incidents", barmode="group")
        )       
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(dash_app.server.view_functions[view_function])

    return dash_app

#KPI5
KPI5 = "https://HWKY9DC1AQ0HOOB-DB202101281644.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi5/av/"
r5 = requests.get(KPI5)
KPI5JSON = r5.json()["items"]

#SIMPLE VERSION 

k5_month = []
k5_unavailability_time = []
k5_availability_percentage = []
k5_service_name = []

for dict in KPI5JSON:
    k5_month.append(dict["month"])
    k5_unavailability_time.append(dict["unavailability_time"])
    k5_availability_percentage.append(dict["availability_percentage"])
    k5_service_name.append(dict["service_name"])

k5_df = pd.DataFrame({
    "Months": k5_month,
    "Number of Unavailability": k5_unavailability_time,
    "Percentage of Availability": k5_availability_percentage,
    "Service": k5_service_name,
})

def create_kpi5(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi5", url_base_pathname='/kpi5/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi5-graph',
            figure= px.bar(k5_df, x="Months", y="Number of Unavailability", color="Service", hover_name="Percentage of Availability", barmode="group")
        )  
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(dash_app.server.view_functions[view_function])

    return dash_app

#KPI6
KPI6 = "https://HWKY9DC1AQ0HOOB-DB202101281644.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi6/monav/"
r6 = requests.get(KPI6)
KPI6JSON = r6.json()["items"]

k6_month = []
k6_monthly_av = []
 
for dict in KPI6JSON:
    k6_month.append(dict["month"])
    k6_monthly_av.append(dict["monthly_av"])
    
k6_df = pd.DataFrame({
    "Months": k6_month,
    "Average": k6_monthly_av
    })
        
def create_kpi6(flask_app):
      dash_app = dash.Dash(server=flask_app, name="kpi6", url_base_pathname='/kpi6/')
      
      dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi6-graph',
            figure= px.bar(k6_df, x="Months", y="Average", barmode="group")
        )  
    )

      for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(dash_app.server.view_functions[view_function])

      return dash_app