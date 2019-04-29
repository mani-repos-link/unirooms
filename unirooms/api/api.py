import os
from flask import Flask
from flask_restful import Resource, Api
from config import config
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)

with open(os.getenv("FEED_JSON_FILE")) as f:
    feed = json.load(f)


with open(os.getenv("ROOMS_JSON_FILE")) as f:
    room_data = json.load(f)


class get_feed(Resource):
    def get(self):
        return {'data': feed[:]}


# api.add_resource(get_feed, '/')
api.add_resource(get_feed, '/api')


class get_rooms_stats(Resource):
    def get(self):
        return {'data': room_data}


api.add_resource(get_rooms_stats, '/api/rooms_stats')

