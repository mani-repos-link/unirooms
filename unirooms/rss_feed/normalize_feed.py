import json


class NormalizeFeed:
    def __init__(self, file):
        self.filename = file
        self.lecture_type = {'lect': 'LECT', 'lab': 'LAB', 'unknown': 'UNKNOWN'}

    def normalize(self):
        self.data = []
        with open(self.filename) as f:
            self._feed = json.load(f)

        for obj in self._feed:
            lect_type = self.__get_lecture_type(obj['title'])
            normlized_object = {
                "date": obj.date,
                "start": obj.time.split[' '][0],
                "end": obj.time.split[' '][1],
                "title": (obj.title.split[' '][1]).replace(lect_type, ''),
                "type": lect_type,
            }
            self.data.append(normlized_object)

    def __get_lecture_type(self, title):
        if len(title) < 8:
            return self.lecture_type['unknown']
        last_chars = (title[-5:]).rstrip().lstrip()
        if last_chars not in self.lecture_type:
            last_chars = self.lecture_type['unknown']
        return last_chars

