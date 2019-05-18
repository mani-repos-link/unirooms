# -*- coding: utf-8 -*-
"""

This Python file contains some configurations to manage Unirooms.
It loads .env file from root of this project.

This file should be imported wherever configuration or environment variables are used.

"""

import sys
from dotenv import load_dotenv
import os


# this is not good way to find path
BASEDIR = os.path.abspath((str(__file__)) + "/../../../") + "/"  # project root directory
UNIROOMS_MODULE = BASEDIR + "unirooms/"  # project modules/logic
API_PATH_MODULE = UNIROOMS_MODULE + "api/"  # api module path
RSS_FEED_MODULE = UNIROOMS_MODULE + "rss_feed/"  # rss feed module path


if BASEDIR not in sys.path:  # dynamically adding the path to sys
    sys.path.insert(0, BASEDIR)

if UNIROOMS_MODULE not in sys.path:
    sys.path.append(UNIROOMS_MODULE)

if API_PATH_MODULE not in sys.path:
    sys.path.append(API_PATH_MODULE)

if RSS_FEED_MODULE not in sys.path:
    sys.path.append(RSS_FEED_MODULE)


# Connect the path with your '.env' file name
load_dotenv(dotenv_path=BASEDIR + '.env', verbose=True)

os.environ['project_dir'] = BASEDIR
if BASEDIR not in os.environ['LECTURES_JSON_FILE']:
    os.environ['LECTURES_JSON_FILE'] = BASEDIR + os.getenv("LECTURES_JSON_FILE")
    os.environ['ROOMS_JSON_FILE'] = BASEDIR + os.getenv("ROOMS_JSON_FILE")


