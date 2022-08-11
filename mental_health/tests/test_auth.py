from flask import Flask
import unittest
import requests
from ..database.db import db

class appDBTests(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()

# functional tests
    

class ApiTest(unittest.TestCase):
    api_url = "http://127.0.0.1:5000"
    register_url = "{}/register".format(api_url)
    login_url = "{}/login".format(api_url)

    register_obj = {
        "id": 100,
        "username": "boom",
	    "email": "boom@gmail.com",
	    "password": "boomba"
    }

    login_obj = {
        "username": "baz",
        "password": "bak"
    }

    def test_register_get(self):
        req = requests.get(ApiTest.register_url)
        self.assertEqual(req.status_code, 405)

    def test_register_post(self):
        reqs = requests.post(ApiTest.register_url, json = ApiTest.register_obj)
        self.assertEqual(reqs.status_code, 201)

    def test_login(self):
        reqs = requests.post(ApiTest.login_url, json = ApiTest.login_obj)
        self.assertEqual(reqs.status_code, 200)

if __name__ == "__main__":
     unittest.main()