"""

CryptoPanic API Formatter.

Use Wrapper to make calls and get data.
Format data for streaming input and monitoring.
Historical Data seems to be limited to 12/24/2018 but there is no Documentation.

"""
import api_gather
# from importlib import reload
# reload(api_gather)

url_everything = api_gather.make_url(filter='hot')
everything_pages_last_100 = api_gather.get_pages_list_json(9, url_everything)

everything_pages_last_100_results = []
for page in everything_pages_last_100:
    everything_pages_last_100_results.append(page['results'])
df_results = api_gather.concatenate_pages(everything_pages_last_100_results)
