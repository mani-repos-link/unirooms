import os
from settings import settings
from rss_feed.rss_downloader import RssDownloader
from rss_feed.normalize_feed import NormalizeFeed


# import os
# os.getenv("RSS_FEED_URL")
# downloader = RssDownloader(os.getenv("RSS_FEED_URL"))
# downloader.save(os.getenv("FEED_JSON_FILE"))

n = NormalizeFeed(os.getenv("FEED_JSON_FILE"))
n.normalize()
