import json
import os
import threading
import time

from flask import Flask, request
from flask_restful import Resource, Api
# import api.helpers as helper
# from rss_feed import RssDownloader
import unirooms.api.helpers as helper
from unirooms.rss_feed.rss_downloader import RssDownloader

app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)

feed_update_time = int(os.getenv("UPDATE_FEED_IN_SECONDS"))

with open(os.getenv("LECTURES_JSON_FILE")) as f:
    lectures = json.load(f)
with open(os.getenv("ROOMS_JSON_FILE")) as f:
    room_data = json.load(f)

rd = RssDownloader()

def update_feed():
    global lectures
    global room_data
    while True:
        print("Updating feed")
        rd.run()

        with open(os.getenv("LECTURES_JSON_FILE")) as f:
            lectures = json.load(f)
        with open(os.getenv("ROOMS_JSON_FILE")) as f:
            room_data = json.load(f)
        
        time.sleep(feed_update_time)


threading.Thread(target=update_feed).start()
# print(lectures[0])

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
        self.data['optionalParameters_st_et'] = {
            "?startTime=<timestamp>&endTime=<timestamp>":
                "Moreover, you can define starttime and endtime to get the feed of specific time.",
            "example": "/api/E/5?startTime=1556870400&endTime=1556884800"
        }

    def get(self):
        return {'data': self.data}


class LecturesList(Resource):
    def get(self):
        return {'data': lectures[:]}


class AllRoomsList(Resource):
    def get(self):
        return {'data': room_data}


class Buildings(Resource):
    def __init__(self):
        self.data = []

    def get(self, building):
        self.data = helper.get_building_timetable(building.upper(), lectures)
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
        self.data = helper.get_floor_timetable(building.upper(), floor, lectures)
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
        self.data = helper.get_room_timetable(building.upper(), floor, room, lectures)
        if is_time_params_valid():
            self.data = helper.get_by_time_timetable(
                request.args.get('startTime'),
                request.args.get('endTime'),
                self.data)
        return {'data': self.data}


api.add_resource(Endpoints, '/')
api.add_resource(LecturesList, '/api/')
api.add_resource(AllRoomsList, '/api/rooms_stats')
api.add_resource(Buildings, '/api/<string:building>', endpoint='/api/building')
api.add_resource(Floors, '/api/<string:building>/<string:floor>', endpoint='/api/floor')
api.add_resource(Rooms, '/api/<string:building>/<string:floor>/<string:room>', endpoint='/api/room')

