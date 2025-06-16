import datetime
from dataclasses import dataclass
from typing import List, Optional
import feedparser

@dataclass
class Article:
    title: str
    link: str
    published: datetime.datetime
    summary: str


def fetch_articles(feed_url: str, start_date: Optional[datetime.datetime] = None,
                   end_date: Optional[datetime.datetime] = None,
                   tickers: Optional[List[str]] = None) -> List[Article]:
    """Fetch articles from an RSS feed and filter by date range and tickers."""
    feed = feedparser.parse(feed_url)
    articles: List[Article] = []
    for entry in feed.entries:
        # Parse publication date
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            published = datetime.datetime(*entry.published_parsed[:6])
        else:
            published = datetime.datetime.now()
        if start_date and published < start_date:
            continue
        if end_date and published > end_date:
            continue
        title_lower = entry.title.lower()
        if tickers:
            matched = False
            for ticker in tickers:
                if ticker.lower() in title_lower:
                    matched = True
                    break
            if not matched:
                continue
        articles.append(Article(
            title=entry.title,
            link=entry.link,
            published=published,
            summary=getattr(entry, 'summary', '')
        ))
    return articles
