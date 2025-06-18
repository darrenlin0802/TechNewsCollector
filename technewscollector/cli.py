import argparse
import datetime

from .aggregator import fetch_articles
from .summarizer import summarize_articles
from .podcast import text_to_speech

DEFAULT_FEED = 'https://news.google.com/rss/search?q=technology&hl=en-US&gl=US&ceid=US:en'


def parse_args():
    parser = argparse.ArgumentParser(description='TechNewsCollector CLI')
    parser.add_argument('--start', type=str, help='Start date YYYY-MM-DD')
    parser.add_argument('--end', type=str, help='End date YYYY-MM-DD')
    parser.add_argument('--tickers', nargs='*', help='Ticker symbols to filter')
    parser.add_argument('--feed', type=str, default=DEFAULT_FEED, help='RSS feed URL')
    parser.add_argument('--article', type=str, help='Path to save article text')
    parser.add_argument('--podcast', type=str, help='Path to save podcast MP3')
    parser.add_argument('--lang', type=str, default='en', help='Podcast language code')
    return parser.parse_args()


def main():
    args = parse_args()
    start = datetime.datetime.fromisoformat(args.start) if args.start else None
    end = datetime.datetime.fromisoformat(args.end) if args.end else None
    articles = fetch_articles(args.feed, start_date=start, end_date=end, tickers=args.tickers)
    summary = summarize_articles(articles)
    if args.article:
        with open(args.article, 'w', encoding='utf-8') as f:
            f.write(summary)
    if args.podcast:
        text_to_speech(summary, args.podcast, lang=args.lang)
    if not args.article and not args.podcast:
        print(summary)


if __name__ == '__main__':
    main()
