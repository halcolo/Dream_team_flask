#This /app/__init__.py have the configuration and initaliaze of all the project

from flask import Flask

#Initialize the app
app = Flask(__name__, instance_relative_config=True)

#Load Views
from app import views

# Load the config file
app.config.from_object('config')