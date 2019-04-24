import json


class FeedNormalizer:
    def __init__(self, file):
        self.filename = file
        self.lecture_type = {'lect': 'LECT', 'lab': 'LAB', 'unknown': 'UNKNOWN'}
        self.data = []

    def normalize(self):
        with open(self.filename) as f:
            feed = json.load(f)
        for obj in feed:
            lect_type = self.__get_lecture_type(obj['title'])
            if lect_type == self.lecture_type["unknown"]:
                continue
            normalized_object = {
                "date": obj.date,
                "start-time": obj.time.split[' '][0],
                "end-time": obj.time.split[' '][1],
                "title": (obj.title.split[' '][1]).replace(lect_type, ''),
                "type": lect_type,
                "lecturer": obj['lecturer'],
                "room": obj['room'][0:5].strip(),
                "faculty": lect_type,
            }
            print(normalized_object)
            break;
            self.data.append(normalized_object)

    def __get_lecture_type(self, title):
        if len(title) < 8:
            return self.lecture_type['unknown']
        last_chars = (title[-5:]).strip()
        if last_chars not in self.lecture_type:
            last_chars = self.lecture_type['unknown']
        return last_chars

