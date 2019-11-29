from app import app
from .models import *
from .routes import *
import unittest
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class FlaskTests(unittest.TestCase):

    # Runs before every test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                                'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # Runs after every test
    def tearDown(self):
        pass

    def test_email_sending(self):
        response = self.app.get('/send_email_button', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_switch(self):
        response = self.app.get('/user_profile', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_return_to_menu(self):
        response = self.app.get('/return_to_menu', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_show_new_reviews(self):
        response = self.app.get('/show_reviews', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()