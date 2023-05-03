from dotenv import load_dotenv
import os


# Load environment variables from .env
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(basedir, '.env'))
