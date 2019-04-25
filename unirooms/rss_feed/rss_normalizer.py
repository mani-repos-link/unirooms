import json
import re
from datetime import datetime, timezone

lecture_type = {'lect': 'LECT', 'lab': 'LAB', 'unknown': 'UNKNOWN'}


def normalize_feed(feed):
    lectures = []
    for entry in feed.entries:
        entry = entry.summary
        entry = entry.split(' - ')
        if len(entry) != 5:
            continue

        # date and time
        date = entry[0]
        time = entry[1].split('-')
        start_time_timestamp = _datetimestr_to_timestamp(date, time[0])
        end_time_timestamp = _datetimestr_to_timestamp(date, time[1])

        # lecture title and type
        title = entry[2][:-5].strip()
        lect_type = entry[2][-4:]

        # location
        location = entry[3][:4]
        # Try matching string beginning with upper case letter followed
        # by three digits. If match does not succeed, the location is
        # probably not in Bozen se we can skip it.
        match_location = re.match("[A-Z][0-9]{3}", location)
        if not match_location:
            continue
        building = location[0]
        floor = location[1]
        room = location[2:4]

        # lecturer
        lecturer = entry[4]
        print(location, ' ', lecturer)

        lecture_object = {
            "building": building,
            "floor": floor,
            "room": room,
            "start-timestamp": start_time_timestamp,
            "end-timestamp": end_time_timestamp,
            "title": title,
            "type": lect_type,
            "lecturer": lecturer
        }
        lectures.append(lecture_object)
    return lectures


def _datetimestr_to_timestamp(datestr, timestr):
    datestr = datestr.split('.')
    day = int(datestr[0])
    month = int(datestr[1])
    year = int(datestr[2])

    timestr = timestr.split(':')
    hour = int(timestr[0])
    minute = int(timestr[1])

    d = datetime(year, month, day, hour, minute, tzinfo=timezone.utc)
    return datetime.timestamp(d)


def _get_lecture_type(title):
    if len(title) < 8:
        return lecture_type['unknown']
    last_chars = (title[-4:])
    if last_chars not in lecture_type:
        last_chars = lecture_type['unknown']
    return last_chars
