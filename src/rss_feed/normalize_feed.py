import json


class NormalizeFeed:

    def __init__(self, file):
        self.filename = file
        pass

    def normalize(self):
        self.data = []
        with open(self.filename) as f:
            self._feed = json.load(f)

        for obj in self._feed:
            normlized_object = {
                "date": obj.date,
                "start": obj.time.split[' '][0],
                "end": obj.time.split[' '][1],
                "title": obj.title.split[' '][1],
            }


