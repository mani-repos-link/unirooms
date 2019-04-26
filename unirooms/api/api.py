import os
from flask import Flask
from flask_restful import Resource, Api
from config import config
import json

app = Flask(__name__)
api = Api(app)

with open(os.getenv("FEED_JSON_FILE")) as f:
    feed = json.load(f)


class get_feed(Resource):
    def get(self):
        return {'data': feed[:]}


api.add_resource(get_feed, '/api')

