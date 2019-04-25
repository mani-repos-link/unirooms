from dotenv import load_dotenv
import os

#env_path = str(__file__).strip(os.path.basename(__file__)) + '.env'
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

test_var = os.getenv("RSS_FEED_URL")

print(test_var)