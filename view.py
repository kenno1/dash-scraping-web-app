import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime
from assets.database import db_session
from assets.models import Data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()

dates = []
subscribers = []
reviews = []

for datum in data:
    dates.append(datum.date)
    subscribers.append(datum.subscribers)
    reviews.append(datum.reviews)

diff_subscribers = pd.Series(subscribers).diff().values
diff_reviews = pd.Series(reviews).diff().values

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H2(children='Python Web Scraping ~ application ~ '),
    html.Div(children=[
        dcc.Graph(
            id='subscriber_graph',
            figure={
                'data':[
                    go.Scatter(
                        x=dates,
                        y=subscribers,
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
                    range=[2000, max(subscribers)+100]),
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
                        y=reviews,
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
                    range=[0, max(reviews)+10]),
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
