from app import app
from .models import *
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

    ######################
    #### TEST METHODS ####
    ######################

    # Testing main page/index works
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Testing alternate route to the index
    def test_alt_main_page(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Testing contact page
    def test_contact_page(self):
        response = self.app.get('/contact', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Testing about page
    def test_about_page(self):
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Testing write page
    def test_write_page(self):
        response = self.app.get('/write', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Testing reviews page
    def test_reviews_page(self):
        response = self.app.get('/reviews', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Testing logout page
    def test_logout_page(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
