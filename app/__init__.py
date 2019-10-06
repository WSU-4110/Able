# When a directory has a file named "__init__.py" in it, it will run that file when being imported
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


# Setting up SQLite to work
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
Bootstrap(app)
# technically we should separate this out, but for a class project it doesn't matter
app.config['SECRET_KEY'] = 'how-many-penguins-exist-in-michigan'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'able.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Why are these at the bottom? Couldn't tell ya! :)
from app import routes, models