"""
 This python file is used only for test the scripts.
"""
import os
import json
try:
    from unirooms.config import config
except:
    import config.config

from unirooms.api import api

if __name__ == '__main__':
    print("This is only DEVELOPMENT SERVER.")
    print("\n************                 ************")
    print("******                             ******")
    print("*** Feed Updating thread is launched. ***")
    print("******                             ******\n\n")
    api.app.run(debug=False)

