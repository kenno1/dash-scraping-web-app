import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('assets/data.csv')

dates = []
for _date in df['date']:
    date = datetime.datetime.strptime(_date, '%Y/%m/%d').date()
    dates.append(date)

n_subscribers = df['subscribers'].values
n_reviews = df['reviews'].values

diff_subscribers = df['subscribers'].diff().values
diff_reviews = df['reviews'].diff().values

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H2(children='Python Web Scraping ~ application ~ '),
    html.Div(children=[
        dcc.Graph(
            id='subscriber_graph',
            figure={
                'data':[
                    go.Scatter(
                        x=dates,
                        y=n_subscribers,
                        mode='lines+markers',
                        name='Number of students',
                        opacity=0.7,
                        yaxis='y1'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_subscribers,
                        name='Increased number of students',
                        yaxis='y2'
                    )
                ],
                'layout':go.Layout(
                    title='Transition number of students',
                    xaxis=dict(title='date'),
                    yaxis=dict(title='Number of students', side='left', showgrid=False,
                    range=[2000, max(n_subscribers)+100]),
                    yaxis2=dict(title='Increased number of students', side='right', overlaying='y', showgrid=False,
                    range=[0, max(diff_subscribers[1:])]),
                    margin=dict(l=200, r=200, b=100, t=100)
                )
            }
        ),
        dcc.Graph(
            id='review_graph',
            figure={
                'data':[
                    go.Scatter(
                        x=dates,
                        y=n_reviews,
                        mode='lines+markers',
                        name='Number of reviews',
                        opacity=0.7,
                        yaxis='y1'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_reviews,
                        name='Increased number of reviews',
                        yaxis='y2'
                    )
                ],
                'layout':go.Layout(
                    title='Transition number of reviews',
                    xaxis=dict(title='date'),
                    yaxis=dict(title='Number of reviews', side='left', showgrid=False,
                    range=[0, max(n_reviews)+10]),
                    yaxis2=dict(title='Increased number of reviews', side='right', overlaying='y', showgrid=False,
                    range=[0, max(diff_reviews[1:])]),
                    margin=dict(l=200, r=200, b=100, t=100)
                )
            }
        )
    ])
],style={
    'textAlign': 'center',
    'width': '1200px',
    'margin': '0 auto'
})

if __name__ == '__main__':
    app.run_server(debug=True)
