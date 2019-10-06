# When a directory has a file named "__init__.py" in it, it will run that file when being imported
from flask import Flask
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
# technically we should separate this out, but for a class project it doesn't matter
app.config['SECRET_KEY'] = 'how-many-penguins-exist-in-michigan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from app import routes