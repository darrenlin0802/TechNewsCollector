import sys, os; sys.path.insert(0, os.path.abspath("."))
import datetime
from technewscollector.aggregator import fetch_articles

SAMPLE_FEED = 'tests/sample.rss'


def test_fetch_articles_filters_by_ticker():
    start = datetime.datetime(2024, 3, 1)
    end = datetime.datetime(2024, 3, 3)
    articles = fetch_articles(SAMPLE_FEED, start_date=start, end_date=end, tickers=['TSLA'])
    assert len(articles) == 1
    assert 'Tesla' in articles[0].title
