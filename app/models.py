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

    # Method to debug by printing out results of creation when calling the object alone
    # No point in printing the password as it will be hashed
    def __repr__(self):
        return 'ID: {}, User: {}, Email: {}'.format(self.id, self.username, self.email)


# Helper function for login functionality
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.Integer, db.ForeignKey('location.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.TEXT())

    # Method to debug by printing out results of creation when calling the object alone
    def __repr__(self):
        return 'ID: {}, Location: {}, User: {}, Rating: {}, Review: {}'.format(self.id, self.location, self.user,
                                                                               self.rating, self.review)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.VARCHAR(500), nullable=False)
    type = db.Column(db.VARCHAR(300), nullable=False)
    braille = db.Column(db.BOOLEAN, nullable=False, default=0)
    wheelchair = db.Column(db.BOOLEAN, nullable=False, default=0)
    closed_captions = db.Column(db.BOOLEAN, nullable=False, default=0)
    quiet_space = db.Column(db.BOOLEAN, nullable=False, default=0)
    parking = db.Column(db.BOOLEAN, nullable=False, default=0)

    # Method to debug by printing out results of creation when calling the object alone
    def __repr__(self):
        return 'ID: {}, Address: {}, Braille: {}, Wheelchair: {}, CC: {},' \
               'Quiet Space: {}, Parking: {}'.format(self.id, self.address, self.braille, self.wheelchair,
                                                     self.closed_captions, self.quiet_space, self.parking)
