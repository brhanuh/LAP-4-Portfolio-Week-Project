import json, requests
from urllib import response
import unittest
from . import app

class Flask(unittest.TestCase):

    API_URL = ""

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(b'db' in response.data)

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