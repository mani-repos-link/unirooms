from datetime import date
import json
import feedparser as fp
import os
import time


def get_today_date():
    return str(date.today().strftime('%d.%m.%Y'))


class RssDownloader:

    DOWNLOAD_INTERVAL_IN_MINS = 60

    def __init__(self):
        self._data = []
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
            self._save()
            self._wait()

    def _wait(self):
        time.sleep(RssDownloader.DOWNLOAD_INTERVAL_IN_MINS * 60)

    def _download(self):
        self._feed = fp.parse(self._url)

    def _parse_rss_feed(self):
        print(self.feed)
        for entry in self.feed.entries:
            entry = entry.summary
            info = entry.split(' - ')
            obj = {
                'date': info[0],
                'time': info[1],
                'title': info[2],
                'room': info[3] if len(info) > 4 else '',
                'lecturer': info[4] if len(info) > 4 else ''
            }
            print(obj)
            self._data.append(obj)

    def _save(self, file='../resource/feed_data.json'):
        with open(file, 'w') as f:
            json.dump(self._data, f, indent=4)


if __name__ == "__main__":
    rd = RssDownloader()
    rd.run()