import time
from rss_normalizer import normalize_feed
import json
import feedparser as fp
import os


class RssDownloader:

    DOWNLOAD_INTERVAL_IN_MINS = 60

    def __init__(self):
        self._feed_entries = []
        self._lecture_objects = []
        # TODO: get the url from the .env file:
        # self._url = os.getenv("RSS_FEED_URL")
        self._url = "http://aws.unibz.it/risweb/timetable.aspx?showtype=0&format=rss"

    def run(self):
        """
        Runs the rss feed downloader. Downloads the timetable rss
        feed every 'DOWNLOAD_INTERVAL_IN_MINS' minutes.
        """
        while True:
            self._download()
            self._lecture_objects = normalize_feed(self._feed)
            print(self._lecture_objects)
            #self._save()
            self._wait()

    def _wait(self):
        time.sleep(RssDownloader.DOWNLOAD_INTERVAL_IN_MINS * 60)

    def _download(self):
        self._feed = fp.parse(self._url)

    def _parse_rss_feed(self):
        for entry in self._feed.entries:
            entry = entry.summary
            info = entry.split(' - ')
            print(entry)
            self._feed_entries.append(info)

    def _save(self, file='../resource/feed_data.json'):
        with open(file, 'w') as f:
            json.dump(self._data, f, indent=4)


if __name__ == "__main__":
    rd = RssDownloader()
    rd.run()