"""
CryptoPanic API Wrapper.

Docs for API found here. https://cryptopanic.com/developers/api/

CryptoPanic Server is cached every 30 seconds. So crawling at a faster rate is pointless.
All API methods are rate limited per IP at 5req/sec.

Use like this:

    df = concatenate_pages(pages_list=get_pages_list_json(2, make_url(filter='hot', currencies='btc,eth,xrp')))

"""

import requests
import pandas as pd
import datetime
import config
import time

global_api_rate_delay = .2  # All API methods are rate limited per IP at 5req/sec.


def make_url(filter=None, currencies=None, kind=None, region=None, page=None):
    """Handle of URL variables for API POST."""
    url = 'https://cryptopanic.com/api/v1/posts/?auth_token={}'.format(config.API_KEY)

    if currencies is not None:
        if len(currencies.split(',')) <= 50:
            url += "&currencies={}".format(currencies)
        else:
            print("Warning: Max Currencies is 50")
            return

    if kind is not None and kind in ['news', 'media']:
        url += "&kind={}".format(kind)

    filters = ['rising', 'hot', 'bullish', 'bearish', 'important', 'saved', 'lol']
    if filter is not None and filter in filters:
        url += "&filter={}".format(filter)

    regions = ['en', 'de', 'es', 'fr', 'it', 'pt', 'ru']  # (English), (Deutsch), (Español), (Français), (Italiano), (Português), (Русский)--> Respectively
    if region is not None and region in regions:
        url += "&region={}".format(region)

    if page is not None:
        url += "&page={}".format(page)

    return url


def get_page_json(url=None):
    """
    Get First Page.

    Returns Json.

    """
    time.sleep(global_api_rate_delay)
    if not url:
        url = "https://cryptopanic.com/api/v1/posts/?auth_token={}".format(config.API_KEY)
    page = requests.get(url)
    data = page.json()
    return data


def get_pages_list_json(lookback, url):
    """
    Get history of pages starting from page 1 to the lookback.

    Returns: List of Pages in Json format

    """
    pages_list_json = [get_page_json(url)]

    for i in range(lookback):
        pages_list_json.append(get_page_json(pages_list_json[i]["next"]))

    return pages_list_json


def get_df(data):
    """Return pandas DF."""
    df = pd.DataFrame(data)
    try:
        df['created_at'] = pd.to_datetime(df.created_at)
    except Exception as e:
        pass

    return df


def concatenate_pages(pages_list):
    """Concatenate Pages into one Dataframe."""
    frames = []
    for page in pages_list:
        frames.append(get_df(page))

    return pd.concat(frames, ignore_index=True)

# df = concatenate_pages(get_pages_list_json(2, make_url()))
