from app import app
from .models import *
import os
import unittest


class FLaskTest(unittest.TestCase):

    # Setup#
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                                'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # Post-Test#
    def tearDown(self):
        pass

    # Tests#

    #Testing Main Page
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    #Testing Contact Page
    def test_contact_page(self):
        response = self.app.get('/contact', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    #Testing Navigation Page
    def test_navigation_page(self):
        response = self.app.get('/navigation', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    #Testing Backup Navigation Page
    def test_navigation_page(self):
        response= self.app.get('/navigationBack', follow_redirects=True)
        self.assertEqual(response.status_code,200)

    #Testing About Page
    def test_about_page(self):
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code,200)

    #Testing Reviews
    def test_reviews_page(self):
        response=self.app.get('/reviews', follow_redirects= True)
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()