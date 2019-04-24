import os

from .rss_feed.feed_normalizer import FeedNormalizer


# import os
# os.getenv("RSS_FEED_URL")
# downloader = RssDownloader(os.getenv("RSS_FEED_URL"))
# downloader.save(os.getenv("FEED_JSON_FILE"))

if __name__ == "__main__":
    n = FeedNormalizer(os.getenv("FEED_JSON_FILE"))
    n.normalize()
