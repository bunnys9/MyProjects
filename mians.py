from azure.storage.blob import BlobServiceClient
import json
import argparse
import datetime
import logging
import threading
import time
import requests
import re
import shutil
import json

from .connection import scoped_connection, scoped_advisory_lock
from .models import UPDATE_OBSERVATIONS_LOCK_ID
from joblib import Parallel, delayed



log = logging.getLogger()

Azure_container = os.get.env("container")
connect_string = os.get.env("connect_str")

