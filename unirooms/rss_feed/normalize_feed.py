import json


class NormalizeFeed:
    def __init__(self, file):
        self.filename = file
        self.lecture_type = {
            'lect': 'LECT',
            'lab': 'LAB',
            'unknown': 'UNKNOWN'
        }
        pass

    def normalize(self):
        self.data = []
        with open(self.filename) as f:
            self._feed = json.load(f)

        for obj in self._feed:
            print(obj)
            print(self.__get_lecture_type(obj.title))
            break
            normlized_object = {
                "date": obj.date,
                "start": obj.time.split[' '][0],
                "end": obj.time.split[' '][1],
                "title": obj.title.split[' '][1],
            }
            self.data.append(normlized_object)

    def __get_lecture_type(self, title):
        if len(title) < 8:
            return self.lecture_type['unknown']
        last_chr = title[-1:8]
        print(last_chr)
        return last_chr
