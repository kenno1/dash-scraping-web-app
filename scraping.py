from bs4 import BeautifulSoup
import requests

from assets.database import db_session
from assets.models import Data
import datetime

def get_udemy_info():
    url = 'https://scraping-for-beginner.herokuapp.com/udemy'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    n_subscribers = soup.select('.subscribers')[0].string
    n_subscribers = int(n_subscribers.split('：')[1])

    n_reviews = soup.select('.reviews')[0].string
    n_reviews = int(n_reviews.split('：')[1])

    results = {
        'n_subscribers' : n_subscribers,
        'n_reviews' : n_reviews
    }

    return results

def write_data():
    
    _results = get_udemy_info()

    date = datetime.date.today()
    subscribers = _results['n_subscribers']
    reviews = _results['n_reviews']
    
    row = Data(date=date, subscribers=subscribers, reviews=reviews)

    db_session.add(row)
    db_session.commit()

if __name__ == '__main__':
    write_data()