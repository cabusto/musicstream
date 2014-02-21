import os
from flask import Flask

# single module, so we use __name__ to create the Flask object
app = Flask(__name__)


# set upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['UPLOADS_FOLDER'] = UPLOAD_FOLDER

from app import views

