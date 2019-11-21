# This will hold our DB table schema
from app import db, login
# UserMixin is a class that provides all the functionality of flask_login in one class
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# We'll need to eventually design the whole Database, but this is fine enough now for the User table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(30), nullable=False)
    email = db.Column(db.VARCHAR(120), nullable=False)
    password = db.Column(db.VARCHAR(150), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.Integer, db.ForeignKey('location.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer, autoincrement=True)
    review = db.Column(db.TEXT())


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.VARCHAR(500), nullable=False)
    type = db.Column(db.VARCHAR(300), nullable=False)
    braille = db.Column(db.BOOLEAN, nullable=False, default=0)
    wheelchair = db.Column(db.BOOLEAN, nullable=False, default=0)
    closed_captions = db.Column(db.BOOLEAN, nullable=False, default=0)
    audio_captions = db.Column(db.BOOLEAN, nullable=False, default=0)
    quiet_space = db.Column(db.BOOLEAN, nullable=False, default=0)
    parking = db.Column(db.BOOLEAN, nullable=False, default=0)
