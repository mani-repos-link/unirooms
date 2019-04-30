import time
import os
import json
import feedparser as fp
from config import config
from rss_feed import *


class RssDownloader:

    def __init__(self):
        self._feed_entries = []
        self._lecture_objects = []
        self._url = os.getenv("RSS_FEED_URL")

    def run(self):
        self._download()
        self._lecture_objects = normalize_feed(self._feed)
        # print(self._lecture_objects)
        self._save(os.getenv("LECTURES_JSON_FILE"))

    def _download(self):
        self._feed = fp.parse(self._url)

    def _save(self, file):
        with open(file, 'w') as f:
            json.dump(self._lecture_objects, f, indent=4)
