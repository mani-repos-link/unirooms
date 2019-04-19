from dotenv import load_dotenv
import os

env_path = str(__file__).strip(os.path.basename(__file__)) + '../.env'
load_dotenv(dotenv_path=env_path)





