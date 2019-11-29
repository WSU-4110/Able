from app import app
from app.models import *
import unittest
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class PyCharmTests(unittest.TestCase):

    # executed prior to each test
    def test_setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.config['BASEDIR'], 'able.db')
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # executed after each test
    def tearDown(self):
        pass

    def email_sending_test(self):
        response = self.app.get('/send_email_button', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()