"""
 This python file is used only for test the scripts.
"""

import os
from config import config
from rss_feed import rss_downloader

print("print test", "Executing from", __file__)
test_var = os.getenv("NORMALIZED_JSON_FILE")

print("print test", test_var)
print("print test", os.getenv('project_dir'))

# r = rss_downloader()  # need some refactoring in the class


