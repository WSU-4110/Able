# This will hold our DB table schema
from app import db


# We'll need to eventually design the whole Database, but this is fine enough now for the User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(30))
    email = db.Column(db.VARCHAR(120))
    password = db.Column(db.VARCHAR(40))

    # Method to debug by printing out results of creation when calling the object alone
    def __repr__(self):
        return 'User: {}, Email: {}'.format(self.username, self.email)
