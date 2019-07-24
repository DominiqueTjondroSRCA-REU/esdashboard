import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

import plotly.plotly as py
import base64


import numpy as np
from collections import defaultdict
import csv

image_filename = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-10 at 11.07.38 AM.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#Scenario 1
scenario_one_energy1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 10.34.05 AM.png' # replace with your own image
encoded_image_one = base64.b64encode(open(scenario_one_energy1, 'rb').read())

scenario_one_energy2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 10.33.32 AM.png' # replace with your own image
encoded_image_two = base64.b64encode(open(scenario_one_energy2, 'rb').read())

scenario_one_consumption1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.25.12 AM.png' # replace with your own image
encoded_image_three = base64.b64encode(open(scenario_one_consumption1, 'rb').read())

scenario_one_consumption2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.25.40 AM.png' # replace with your own image
encoded_image_four = base64.b64encode(open(scenario_one_consumption2, 'rb').read())

scenario_one_withdrawal1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.37.28 AM.png' # replace with your own image
encoded_image_five = base64.b64encode(open(scenario_one_withdrawal1, 'rb').read())

scenario_one_withdrawal2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.37.44 AM.png' # replace with your own image
encoded_image_six = base64.b64encode(open(scenario_one_withdrawal2, 'rb').read())

#Scenario 2
sscenario_one_energy1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.53.08 AM.png' # replace with your own image
eencoded_image_one = base64.b64encode(open(sscenario_one_energy1, 'rb').read())

sscenario_one_energy2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.53.23 AM.png' # replace with your own image
eencoded_image_two = base64.b64encode(open(sscenario_one_energy2, 'rb').read())

sscenario_one_consumption1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.56.33 AM.png' # replace with your own image
eencoded_image_three = base64.b64encode(open(sscenario_one_consumption1, 'rb').read())

sscenario_one_consumption2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.56.47 AM.png' # replace with your own image
eencoded_image_four = base64.b64encode(open(sscenario_one_consumption2, 'rb').read())

sscenario_one_withdrawal1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.57.12 AM.png' # replace with your own image
eencoded_image_five = base64.b64encode(open(sscenario_one_withdrawal1, 'rb').read())

sscenario_one_withdrawal2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 11.57.29 AM.png' # replace with your own image
eencoded_image_six = base64.b64encode(open(sscenario_one_withdrawal2, 'rb').read())

sscenario_one_transmission1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 12.17.08 PM.png' # replace with your own image
eencoded_image_seven = base64.b64encode(open(sscenario_one_transmission1, 'rb').read())

sscenario_one_transmission2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 12.18.32 PM.png' # replace with your own image
eencoded_image_eight = base64.b64encode(open(sscenario_one_transmission2, 'rb').read())

#Scenario 3
ssscenario_one_energy1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 12.33.37 PM.png' # replace with your own image
eeencoded_image_one = base64.b64encode(open(ssscenario_one_energy1, 'rb').read())

ssscenario_one_energy2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 12.33.53 PM.png' # replace with your own image
eeencoded_image_two = base64.b64encode(open(ssscenario_one_energy2, 'rb').read())

ssscenario_one_consumption1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 12.34.20 PM.png' # replace with your own image
eeencoded_image_three = base64.b64encode(open(ssscenario_one_consumption1, 'rb').read())

ssscenario_one_consumption2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 12.35.03 PM.png' # replace with your own image
eeencoded_image_four = base64.b64encode(open(ssscenario_one_consumption2, 'rb').read())

ssscenario_one_withdrawal1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 12.36.43 PM.png' # replace with your own image
eeencoded_image_five = base64.b64encode(open(ssscenario_one_withdrawal1, 'rb').read())

ssscenario_one_withdrawal2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-11 at 12.37.02 PM.png' # replace with your own image
eeencoded_image_six = base64.b64encode(open(ssscenario_one_withdrawal2, 'rb').read())

#FEWSION images
fewsion1 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-18 at 1.34.37 PM.png' # replace with your own image
encodedfewsion1 = base64.b64encode(open(fewsion1, 'rb').read())

fewsion2 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-18 at 1.35.14 PM.png' # replace with your own image
encodedfewsion2 = base64.b64encode(open(fewsion2, 'rb').read())

fewsion3 = '/Users/dominiquetjondro/PycharmProjects/Dashboard/resources/Screen Shot 2019-07-18 at 1.35.58 PM.png' # replace with your own image
encodedfewsion3 = base64.b64encode(open(fewsion3, 'rb').read())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
server = app.server

tdf = pd.read_csv(
    'file://localhost/Users/dominiquetjondro/Downloads/technologies.csv')
technologies = tdf['acronym'].unique()

df2 = pd.read_csv(
    'file://localhost/Users/dominiquetjondro/Downloads/Workbook1.12.csv')

df = pd.read_csv(
    'file://localhost/Users/dominiquetjondro/Downloads/balancingareas.csv')
balancingareas = df['Balancing Areas'].unique()


df1 = pd.read_csv(
    'file://localhost/Users/dominiquetjondro/Downloads/basicscatter.csv')

dfwaterwithdrawl = pd.read_csv(
    'file://localhost/Users/dominiquetjondro/Downloads/waterwithdrawl.csv')

dfwaterconsumption = pd.read_csv(
    'file://localhost/Users/dominiquetjondro/Downloads/waterconsumption.csv')

Renewable_Energy_Technology = pd.read_csv(
    'file://localhost/Users/dominiquetjondro/Downloads/ret1.csv')

sourcesink = pd.read_csv('file://localhost/Users/dominiquetjondro/Downloads/timeslice.csv')

powertechnologies = Renewable_Energy_Technology['powertype'].unique()

ddf = df1[df1['balancingarea']=='p1']
ddf1 = Renewable_Energy_Technology[Renewable_Energy_Technology['BA']=='p1']

ssddf1 = sourcesink[sourcesink['sourceBA']=='p1']

available_indicators = df1['powertype'].unique()
# technology_type = ('Wind', 'Hydro', 'Geothermal')



# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501

#data for Global Warming impact Tab
dataframe26 = pd.read_csv('/Users/dominiquetjondro/Downloads/average2.6.csv')

year_values = {}
year_count = {}

for i, row in dataframe26.iterrows():
   year_values[row['year']] = 0
   year_count[row['year']] = 0

for i, row in dataframe26.iterrows():
    year_values[row['year']] += row['value']
    year_count[row['year']] += 1

averages = {}

for year, value in year_values.items():
    averages[year] = (value / year_count[year])

x_values = []
y_values = []

for year, average in averages.items():
   x_values.append(year)
   y_values.append(average)

bar1 = go.Bar(
	x= x_values,
	y= y_values,
	name= 'RCP 2.6',
	marker=dict(
		color='rgb(201,219, 243)'
		)
	)

dataframe45 = pd.read_csv('/Users/dominiquetjondro/Downloads/average4.5.csv')

year_values = {}
year_count = {}

for i, row in dataframe45.iterrows():
  year_values[row['year']] = 0
  year_count[row['year']] = 0

for i, row in dataframe45.iterrows():
  year_values[row['year']] += row['value']
  year_count[row['year']] += 1

averages = {}

for year, value in year_values.items():
  averages[year] = (value / year_count[year])

x_values = []
y_values = []

for year, average in averages.items():
  x_values.append(year)
  y_values.append(average)

bar2 = go.Bar(
  x=x_values,
  y=y_values,
  name='RCP 4.5',
  marker=dict(
    color='rgb(157, 202, 225)'
  )
)

dataframe60 = pd.read_csv('/Users/dominiquetjondro/Downloads/average6.0.csv')

year_values = {}
year_count = {}

for i, row in dataframe60.iterrows():
  year_values[row['year']] = 0
  year_count[row['year']] = 0

for i, row in dataframe60.iterrows():
  year_values[row['year']] += row['value']
  year_count[row['year']] += 1

averages = {}

for year, value in year_values.items():
  averages[year] = (value / year_count[year])

x_values = []
y_values = []

for year, average in averages.items():
  x_values.append(year)
  y_values.append(average)

bar3 = go.Bar(
  x=x_values,
  y=y_values,
  name='RCP 6.0',
  marker=dict(
    color='rgb(106, 173, 215)'
  )
)

dataframe85 = pd.read_csv('/Users/dominiquetjondro/Downloads/average8.5.csv')

year_values = {}
year_count = {}

for i, row in dataframe85.iterrows():
  year_values[row['year']] = 0
  year_count[row['year']] = 0

for i, row in dataframe85.iterrows():
  year_values[row['year']] += row['value']
  year_count[row['year']] += 1

averages = {}

for year, value in year_values.items():
  averages[year] = (value / year_count[year])

x_values = []
y_values = []

for year, average in averages.items():
  x_values.append(year)
  y_values.append(average)

bar4 = go.Bar(
  x=x_values,
  y=y_values,
  name='RCP 8.5',
  marker=dict(
    color='rgb(49, 129, 188)'
  )
)


data = [bar1, bar2, bar3, bar4]
layout = go.Layout(
    xaxis= {
        'title': 'Years',
    },
    yaxis= {
        'title' : 'Energy Generated ( MWh )'
    },
    barmode='group',
    title='Average Projected Energy Generation by RCP',
)




app.layout = html.Div( style= {'max-width': '100%', 'overflow-x': 'hidden'},
    children= [    html.Div(style= {'margin-top': 10,
                     'font-family': 'Nunito'},
        children=[
        html.Link(href='https://fonts.googleapis.com/css?family=Nunito&display=swap', rel='stylesheet'),

        html.Link(href='https://fonts.googleapis.com/css?family=Nunito:700&display=swap', rel='stylesheet'),
        html.Div(
            [
                html.H1(children='ENERGY SYSTEMS',
                        className='nine columns',
                        style= { 'margin-top': 10,
                                 'font-family': 'Nunito',
                                 'font-weight': 'bold',
                                 'letter-spacing': 1}
                        ),
                html.Img(
                    src="https://brand.ncsu.edu/assets/logos/ncstate-brick-4x1-red-max.png",
                    className='three columns',
                    style={
                        'height': '25%',
                        'width': '25%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 20,
                    },
                ),
                html.P(children='An Introduction to the ReEDS Model displaying National Energy Systems',
                        className='nine columns',
                        style= {'font-family': 'Nunito',
                                'margin-top': -10}
                )
            ], className="row"
        ),

    dcc.Tabs(id="tabs", children=[

                dcc.Tab(label='Introduction', children=[

                    html.Div([

                        html.Div(
                            style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40,
                                   'margin-left': 180,
                                   'margin-right': 180, 'padding-top': 4}, children=
                            [
                                html.Div([
                                    html.H1(children="Introduction",
                                            style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                                ]),

                                html.H2(children=html.Em(
                                    children='Data referencing the Regional Energy Deployment System (ReEDS) model shows power generation, energy generation, water consumption, and water withdrawal amongst the various balancing areas in the United States. The model is meant to illustrate changes within consumption and generation patterns in regards to climate change and power technologies'),
                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                           'letter-spacing': .2},
                                    className='twelve columns'
                                )
                            ], className="row"
                        ),
                    ]),

                    html.Div(
                        [
                            html.H2(children=html.Em(
                                children='The text and image below displays important terms and abbreviations related to energy systems and its functions. To better understand energy systems in this context, take note of what is noted below'),
                                style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 30,
                                       'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                className='twelve columns'
                            )
                        ], className="row"
                    ),

                        html.Div(
                            [
                                html.Div([
                                    html.Div(children=['The ',
                                                       html.Strong(children=html.U(
                                                           children='Regional Energy Deployment System (ReEDS)')),
                                                       ' model is a capacity expansion and dispatch model for the contiguous U.S. electric power sector that relies on system-wide least cost optimization to estimate the type and location of future generation and transmission capacity.'],
                                             # className='eleven columns',
                                             style={'margin-top': 12.5,
                                                    'margin-right': 20
                                                    }
                                             ),

                                        html.A(children=
                                               [html.Img(
                                                   src='https://www.nrel.gov/analysis/reeds/assets/images/screen-reeds.jpg',
                                                   style={
                                                       'height': '100%',
                                                       'width': '90%',
                                                       # 'position': 'relative',
                                                       'margin-top': 20,
                                                       'margin-right': 20
                                                   },
                                                   )],
                                               href='https://openei.org/apps/reeds/',
                                               target='_blank'),

                                ], className='six columns'
                                ),

                                html.Div([
                                    html.Div(children=[
                                        html.H3(children=html.Strong(children='IMPORTANT TERMS:'), style={'font-size': 20}),
                                        html.P(children=[html.Strong(children=html.U(children='Cascadia Subduction Zone:')),
                                                         ' a continental plate boundary off the west coast of Washington State that is capable of generating huge earthquakes.']),
                                        html.P(children=[html.Strong(children=html.U(children='Drought:')),
                                                         ' An extended period of time where less water falls as rain or snow, causing significant shortfalls in water supplies that are needed by cities and farmers.']),
                                        html.P(children=[html.Strong(children=html.U(children='Footprint:')),
                                                         ' The size of your supply chain’s effects on the Earth and its natural resources.']),
                                        html.P(children=[html.Strong(children=html.U(children='Supply Chain:')),
                                                         ' The sources and means of delivery of your goods and services, including the raw materials and water used, manufacture, transportation, storage, and distribution.']),
                                        html.H3(children=html.Strong(children='IMPORTANT ABBREVIATIONS:'),
                                                style={'font-size': 20}),
                                        html.P(children=[html.Strong(children=html.U(children='BA:')),
                                                         ' Balancing Area (electricity supply and demand within geographic boundaries)']),
                                        html.P(children=[html.Strong(children=html.U(children='RCP:')),
                                                         ' Representative Concentration Pathway (greenhouse gas concentration trajectory)']),
                                        html.P(children=[html.Strong(children=html.U(children='CC:')),
                                                         ' Combined Cycle Turbine']),

                                    ], style={'margin-left': 20}),
                                    html.Div(style={'height': 30}),

                                ], className='six columns'
                                ),

                                html.H2(
                                    style={'margin-top': 20,
                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180},
                                    className='twelve columns'
                                )

                            ], className="row"
                        )
                    ]),

                dcc.Tab(label='Global Warming Impact', children=[
                                        html.Div(
                                            style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40, 'margin-left': 180,
                                                   'margin-right': 180, 'padding-top': 4}, children=
                                            [
                                                html.Div([
                                                    html.H1(children="Global Warming Impact",
                                                            style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                                                ]),

                                                html.H2(children=html.Em(
                                                    children='The RCP is a greenhouse gas concentration trajectory that indicates the severity of climate change, where 2.6 is the optimal condition and 8.5 is the worse case scenario'),
                                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                                           'letter-spacing': .2},
                                                    className='twelve columns'
                                                )
                                            ], className="row"
                                        ),

                                        html.Div(
                                            [
                                                html.H2(children=html.Em(
                                                    children='This is a bar graph that displays the change in average energy generation patterns across various climate change indexes, known as the RCP'),
                                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 30,
                                                           'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                                    className='twelve columns'
                                                )
                                            ], className="row"
                                        ),

                                            html.Div(
                                                [
                                                html.Div([
                                                    dcc.Graph(
                                                        figure=go.Figure(data=data, layout=layout)




                                                    )
                                                    ], className= 'twelve columns'
                                                    ),

                                                ], className="row"
                                            ),

                                        ]),

                dcc.Tab(label='Power Technologies', children=[
                                html.Div(
                                    style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40, 'margin-left': 180,
                                           'margin-right': 180, 'padding-top': 4}, children=
                                    [
                                        html.Div([
                                            html.H1(children="Power Technologies",
                                                    style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                                        ]),

                                        html.H2(children=html.Em(
                                            children='Power technologies relate to an interdisciplinary engineering science that deals with the extraction, conversion, transportation, storage and use of energy. Different power technologies convert energy into a useable form in varying processes'),
                                            style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                                   'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                                   'letter-spacing': .2},
                                            className='twelve columns'
                                        )
                                    ], className="row"
                                ),


                                html.Div(
                                    [
                                        html.H2(children=html.Em(
                                            children='This is a scatter plot that displays the relationships between a balancing area and its energy generation according to specific power technologies at varying climate change indexes throughout the years'),
                                            style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 30,
                                                   'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                            className='twelve columns'
                                        )
                                    ], className="row"
                                ),


                                    html.Div([
                                        html.Div([

                                            dcc.Dropdown(
                                                id='my-dropdown1',
                                                options=[{'label': i, 'value': i} for i in balancingareas],
                                                value='p1'
                                            ),

                                            html.Div(id='output-container1'),

                                            dcc.Dropdown(
                                                id='powertechnologydropdown',
                                                options=[{'label': i, 'value': i} for i in powertechnologies],
                                                value='hydroelectric'
                                            ),

                                            html.Div(id='output-container-power'),

                                        ], className="eight columns"
                                        ),

                                        html.Div([
                                            dcc.Dropdown(
                                                id='acronym',
                                                options=[{'label': i, 'value': i} for i in technologies],
                                                value='AC'
                                            ),

                                            html.Div(id='outputtechnologies'),

                                            ], className="four columns"
                                        ),

                                            html.Div([
                                                dcc.Graph(
                                                    id='year-vs-value1'
                                                )
                                            ], className='twelve columns'
                                            ),


                                        html.H2(
                                            style={'margin-top': 20,
                                                   'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180},
                                            className='twelve columns'
                                        )

                                    ])

                    ]),

                dcc.Tab(label='Time Slices', children=[
                    html.Div([

                        html.Div(
                            style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40,
                                   'margin-left': 180,
                                   'margin-right': 180, 'padding-top': 4}, children=
                            [
                                html.Div([
                                    html.H1(children="Time Slices",
                                            style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                                ]),

                                html.H2(children=html.Em(
                                    children='A time slice represents a specific interval of time. It takes hours, months, seasons, and the time of day into consideration. H17 is classified as the superpeak. AC flow refers to energy exchanges between various balancing areas'),
                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                           'letter-spacing': .2},
                                    className='twelve columns'
                                )
                            ], className="row"
                        ),
                    ]),

                    html.Div(
                        [
                            html.H2(children=html.Em(
                                children='This is a scatterplot that displays changes in AC flow value in respect to different time slices across various balancing areas. Use both graphs simultaneously to visualize the direction of energy transfers between 2 balancing areas'),
                                style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 30,
                                       'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                className='twelve columns'
                            )
                        ], className="row"
                    ),

                    html.Div([
                        html.Div([

                            html.Label('Source BA'),
                            dcc.Dropdown(
                                id='my-dropdownSOURCE',
                                options=[{'label': i, 'value': i} for i in balancingareas],
                                value='p1'
                            ),
                            html.Div(id='output-containerSOURCE'),

                            html.Label('Sink BA'),
                            dcc.Dropdown(
                                id='my-dropdownSINK',
                                options=[{'label': i, 'value': i} for i in balancingareas],
                                value='p1'
                            ),
                            html.Div(id='output-containerSINK'),

                            dcc.Graph(
                                id='sourcesink'
                            )
                        ], className='six columns')
                    ]),

                    html.Div([
                        html.Div([

                            html.Label('Source BA'),
                            dcc.Dropdown(
                                id='my-dropdownSOURCE1',
                                options=[{'label': i, 'value': i} for i in balancingareas],
                                value='p1'
                            ),
                            html.Div(id='output-containerSOURCE1'),

                            html.Label('Sink BA'),
                            dcc.Dropdown(
                                id='my-dropdownSINK1',
                                options=[{'label': i, 'value': i} for i in balancingareas],
                                value='p1'
                            ),

                            html.Div(id='output-containerSINK1'),

                            dcc.Graph(
                                id='sourcesink1'
                            ),

                            html.H2(
                                style={'margin-top': 20,
                                       'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180},
                                className='twelve columns'
                            )

                        ], className='six columns')
                    ])
                ]),

                dcc.Tab(label='Energy', children=[
                html.Div([

                html.Div(
                    style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40,
                           'margin-left': 180,
                           'margin-right': 180, 'padding-top': 4}, children=
                    [
                        html.Div([
                            html.H1(children="Energy",
                                    style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                        ]),

                        html.H2(children=html.Em(
                            children='Energy generation describes the production of both primary and secondary energy for the purpose of serving the needs of mankind'),
                            style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                   'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                   'letter-spacing': .2},
                            className='twelve columns'
                        )
                    ], className="row"
                ),
            ]),

            html.Div(
                [
                    html.H2(children=html.Em(
                        children='This is a scatter plot that displays energy generation patterns in respect to various power technologies in each balancing area in the United States. This is a representation of energy generation at an RCP of 2.6'),
                        style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 30,
                               'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                        className='twelve columns'
                    )
                ], className="row"
            ),

            html.Div([
                html.Div([

                    dcc.Dropdown(
                        id='my-dropdown',
                        options=[{'label': i, 'value': i} for i in balancingareas],
                        value='p1'
                    ),
                    html.Div(id='output-container'),

                    dcc.Graph(
                        id='year-vs-value',
                        figure={
                            'data': [
                                go.Scatter(
                                    x=ddf[ddf['powertype'] == i]['year'],
                                    y=ddf[ddf['powertype'] == i]['value'],
                                    text=ddf[ddf['powertype'] == i]['powertype'],
                                    mode='markers',
                                    opacity=0.7,
                                    marker={
                                        'size': 15,
                                        'line': {'width': 0.5, 'color': 'white'}
                                    },
                                    name=i
                                ) for i in df1.powertype.unique()
                            ],
                            'layout': go.Layout(
                                xaxis={'type': 'log', 'title': 'Year'},
                                yaxis={'title': 'Energy Generated'},
                                margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                                legend={'x': 0, 'y': 1},
                                hovermode='closest'
                            )
                        }
                    ),

                    html.H2(
                        style={'margin-top': 20,
                               'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180},
                        className='twelve columns'
                    )

                ])
            ])

        ]),

                dcc.Tab(label='Water Withdrawal', children=[
                                        html.Div(
                                            style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40, 'margin-left': 180,
                                                   'margin-right': 180, 'padding-top': 4}, children=
                                            [
                                                html.Div([
                                                    html.H1(children="Water Withdrawal",
                                                            style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                                                ]),

                                                html.H2(children=html.Em(
                                                    children='Water withdrawal describes the total amount of water withdrawn from a surface water or groundwater source'),
                                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                                           'letter-spacing': .2},
                                                    className='twelve columns'
                                                )
                                            ], className="row"
                                        ),


                                        html.Div(
                                            [
                                                html.H2(children=html.Em(
                                                    children='This is a scatter plot that displays water withdrawal patterns in respect to various power technologies in each balancing area in the United States. This is a representation of water withdrawal at an RCP of 2.6'),
                                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 30,
                                                           'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                                    className='twelve columns'
                                                )
                                            ], className="row"
                                        ),

                                        html.Div([
                                            html.Div([

                                            dcc.Dropdown(
                                                id='my-dropdown-waterwithdrawl',
                                                options=[{'label': i, 'value': i} for i in balancingareas],
                                                value='p1'
                                            ),
                                            html.Div(id='output-container-waterwithdrawl'),

                                            dcc.Graph(
                                                    id='waterwithdrawl',
                                                    figure={
                                                        'data': [
                                                            go.Scatter(
                                                                x=ddf[ddf['powertype'] == i]['year'],
                                                                y=ddf[ddf['powertype'] == i]['value'],
                                                                text=ddf[ddf['powertype'] == i]['powertype'],
                                                                mode='markers',
                                                                opacity=0.7,
                                                                marker={
                                                                    'size': 15,
                                                                    'line': {'width': 0.5, 'color': 'white'}
                                                                },
                                                                name=i
                                                            ) for i in dfwaterwithdrawl.powertype.unique()
                                                        ],
                                                        'layout': go.Layout(
                                                            xaxis={'type': 'log', 'title': 'Year'},
                                                            yaxis={'title': 'Energy Generated'},
                                                            margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                                                            legend={'x': 0, 'y': 1},
                                                            hovermode='closest'
                                                        )
                                                    }
                                                ),

                                                html.H2(
                                                    style={'margin-top': 20,
                                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180},
                                                    className='twelve columns'
                                                )


                                            ])
                                        ])

                        ]),

                dcc.Tab(label='Water Consumption', children=[
                                    html.Div(
                                        style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40, 'margin-left': 180,
                                               'margin-right': 180, 'padding-top': 4}, children=
                                        [
                                            html.Div([
                                                html.H1(children="Water Consumption",
                                                        style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                                            ]),

                                            html.H2(children=html.Em(
                                                children='Water consumption describes the portion of the withdrawn water permanently lost from its source'),
                                                style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                                       'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                                       'letter-spacing': .2},
                                                className='twelve columns'
                                            )
                                        ], className="row"
                                    ),


                                    html.Div(
                                        [
                                            html.H2(children=html.Em(
                                                children='This is a scatter plot that displays water consumption patterns in respect to various power technologies in each balancing area in the United States. This is a representation of water consumption at an RCP of 2.6'),
                                                style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 30,
                                                       'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                                className='twelve columns'
                                            )
                                        ], className="row"
                                    ),

                                        html.Div([
                                            html.Div([

                                            dcc.Dropdown(
                                                id='my-dropdown-waterconsumption',
                                                options=[{'label': i, 'value': i} for i in balancingareas],
                                                value='p1'
                                            ),
                                            html.Div(id='output-container-waterconsumption'),

                                            dcc.Graph(
                                                    id='waterconsumption',
                                                    figure={
                                                        'data': [
                                                            go.Scatter(
                                                                x=ddf[ddf['powertype'] == i]['year'],
                                                                y=ddf[ddf['powertype'] == i]['value'],
                                                                text=ddf[ddf['powertype'] == i]['powertype'],
                                                                mode='markers',
                                                                opacity=0.7,
                                                                marker={
                                                                    'size': 15,
                                                                    'line': {'width': 0.5, 'color': 'white'}
                                                                },
                                                                name=i
                                                            ) for i in dfwaterconsumption.powertype.unique()
                                                        ],
                                                        'layout': go.Layout(
                                                            xaxis={'type': 'log', 'title': 'Year'},
                                                            yaxis={'title': 'Energy Generated'},
                                                            margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                                                            legend={'x': 0, 'y': 1},
                                                            hovermode='closest'
                                                        )
                                                    }
                                                ),

                                                html.H2(
                                                    style={'margin-top': 20,
                                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180},
                                                    className='twelve columns'
                                                )


                                            ])
                                        ])

                        ]),

                dcc.Tab(label='Overview', children=[
                                    html.Div([

                                        html.Div(
                                            style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40,
                                                   'margin-left': 180,
                                                   'margin-right': 180, 'padding-top': 4}, children=
                                            [
                                                html.Div([
                                                    html.H1(children="Overview",
                                                            style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                                                ]),

                                                html.H2(children=html.Em(
                                                    children='Power techonologies play a huge role in energy consumption and generation patterns, as conversion rations for each method differ from one another '),
                                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                                           'letter-spacing': .2},
                                                    className='twelve columns'
                                                )
                                            ], className="row"
                                        ),
                                    ]),

                                    html.Div(
                                        [
                                            html.H2(children=html.Em(
                                                children='This is a scatterplot that displays changes in energy generation between two power technologies across a time slider'),
                                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                                           'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                                    className='twelve columns'
                                                    )
                                        ], className="row"
                                    ),

                                            html.Div([
                                                html.Div([

                                                    html.Div([
                                                        dcc.Dropdown(
                                                            id='xaxis-column',
                                                            options=[{'label': i, 'value': i} for i in available_indicators],
                                                            value='hydro'
                                                        ),
                                                    ],
                                                        style={'width': '48%', 'display': 'inline-block'}),

                                                    html.Div([
                                                        dcc.Dropdown(
                                                            id='yaxis-column',
                                                            options=[{'label': i, 'value': i} for i in available_indicators],
                                                            value='gas-CC'
                                                        ),

                                                    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
                                                ]),

                                                dcc.Graph(id='indicator-graphic'),

                                                dcc.Slider(
                                                    id='year--slider',
                                                    min=df2['Year'].min(),
                                                    max=df2['Year'].max(),
                                                    value=df2['Year'].max(),
                                                    marks={str(year): str(year) for year in df2['Year'].unique()},
                                                    step=None
                                                ),



                                            ], className= 'twevlve columns'),

                                            html.H2(
                                                style={'margin-top': 50,
                                                       'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180},
                                                className='twelve columns'
                                            )
                                        ]),

                dcc.Tab(label='Scenarios', children=[

                        html.Div([

                            html.Div(
                                style={'background-color': '#cccccc', 'margin-top': 40, 'margin-bottom': 40,
                                       'margin-left': 180,
                                       'margin-right': 180, 'padding-top': 4, 'padding-bottom': 10}, children=
                                [
                                    html.Div([
                                        html.H1(children="Scenarios",
                                                style={'text-align': 'center', 'margin-top': 20, 'font-size': 24}),
                                    ]),

                                    html.H2(children=html.Em(
                                        children='Scenarios were inspired by FEW-View™ and better curated to correlated with the ReEDS Model Scenario Application'),
                                        style={'text-align': 'center', 'font-size': 16, 'margin-top': -10,
                                               'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180,
                                               'letter-spacing': .2},
                                        className='twelve columns'
                                    ),

                                    html.Div([
                                        html.P(children='Explore more on your own using the following links:',
                                               style = {'text-align': 'center'})
                                        ]),

                                    html.Div([
                                        html.A(children='FEW-View™',
                                               href='https://fewsion.dtn.asu.edu/',
                                               style={'margin-left': 350, 'margin-bottom': 20},
                                               target='_blank')
                                    ]),
                                    html.Div([
                                        html.A(children='ReEDS Model Scenario Application',
                                               href='https://ncsu.maps.arcgis.com/apps/webappviewer/index.html?id=5347aabd36be4d978d616ff4f94edf39',
                                               style={'margin-left': 280, 'margin-bottom': 50},
                                               target='_blank')
                                    ]),


                                    html.Div([
                                        html.P(children='',
                                               style = {'text-align': 'center'}),
                                    ]),

                                ], className="row"
                            ),
                        ]),





                        html.Div(
                            [
                                html.H2(children=html.U(
                                    children='Scenarios have been inspired by the storylines mapped from FEWSION, a website that maps the U.S food, energy, and water system'),
                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 60,
                                           'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                    className='twelve columns'
                                )
                            ], className="row"
                        ),


                        html.Div(
                            [
                                html.H2(children=html.Em(
                                    children='FEWSION™ has built the first complete empirical description of the U.S. food, energy, and water system (the FEW Nexus) so that every citizen and policymaker in the U.S. can see where their food, energy, and water come from'),
                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 60,
                                           'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                    className='twelve columns'
                                )
                            ], className="row"
                        ),

                        html.Div(
                            [
                                html.H2(children=html.Em(
                                    children='FEW-View™ is the online educational tool that helps U.S. residents and community leaders visualize their supply chains, with an emphasis on food, energy, and water'),
                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 20,
                                           'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                    className='twelve columns'
                                )
                            ], className="row"
                        ),

                        html.Div(
                            [
                                html.H2(children=html.Strong(
                                    children='Explore the scenarios below by clicking on the respective image'),
                                    style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 60,
                                           'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                    className='twelve columns'
                                )
                            ], className="row"
                        ),

                            html.Div([

                                html.A(children=
                                       [html.Img(src='data:image/png;base64,{}'.format(encodedfewsion1.decode()),
                                                 style={
                                                     'height': '100%',
                                                     'width': '90%',
                                                     'margin-bottom': 30,
                                                     'margin-top': 20,
                                                     'margin-left': 150
                                                 },
                                                 )],
                                       href='https://fewsion.dtn.asu.edu/app/public?scenario_id=13&hide_info=true',
                                       target='_blank'),

                            ], className='ten columns'
                            ),

                            html.Div([

                                html.A(children=
                                       [html.Img(src='data:image/png;base64,{}'.format(encodedfewsion2.decode()),
                                                 style={
                                                     'height': '100%',
                                                     'width': '90%',
                                                     'margin-bottom': 30,
                                                     'margin-top': 20,
                                                     'margin-left': 150
                                                 },
                                                 )],
                                       href='https://fewsion.dtn.asu.edu/app/public?scenario_id=11&hide_info=true',
                                       target='_blank'),

                            ], className='ten columns'
                            ),

                            html.Div([

                                html.A(children=
                                       [html.Img(src='data:image/png;base64,{}'.format(encodedfewsion3.decode()),
                                                 style={
                                                     'height': '100%',
                                                     'width': '90%',
                                                     'margin-bottom': 40,
                                                     'margin-top': 20,
                                                     'margin-left': 150
                                                 },
                                                 )],
                                       href='https://fewsion.dtn.asu.edu/app/public?scenario_id=12&hide_info=true',
                                       target='_blank'),

                            ], className='ten columns'
                            ),


                            html.Div(
                                [
                                    html.H2(children=html.U(
                                        children='To better visualize energy generation, water withdrawal, and water consumption patterns, use the Visual Representations of the ReEDS Model Scenario Application on ArcGIS'),
                                        style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 40,
                                               'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                        className='twelve columns'
                                    )
                                ], className="row"
                            ),


                            html.Div(
                                [
                                    html.H2(children=html.Em(
                                        children='Below are some examples that can be referenced back to the scenarios provided'),
                                        style={'text-align': 'center', 'font-size': 16, 'margin-top': 20, 'margin-botton': 15,
                                               'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                        className='twelve columns'
                                    )
                                ], className="row"
                            ),

                            html.Div(
                                [
                                    html.H2(children=html.Strong(
                                        children='Explore the ReEDS Model Scenario Application by clicking on the map below'),
                                        style={'text-align': 'center', 'font-size': 16, 'margin-top': -10, 'margin-botton': 60,
                                               'padding-left': 180, 'padding-right': 180, 'letter-spacing': .2},
                                        className='twelve columns'
                                    )
                                ], className="row"
                            ),

                                html.Div([

                                    html.A(children=
                                           [html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                                                     style={
                                                         'height': '100%',
                                                         'width': '90%',
                                                         'margin-bottom': 30,
                                                         'margin-top': 20,
                                                         'margin-left': 150
                                                     },
                                                     )],
                                           href='https://ncsu.maps.arcgis.com/apps/webappviewer/index.html?id=5347aabd36be4d978d616ff4f94edf39',
                                           target='_blank'),

                                ], className='ten columns'
                                ),


                            html.Div(
                                [
                                    html.H2(children=html.Em(
                                        children='SCENARIO 1: How a growing population in New York impacts California’s water resources'),
                                        style={'text-align': 'center', 'font-size': 18, 'margin-top': 20, 'margin-botton': 5, 'letter-spacing': .2},
                                        className='twelve columns'
                                    )
                                ], className="row"
                            ),
                            html.Div(
                              [
                                html.Div([


                                  html.Div([
                                    html.Div(children=[
                                      html.H3(children=html.Strong(children='Before'), style={'font-size': 20}),
                                      html.P(children=[html.Strong(children=html.U(children='Energy Generation:')),
                                                       ' Power Technology - Gas CC / Year - 2010']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_one.decode()),
                                             style={
                                               'height': '100%',
                                               'width': '90%',
                                               # 'position': 'relative',
                                               'margin-top': 5,
                                               'margin-bottom': 10,
                                               'margin-right': 20
                                             }
                                             )
                                  ], className='six columns'
                                  ),

                                  html.Div([
                                    html.Div(children=[
                                      html.H3(children=html.Strong(children='After'), style={'font-size': 20}),
                                      html.P(children=[html.Strong(children=html.U(children='Energy Generation:')),
                                                       ' Power Technology - Gas CC / Year - 2050']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_two.decode()),
                                             style={
                                               'height': '100%',
                                               'width': '90%',
                                               # 'position': 'relative',
                                               'margin-top': 5,
                                               'margin-bottom': 10,
                                               'margin-right': 20
                                             }
                                             )
                                  ], className='six columns'
                                  )
                                ], className="row"
                                ),

                                html.Div([
                                  html.Div([
                                    html.Div(children=[
                                      html.P(children=[html.Strong(children=html.U(children='Water Consumption:')),
                                                       ' Power Technology - Geothermal / Year - 2010']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_three.decode()),
                                             style={
                                               'height': '100%',
                                               'width': '90%',
                                               # 'position': 'relative',
                                               'margin-top': 5,
                                               'margin-bottom': 10,
                                               'margin-right': 20
                                             }
                                             )
                                  ], className='six columns'
                                  ),

                                  html.Div([
                                    html.Div(children=[
                                      html.P(children=[html.Strong(children=html.U(children='Water Consumption:')),
                                                       ' Power Technology - Geothermal / Year - 2050']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_four.decode()),
                                             style={
                                               'height': '100%',
                                               'width': '90%',
                                               # 'position': 'relative',
                                               'margin-top': 5,
                                               'margin-bottom': 10,
                                               'margin-right': 20
                                             }
                                             )
                                  ], className='six columns'
                                  )
                                ], className="row"
                                ),



                                html.Div([
                                    html.Div([
                                    html.Div(children=[
                                        html.P(children=[html.Strong(children=html.U(children='Water Withdrawal')),
                                                         ' Power Technology - CSP / Year - 2010']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_five.decode()),
                                             style={
                                                 'height': '100%',
                                                 'width': '90%',
                                                 # 'position': 'relative',
                                                 'margin-top': 5,
                                                 'margin-bottom': 10,
                                                 'margin-right': 20
                                             }
                                             )
                                ], className='six columns'
                                ),

                                html.Div([
                                    html.Div(children=[
                                        html.P(children=[html.Strong(children=html.U(children='Water Withdrawal')),
                                                         ' Power Technology - CSP / Year - 2050']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_six.decode()),
                                             style={
                                                 'height': '100%',
                                                 'width': '90%',
                                                 # 'position': 'relative',
                                                 'margin-top': 5,
                                                 'margin-right': 20
                                             }
                                             )
                                      ], className='six columns'
                                      )
                                  ], className="row"
                                )


                              ]),

                            html.Div(
                                [
                                    html.H2(children=html.Em(
                                        children='SCENARIO 2: How a natural disaster can damage the ports, roads, and other modes of transportation that connect one region from other parts of the world'),
                                        style={'text-align': 'center', 'font-size': 18, 'margin-top': 20, 'margin-botton': 5, 'letter-spacing': .2},
                                        className='twelve columns'
                                    )
                                ], className="row"
                            ),

                              html.Div(
                                  [
                                    html.Div([
                                      html.Div([
                                        html.Div(children=[
                                          html.H3(children=html.Strong(children='Before'), style={'font-size': 20}),
                                          html.P(children=[html.Strong(children=html.U(children='Energy Generation:')),
                                                           ' Power Technology - Hydro / Year - 2010']),
                                        ], style={'margin-left': 20}),

                                        html.Img(src='data:image/png;base64,{}'.format(eencoded_image_one.decode()),
                                                 style={
                                                   'height': '100%',
                                                   'width': '90%',
                                                   # 'position': 'relative',
                                                   'margin-top': 5,
                                                   'margin-bottom': 10,
                                                   'margin-right': 20
                                                 }
                                                 )
                                      ], className='six columns'
                                      ),

                                      html.Div([
                                        html.Div(children=[
                                          html.H3(children=html.Strong(children='After'), style={'font-size': 20}),
                                          html.P(children=[html.Strong(children=html.U(children='Energy Generation:')),
                                                           ' Power Technology - Hydro / Year - 2050']),
                                        ], style={'margin-left': 20}),

                                        html.Img(src='data:image/png;base64,{}'.format(eencoded_image_two.decode()),
                                                 style={
                                                   'height': '100%',
                                                   'width': '90%',
                                                   # 'position': 'relative',
                                                   'margin-top': 5,
                                                   'margin-bottom': 10,
                                                   'margin-right': 20
                                                 }
                                                 )
                                      ], className='six columns'
                                      )
                                    ], className="row"
                                    ),

                                    html.Div([
                                      html.Div([
                                        html.Div(children=[
                                          html.P(children=[html.Strong(children=html.U(children='Water Consumption:')),
                                                           ' Power Technology - Hydro / Year - 2010']),
                                        ], style={'margin-left': 20}),

                                        html.Img(src='data:image/png;base64,{}'.format(eencoded_image_three.decode()),
                                                 style={
                                                   'height': '100%',
                                                   'width': '90%',
                                                   # 'position': 'relative',
                                                   'margin-top': 5,
                                                   'margin-bottom': 10,
                                                   'margin-right': 20
                                                 }
                                                 )
                                      ], className='six columns'
                                      ),

                                      html.Div([
                                        html.Div(children=[
                                          html.P(children=[html.Strong(children=html.U(children='Water Consumption:')),
                                                           ' Power Technology - Hydro / Year - 2050']),
                                        ], style={'margin-left': 20}),

                                        html.Img(src='data:image/png;base64,{}'.format(eencoded_image_four.decode()),
                                                 style={
                                                   'height': '100%',
                                                   'width': '90%',
                                                   # 'position': 'relative',
                                                   'margin-top': 5,
                                                   'margin-bottom': 10,
                                                   'margin-right': 20
                                                 }
                                                 )
                                      ], className='six columns'
                                      )
                                    ], className="row"
                                    ),



                                    html.Div([
                                        html.Div([
                                        html.Div(children=[
                                            html.P(children=[html.Strong(children=html.U(children='Water Withdrawal')),
                                                             ' Power Technology - Hydro / Year - 2010']),
                                        ], style={'margin-left': 20}),

                                        html.Img(src='data:image/png;base64,{}'.format(eencoded_image_five.decode()),
                                                 style={
                                                     'height': '100%',
                                                     'width': '90%',
                                                     # 'position': 'relative',
                                                     'margin-top': 5,
                                                     'margin-bottom': 10,
                                                     'margin-right': 20
                                                 }
                                                 )
                                    ], className='six columns'
                                    ),

                                    html.Div([
                                        html.Div(children=[
                                            html.P(children=[html.Strong(children=html.U(children='Water Withdrawal')),
                                                             ' Power Technology - Hydro / Year - 2050']),
                                        ], style={'margin-left': 20}),

                                        html.Img(src='data:image/png;base64,{}'.format(eencoded_image_six.decode()),
                                                 style={
                                                     'height': '100%',
                                                     'width': '90%',
                                                     # 'position': 'relative',
                                                     'margin-top': 5,
                                                     'margin-right': 20
                                                 }
                                                 )
                                          ], className='six columns'
                                          )
                                      ], className="row"
                                  ),


                                  html.Div([
                                        html.Div([
                                        html.Div(children=[
                                            html.P(children=[html.Strong(children=html.U(children='AC Transmission')),
                                                             ' Year - 2010']),
                                        ], style={'margin-left': 20}),

                                        html.Img(src='data:image/png;base64,{}'.format(eencoded_image_seven.decode()),
                                                 style={
                                                     'height': '100%',
                                                     'width': '90%',
                                                     # 'position': 'relative',
                                                     'margin-top': 5,
                                                     'margin-bottom': 10,
                                                     'margin-right': 20
                                                 }
                                                 )
                                    ], className='six columns'
                                    ),

                                    html.Div([
                                        html.Div(children=[
                                            html.P(children=[html.Strong(children=html.U(children='AC Transmission')),
                                                             ' Year - 2050']),
                                        ], style={'margin-left': 20}),

                                        html.Img(src='data:image/png;base64,{}'.format(eencoded_image_eight.decode()),
                                                 style={
                                                     'height': '100%',
                                                     'width': '90%',
                                                     # 'position': 'relative',
                                                     'margin-top': 5,
                                                     'margin-right': 20
                                                 }
                                                 )
                                          ], className='six columns'
                                          )
                                      ], className="row"
                                  ),
                              ]),


                            html.Div(
                                [
                                    html.H2(children=html.Em(
                                        children='SCENARIO 3: How a hurricane hitting a region home to a large industry can be fatal for its energy and fuel dependents'),
                                        style={'text-align': 'center', 'font-size': 18, 'margin-top': 20, 'margin-botton': 5, 'letter-spacing': .2},
                                        className='twelve columns'
                                    )
                                ], className="row"
                            ),

                              html.Div(
                              [
                                html.Div([
                                  html.Div([
                                    html.Div(children=[
                                      html.H3(children=html.Strong(children='Before'), style={'font-size': 20}),
                                      html.P(children=[html.Strong(children=html.U(children='Energy Generation:')),
                                                       ' Power Technology - DistPV / Year - 2010']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(eeencoded_image_one.decode()),
                                             style={
                                               'height': '100%',
                                               'width': '90%',
                                               # 'position': 'relative',
                                               'margin-top': 5,
                                               'margin-bottom': 10,
                                               'margin-right': 20
                                             }
                                             )
                                  ], className='six columns'
                                  ),

                                  html.Div([
                                    html.Div(children=[
                                      html.H3(children=html.Strong(children='After'), style={'font-size': 20}),
                                      html.P(children=[html.Strong(children=html.U(children='Energy Generation:')),
                                                       ' Power Technology - DistPV / Year - 2050']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(eeencoded_image_two.decode()),
                                             style={
                                               'height': '100%',
                                               'width': '90%',
                                               # 'position': 'relative',
                                               'margin-top': 5,
                                               'margin-bottom': 10,
                                               'margin-right': 20
                                             }
                                             )
                                  ], className='six columns'
                                  )
                                ], className="row"
                                ),

                                html.Div([
                                  html.Div([
                                    html.Div(children=[
                                      html.P(children=[html.Strong(children=html.U(children='Water Consumption:')),
                                                       ' Power Technology - Hydro / Year - 2010']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(eeencoded_image_three.decode()),
                                             style={
                                               'height': '100%',
                                               'width': '90%',
                                               # 'position': 'relative',
                                               'margin-top': 5,
                                               'margin-bottom': 10,
                                               'margin-right': 20
                                             }
                                             )
                                  ], className='six columns'
                                  ),

                                  html.Div([
                                    html.Div(children=[
                                      html.P(children=[html.Strong(children=html.U(children='Water Consumption:')),
                                                       ' Power Technology - Hydro / Year - 2050']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(eeencoded_image_four.decode()),
                                             style={
                                               'height': '100%',
                                               'width': '90%',
                                               # 'position': 'relative',
                                               'margin-top': 5,
                                               'margin-bottom': 10,
                                               'margin-right': 20
                                             }
                                             )
                                  ], className='six columns'
                                  )
                                ], className="row"
                                ),



                                html.Div([
                                    html.Div([
                                    html.Div(children=[
                                        html.P(children=[html.Strong(children=html.U(children='Water Withdrawal')),
                                                         ' Power Technology - CoalOldScr / Year - 2010']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(eeencoded_image_five.decode()),
                                             style={
                                                 'height': '100%',
                                                 'width': '90%',
                                                 # 'position': 'relative',
                                                 'margin-top': 5,
                                                 'margin-bottom': 10,
                                                 'margin-right': 20
                                             }
                                             )
                                ], className='six columns'
                                ),

                                html.Div([
                                    html.Div(children=[
                                        html.P(children=[html.Strong(children=html.U(children='Water Withdrawal')),
                                                         ' Power Technology - CoalOldScr / Year - 2050']),
                                    ], style={'margin-left': 20}),

                                    html.Img(src='data:image/png;base64,{}'.format(eeencoded_image_six.decode()),
                                             style={
                                                 'height': '100%',
                                                 'width': '90%',
                                                 # 'position': 'relative',
                                                 'margin-top': 5,
                                                 'margin-right': 20
                                             }
                                             )
                                      ], className='six columns'
                                      )



                                  ], className="row"
                                )


                              ]),

                                html.H2(
                                    style={'margin-top': 20,
                                           'margin-bottom': 20, 'padding-left': 180, 'padding-right': 180},
                                    className='twelve columns'
                                )










                    ])

            ]),

        html.Div(style={'padding-top' : 40,'padding-left' : 1000, 'margin-left' : -1000, 'margin-right' : -1000,  'margin-bottom' : 0, 'height' : '400%',
                     'background-color' : '#121212'}, children=[

        html.P(children=[html.Em(style= {'text-align': 'center', 'color' : '#ffffff'}, children=['Copyright 2019 - All Rights Reserved.'])])
    ])
    ], className='ten columns offset-by-one')

])


@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 year_value):
    dff = df2[df2['Year'] == year_value]

    return {
        'data': [go.Scatter(
            x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],

        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
            },
            yaxis={
                'title': yaxis_column_name,
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )

    }


@app.callback(
    dash.dependencies.Output('year-vs-value', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    ddf = df1[df1['balancingarea']==value]

    return {
        'data': [
                go.Scatter(
                    x=ddf[ddf['powertype'] == i]['year'],
                    y=ddf[ddf['powertype'] == i]['value'],
                    text=ddf[ddf['powertype'] == i]['powertype'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df1.powertype.unique()
            ],
        'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Year'},
                    yaxis={'title': 'Energy Generated'},
                    margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )

    }


@app.callback(
    dash.dependencies.Output('waterconsumption', 'figure'),
    [dash.dependencies.Input('my-dropdown-waterconsumption', 'value')])
def update_output(value):
    ddfwaterconsumption = dfwaterconsumption[dfwaterconsumption['balancingarea']==value]

    return {
        'data': [
                go.Scatter(
                    x=ddfwaterconsumption[ddfwaterconsumption['powertype'] == i]['year'],
                    y=ddfwaterconsumption[ddfwaterconsumption['powertype'] == i]['value'],
                    text=ddfwaterconsumption[ddfwaterconsumption['powertype'] == i]['powertype'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in ddfwaterconsumption.powertype.unique()
            ],
        'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Year'},
                    yaxis={'title': 'Energy Generated'},
                    margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )

    }


@app.callback(
    dash.dependencies.Output('waterwithdrawl', 'figure'),
    [dash.dependencies.Input('my-dropdown-waterwithdrawl', 'value')])
def update_output(value):
    ddfwaterwithdrawl = dfwaterwithdrawl[dfwaterwithdrawl['balancingarea']==value]

    return {
        'data': [
                go.Scatter(
                    x=ddfwaterwithdrawl[ddfwaterwithdrawl['powertype'] == i]['year'],
                    y=ddfwaterwithdrawl[ddfwaterwithdrawl['powertype'] == i]['value'],
                    text=ddfwaterwithdrawl[ddfwaterwithdrawl['powertype'] == i]['powertype'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in dfwaterwithdrawl.powertype.unique()
            ],
        'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Year'},
                    yaxis={'title': 'Energy Generated'},
                    margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )

    }


@app.callback(
    dash.dependencies.Output('year-vs-value1', 'figure'),
    [dash.dependencies.Input('my-dropdown1', 'value'),
     dash.dependencies.Input('powertechnologydropdown', 'value')])
def update_image(value, value1):
    ddf1 = Renewable_Energy_Technology[Renewable_Energy_Technology['BA']==value]
    ddf11 = ddf1[ddf1['powertype'] == value1]
    # dddf = ddf11[ddf11["RCP"].isin(selector)];
    return {
        'data': [
                go.Scatter(
                    x=ddf11[ddf11['RCP'] == i]['Year'],
                    y=ddf11[ddf11['RCP'] == i]['Value'],
                    text=ddf11[ddf11['RCP'] == i]['RCP'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i,
                ) for i in ddf1.RCP.unique()
            ],
        'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Year'},
                    yaxis={'title': 'Energy Generated'},
                    margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
        }


@app.callback(
    dash.dependencies.Output('sourcesink', 'figure'),
    [dash.dependencies.Input('my-dropdownSOURCE', 'value'),
     dash.dependencies.Input('my-dropdownSINK', 'value')])
def update_image(value, value1):
    ssddf1 = sourcesink[sourcesink['sourceBA']==value]
    ssddf11 = ssddf1[ssddf1['sinkBA'] == value1]
    # dddf = ddf11[ddf11["RCP"].isin(selector)];
    return {
        'data': [
                go.Scatter(
                    x=ssddf11[ssddf11['timeslice'] == i]['Year'],
                    y=ssddf11[ssddf11['timeslice'] == i]['FlowValue'],
                    text=ssddf11[ssddf11['timeslice'] == i]['timeslice'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i,
                ) for i in ssddf1.timeslice.unique()
            ],
        'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Year'},
                    yaxis={'title': 'AC Flow Value'},
                    margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
        }


@app.callback(
    dash.dependencies.Output('sourcesink1', 'figure'),
    [dash.dependencies.Input('my-dropdownSOURCE1', 'value'),
     dash.dependencies.Input('my-dropdownSINK1', 'value')])
def update_image(value, value1):
    ssddf1 = sourcesink[sourcesink['sourceBA']==value]
    ssddf11 = ssddf1[ssddf1['sinkBA'] == value1]
    # dddf = ddf11[ddf11["RCP"].isin(selector)];
    return {
        'data': [
                go.Scatter(
                    x=ssddf11[ssddf11['timeslice'] == i]['Year'],
                    y=ssddf11[ssddf11['timeslice'] == i]['FlowValue'],
                    text=ssddf11[ssddf11['timeslice'] == i]['timeslice'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i,
                ) for i in ssddf1.timeslice.unique()
            ],
        'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Year'},
                    yaxis={'title': 'AC Flow Value'},
                    margin={'l': 60, 'b': 60, 't': 20, 'r': 20},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
        }

@app.callback(
    dash.dependencies.Output('outputtechnologies', 'children'),
    [dash.dependencies.Input('acronym', 'value')])
def update_output(value):
    return tdf[tdf['acronym'] == value]['abbreviation']

if __name__ == '__main__':
    app.run_server(debug=True)
