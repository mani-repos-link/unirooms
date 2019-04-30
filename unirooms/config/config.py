# -*- coding: utf-8 -*-
"""

This Python file contains some configurations to manage Unirooms.
It loads .env file from root of this project.

This file should be imported wherever configuration or environment variables are used.

"""

from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath((str(__file__) + "/../../../")) + "/"

# Connect the path with your '.env' file name
load_dotenv(dotenv_path=BASEDIR + '.env', verbose=True)

os.environ['project_dir'] = BASEDIR
os.environ['LECTURES_JSON_FILE'] = BASEDIR + os.getenv("LECTURES_JSON_FILE")
os.environ['ROOMS_JSON_FILE'] = BASEDIR + os.getenv("ROOMS_JSON_FILE")
# os.environ['NORMALIZED_JSON_FILE'] = BASEDIR + os.getenv("NORMALIZED_JSON_FILE")






