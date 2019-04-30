import os
from flask import Flask
from flask_restful import Resource, Api
from config import config
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)

with open(os.getenv("FEED_JSON_FILE")) as f:
    lectures = json.load(f)


with open(os.getenv("ROOMS_JSON_FILE")) as f:
    room_data = json.load(f)


class Lectures(Resource):
    def get(self):
        return {'data': lectures[:]}


# api.add_resource(get_feed, '/')
api.add_resource(Lectures, '/api')


class Rooms(Resource):
    def get(self):
        return {'data': room_data}


api.add_resource(Rooms, '/api/rooms_stats')

