from config import config
import sys
import os
import json

sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/config/")

from unirooms.rss_feed.rss_downloader import RssDownloader


rs = RssDownloader()
rs.run();
