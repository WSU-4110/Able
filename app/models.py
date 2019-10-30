# This will hold our DB table schema
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


# We'll need to eventually design the whole Database, but this is fine enough now for the User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(30), nullable=False)
    email = db.Column(db.VARCHAR(120), nullable=False)
    password = db.Column(db.VARCHAR(150), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Method to debug by printing out results of creation when calling the object alone
    def __repr__(self):
        return 'User: {}, Email: {}'.format(self.username, self.email)


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    location = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.TEXT(), nullable=True)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    address = db.Column(db.VARCHAR(500), nullable=False)
    type = db.Column(db.VARCHAR(300), nullable=False)
    braille = db.Column(db.BOOLEAN, nullable=False, default=0)
    wheelchair = db.Column(db.BOOLEAN, nullable=False, default=0)
    closed_captions = db.Column(db.BOOLEAN, nullable=False, default=0)
    audio_captions = db.Column(db.BOOLEAN, nullable=False, default=0)
    quiet_space = db.Column(db.BOOLEAN, nullable=False, default=0)
    parking = db.Column(db.BOOLEAN, nullable=False, default=0)


db.create_all()
