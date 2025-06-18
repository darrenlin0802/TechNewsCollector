# TechNewsCollector

A simple prototype for collecting technology news, generating a text summary, and optional podcast audio.

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install feedparser gtts
   ```
3. Run tests with `pytest`:
   ```bash
   pytest
   ```

## Usage

Use the CLI to fetch and summarize news. By default it reads a Google News RSS feed.

```bash
python -m technewscollector.cli --start 2024-03-01 --end 2024-03-03 --tickers TSLA --article summary.txt --podcast summary.mp3
```

This command saves a text summary to `summary.txt` and creates an MP3 podcast `summary.mp3`.
