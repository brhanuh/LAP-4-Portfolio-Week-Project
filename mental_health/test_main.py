import json, requests
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required
from os import access
from urllib import response
import unittest
from . import app

class Flask(unittest.TestCase):

    API_URL = ""
    
    
    def test_my_profile(self):
        tester = app.test_client(self)
        access_token = create_access_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MDA1MjY1NiwianRpIjoiMDFiODM5ZWYtNzRlZS00NDBlLWJiZjktYmI1MGZiMzAwNjIzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImhvbGFob3BlIiwibmJmIjoxNjYwMDUyNjU2LCJleHAiOjE2NjAwNTYyNTZ9.HG6tIyR3v8X4eSsszAyLv7Qe2LvPizOpM0g8edbF6h8')
        headers = {
            'authorization': 'Bearer'.format(access_token)
        }
        response = tester.get("/profile")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(b'Nagato' in response.data)

    def test_get_entries(self):
        tester = app.test_client(self)
        response = tester.get("/entries")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(b'mood' in response.data)
        self.assertTrue(b'date' in response.data)

    def test_get_target_entry(self):
        tester = app.test_client(self)
        response = tester.get("/entry/mood/5")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(b'5' in response.data)
        self.assertTrue(b'mood' in response.data)
    
    def test_get_statistics(self):
        tester = app.test_client(self)
        response = tester.get("/stats/appetite/3")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(b'level of appetite' in response.data)


if __name__ == "__main__":
    unittest.main()