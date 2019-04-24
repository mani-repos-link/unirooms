from datetime import date
import json
import feedparser as fp


def get_today_date():
    return str(date.today().strftime('%d.%m.%Y'))


class RssDownloader:
    def __init__(self, url):
        self.feed = fp.parse(url)
        self._get_feed()

    def _get_feed(self):
        self.data = []
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
            self.data.append(obj)
        return self.data

    def get_entries(self):
        return self.data

    def save(self, file='../resource/feed_data.json'):
        with open(file, 'w') as f:
            json.dump(self.data, f, indent=4)
