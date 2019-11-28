from app import app
from .models import *
import os
import unittest

class FlaskTest(unittest.TestCase):

     # Setup segment runs prior to every test being executed
     def setUp(self):
         app.config['TESTING'] = True
         app.config['WTF_CSRF_ENABLED'] = False
         app.config['DEBUG'] = False
         app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                                 'sqlite:///' + os.path.join(basedir, 'test.db')
         self.app = app.test_client()
         db.drop_all()
         db.create_all()

     # Teardown segment for after each test is executed
     def tearDown(self):
         pass

     # Six Testing Methods #

     # Test 1: Main Page
     def test_main_page(self):
         response = self.app.get('/', follow_redirects=True)
         self.assertEqual(response.status_code, 200)
     # Test 2: Contact Page
     def test_contact_page(self):
         response = self.app.get('/contact', follow_redirects=True)
         self.assertEqual(response.status_code, 200)
     # Test 3: Nav Page
     def test_navigation_page(self):
         response = self.app.get('/navigation', follow_redirects=True)
         self.assertEqual(response.status_code, 200)
     # Test 4: Review Page
     def test_reviews_page(self):
         response=self.app.get('/reviews', follow_redirects= True)
         self.assertEqual(response.status_code,200)
     # Test 5: Logout Page
         def test_logout_page(self):
             response = self.app.get('/logout', follow_redirects=True)
             self.assertEqual(response.status_code, 200)
     # Test 6: Editor Picks Page
         def test_about_page(self):
             response = self.app.get('/editor-picks', follow_redirects=True)
             self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
