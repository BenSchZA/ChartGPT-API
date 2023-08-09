import streamlit as st
from dotenv import load_dotenv
import os
import firebase_admin
import logging
import json
from importlib import import_module
from firebase_admin import firestore


# Display app name
PAGE_NAME = "ChartGPT"
st.set_page_config(page_title=PAGE_NAME, page_icon="📈")

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Load environment variables from .env
load_dotenv()
# If set, Streamlit secrets take preference over environment variables
os.environ.update(st.secrets)

ENV = os.environ.get("ENV", "LOCAL")
URL = os.environ.get("URL", "http://localhost:8501")

if ENV == "LOCAL":
    import app_secrets.gcp_service_accounts

if DEBUG := (os.getenv('DEBUG', 'false').lower() == 'true'):
    logger.warning("Application in debug mode, disable for production")
    fh = logging.FileHandler('logs/debug.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(fh)

if DISPLAY_USER_UPDATES := (os.getenv('DISPLAY_USER_UPDATES', 'false').lower() == 'true'):
    logger.info("User updates will be displayed")

if MAINTENANCE_MODE := (os.getenv('MAINTENANCE_MODE', 'false').lower() == 'true'):
    logger.info("Application in maintenance mode")

# Import sample question for project
datasets = import_module(f'app.config.{os.environ["PROJECT"].lower()}').datasets

# Initialise Google Cloud Firestore
if not firebase_admin._apps:
    try:
        if ENV == "LOCAL":
            cred = firebase_admin.credentials.Certificate(json.loads(os.environ['GCP_SERVICE_ACCOUNT']))
            _ = firebase_admin.initialize_app(cred)
        else:
            _ = firebase_admin.initialize_app()
    except ValueError as e:
        _ = firebase_admin.get_app(name='[DEFAULT]')

db = firestore.client()
db_charts = db.collection('charts')
db_users = db.collection('users')
db_queries = db.collection('queries')
