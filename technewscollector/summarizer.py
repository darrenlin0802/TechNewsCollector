from typing import List
from .aggregator import Article


def summarize_articles(articles: List[Article], max_sentences: int = 5) -> str:
    """Create a simple summary by concatenating the first sentence of each article."""
    summaries = []
    for article in articles:
        text = article.summary or article.title
        # naive sentence split
        sentence = text.split('. ')[0]
        summaries.append(f"- {sentence.strip('.')}. (Source: {article.link})")
        if len(summaries) >= max_sentences:
            break
    return "\n".join(summaries)
