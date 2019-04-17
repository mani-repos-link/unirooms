from dotenv import load_dotenv
load_dotenv(verbose=True)

# test test
import os
from rss_feed.rss_downloader import RssDownloader
from rss_feed.normalize_feed import NormalizeFeed



# import os
# os.getenv("RSS_FEED_URL")

# downloader = RssDownloader(os.getenv("RSS_FEED_URL"))
# downloader.save()

n = NormalizeFeed('resource/feed_data.json')
n.normalize()

