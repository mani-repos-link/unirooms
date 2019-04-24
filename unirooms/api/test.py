import os

from unirooms import settings
from unirooms.rss_feed.rss_downloader import RssDownloader
from unirooms.rss_feed.feed_normalizer import FeedNormalizer


# import os
# os.getenv("RSS_FEED_URL")
# downloader = RssDownloader(os.getenv("RSS_FEED_URL"))
# downloader.save(os.getenv("FEED_JSON_FILE"))

n = FeedNormalizer(os.getenv("FEED_JSON_FILE"))
n.normalize()
