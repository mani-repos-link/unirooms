"""
 This python file is used only for test the scripts.
"""

from config import config
import os
from rss_feed import RssDownloader
import json
from api import *

# print("print test", "Executing from", __file__)
# print("print test", os.getenv('project_dir'))
# print("print LECTURES_JSON_FILE", os.getenv('LECTURES_JSON_FILE'))


# r = RssDownloader()
# r.run()


app.run(debug=False)

