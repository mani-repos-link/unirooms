import time
import os
import json
import feedparser as fp
from config import config
from rss_feed import *


class RssDownloader:

    def __init__(self):
        self._rooms_db = []
        self._feed_entries = []
        self._lecture_objects = []
        self._url = os.getenv("RSS_FEED_URL")

    def run(self):
        self._rooms_db = self._read_json(os.getenv("ROOMS_JSON_FILE"))

        self._download()
        self._lecture_objects, self._rooms_db = normalize_feed(self._feed, self._rooms_db)

        self._save_json(os.getenv("LECTURES_JSON_FILE"), self._lecture_objects)
        self._save_json(os.getenv("ROOMS_JSON_FILE"), self._rooms_db)

    def _download(self):
        self._feed = fp.parse(self._url)

    @staticmethod
    def _save_json(file, data):
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def _read_json(file):
        with open(file, 'r') as fs:
            data = json.load(fs)
        return data

