from app import app
from .models import *
import unittest
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class MyTestCase(unittest.TestCase):
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

    def test_account_creation_email_sending(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_switch(self):
        response = self.app.get('/user_profile', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_return_to_menu(self):
        response = self.app.get('/return_to_menu', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_write_new_review(self):
        response = self.app.get('/write', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_show_new_reviews(self):
        response = self.app.get('/show_reviews', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_email_sending_button(self):
        response = self.app.get('/send_email_button', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
