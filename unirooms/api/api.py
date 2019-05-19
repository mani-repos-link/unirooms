import os
import sys
import json
import threading
import time

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# adding config path to the system. So, config module will auto handle the other modules paths.
sys.path.append(os.path.abspath(os.path.dirname(os.path.realpath(__file__))+"/../config/"))
from config import config


"""
Now we can use unirooms as "namespace" for the modules.
"""
from unirooms.api.helpers import *
from unirooms.rss_feed.rss_downloader import RssDownloader


app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)
CORS(app)

__all__ = ["app", "great_list"]

feed_update_time = int(os.getenv("UPDATE_FEED_IN_SECONDS"))
great_list = get_fresh_timetable_data()

rd = RssDownloader()


def update_feed():
    global great_list
    while True:
        print("** -> Updating feed**")
        rd.run()
        great_list = get_fresh_timetable_data()
        time.sleep(feed_update_time)


th = threading.Thread(target=update_feed)
th.start()
# print("thread is closed!")


def is_time_params_valid():
    if request.args.get('startTime') is None or request.args.get('endTime') is None:
        return False
    if float(request.args.get('startTime')) > float(request.args.get('endTime')):
        return False
    return True


class Endpoints(Resource):
    def __init__(self):
        self.data = {}
        self.fill()

    def fill(self):
        self.data['/'] = "Returns what are you reading now."
        self.data['/api/'] = "Returns the whole lecture list"
        self.data['/api/<building>'] = "Returns the list of the lectures of specific building. The <building> " \
                                       "parameter should a capital letter."
        self.data['/api/<building>/<floor>'] = "Returns the list of the lectures of specific floor based on given " \
                                               "building. The <floor> parameter could be a numeric value."
        self.data['/api/<building>/<floor>/<room>'] = "Returns the list of the lectures of specific room" \
                                                      " Based on given building and floor. " \
                                                      "The <room> parameter should be a numeric value."
        self.data['/api/rooms_stats'] = "Returns the list of the lectures rooms."
        self.data['/api/lecturers/'] = "Returns the list of the professors or lab assistants."
        self.data['/api/lecturer/<string:professor>'] = "Returns the list of the lectures of given professor name."
        self.data['/api/subjects/'] = "Returns the list of the subjects thought in the uni."
        self.data['/api/subject/<string:title>'] = "Returns the data about specific subject based on title."
        self.data['optionalParameters_st_et'] = {
            "?startTime=<timestamp>&endTime=<timestamp>":
                "Moreover, you can define starttime and endtime to get the feed of specific time.",
            "example": "/api/E/5?startTime=1556870400&endTime=1556884800"
        }

    def get(self):
        return {'data': self.data}


class CompleteList(Resource):
    def get(self):
        return {'data': great_list}


class LecturesList(Resource):
    def get(self):
        return {'data': great_list["lectures"]}


class AllRoomsList(Resource):
    def get(self):
        return {'data': great_list["rooms"]}


class Buildings(Resource):
    def __init__(self):
        self.data = []

    def get(self, building):

        if building.upper() not in great_list["buildings"]:
            return {}

        self.data = great_list["buildings"][building.upper()]
        if is_time_params_valid():
            self.data = helper.get_by_time_timetable(
                request.args.get('startTime'),
                request.args.get('endTime'),
                self.data)
        return {'data': self.data}


class Floors(Resource):
    def __init__(self):
        self.data = []

    def get(self, building, floor):
        key = building.upper()+""+floor
        if key not in great_list["buildings"]["floors"]:
            return {}
        self.data = great_list["buildings"]["floors"][key]
        if is_time_params_valid():
            self.data = helper.get_by_time_timetable(
                request.args.get('startTime'),
                request.args.get('endTime'),
                self.data)
        return {'data': self.data}


class Rooms(Resource):
    def __init__(self):
        self.data = []

    def get(self, building, floor, room):
        # self.data = helper.get_room_timetable(building.upper(), floor, room, lectures)

        key = building.upper()+""+floor+""+room
        if key not in great_list["buildings"]["rooms"]:
            return {}

        self.data = great_list["buildings"]["rooms"][key]
        if is_time_params_valid():
            self.data = helper.get_by_time_timetable(
                request.args.get('startTime'),
                request.args.get('endTime'),
                self.data)
        return {'data': self.data}


class Lecturers(Resource):
    def get(self):
        # self.data = helper.get_room_timetable(building.upper(), floor, room, lectures)
        return {'data': great_list["lecturers"]}


class ProfessorLecture(Resource):
    def get(self, professor):
        key = professor.lower()
        similar_names = []
        for prof_name in (great_list["lecturers_lectures"]).keys():
            if key in prof_name.lower() or prof_name.lower() in key:
                similar_names.append(prof_name)

        if len(similar_names) == 0:
            return {}
        data = []
        for name in similar_names:
            data.append(great_list["lecturers_lectures"][name])
        if is_time_params_valid():
            data = helper.get_by_time_timetable(
                request.args.get('startTime'),
                request.args.get('endTime'),
                data)
        return {'data': data}


class SubjectList(Resource):
    def get(self):
        subjects = list(great_list["subjects"].keys())
        print(subjects)
        # return {'data': _list}
        return {'total': len(subjects), 'data': subjects}


class Subject(Resource):
    def get(self, title):
        key = title.lower()
        similar_names = []
        for title in (great_list["subjects"]).keys():
            if key in title.lower() or title.lower() in key:
                similar_names.append(title)

        if len(similar_names) == 0:
            return {}
        data = []
        for name in similar_names:
            data.append(great_list["subjects"][name])
        if is_time_params_valid():
            data = helper.get_by_time_timetable(
                request.args.get('startTime'),
                request.args.get('endTime'),
                data)
        return {'data': data}


api.add_resource(Endpoints, '/')
api.add_resource(LecturesList, '/api/')
api.add_resource(CompleteList, '/api/all/')
api.add_resource(Lecturers, '/api/lecturers/', endpoint='/api/lecturers')
api.add_resource(ProfessorLecture, '/api/lecturer/<string:professor>', endpoint='/api/lecturer')

api.add_resource(SubjectList, '/api/subjects/', endpoint='/api/subjectlist')
api.add_resource(Subject, '/api/subject/<string:title>', endpoint='/api/subject')

api.add_resource(AllRoomsList, '/api/rooms_stats')
api.add_resource(Buildings, '/api/<string:building>', endpoint='/api/building')
api.add_resource(Floors, '/api/<string:building>/<string:floor>', endpoint='/api/floor')
api.add_resource(Rooms, '/api/<string:building>/<string:floor>/<string:room>', endpoint='/api/room')


