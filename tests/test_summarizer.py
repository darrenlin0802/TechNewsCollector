import sys, os; sys.path.insert(0, os.path.abspath("."))
from technewscollector.aggregator import Article
from technewscollector.summarizer import summarize_articles
import datetime


def test_summarize_articles_basic():
    articles = [
        Article(title='Test Article', link='http://example.com',
                published=datetime.datetime.now(), summary='This is a test. More details here.')
    ]
    summary = summarize_articles(articles)
    assert 'This is a test' in summary
