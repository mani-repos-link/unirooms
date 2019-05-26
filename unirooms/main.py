"""
 This python file is used only for test the scripts.
"""
import sys
import os
import json

sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/config/")

from config import config
from unirooms.api.api import *


if __name__ == '__main__':
    print("\n\nThis is only the DEVELOPMENT SERVER.")
    print("\n************                 ************")
    print("******                             ******")
    print("*** Feed Updating thread is launched. ***")
    print("******                             ******\n\n")
    app.run(debug=True)
