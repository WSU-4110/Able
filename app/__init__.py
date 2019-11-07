# When a directory has a file named "__init__.py" in it, it will run that file when being imported
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


# Setting up SQLite to work
basedir = os.path.abspath(os.path.dirname(__file__))
# Instantiating Flask
app = Flask(__name__)
# Bootstrap CSS
Bootstrap(app)
# technically we should separate this out, but for a class project it doesn't matter
app.config['SECRET_KEY'] = 'how-many-penguins-exist-in-michigan'
# On two lines to follow PEP8 standards
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                        'sqlite:///' + os.path.join(basedir, 'able.db')
# Suppresses a debug message
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Instantiate SQLAlchemy object
db = SQLAlchemy(app)
# We most likely will not be using this since we will have no need to migrate what little data we have in testing
# to another database schema
migrate = Migrate(app, db)

# Why are these at the bottom? Couldn't tell ya! :)
from app import routes, models, notifications