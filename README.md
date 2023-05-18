# APNews Web Scraper

This Python package, `apnews`, provides a simple way to scrape top news articles from the Associated Press website.

## Installation

You can install `apnews` from PyPI:

```shell
pip install apnews
```

## Usage

Here is an example of how to use `apnews`:

```python
import apnews

articles = apnews.scrape_top_news()
for title, article in articles:
    print(title, article)
```

## License

This project is licensed under the terms of the MIT license.
