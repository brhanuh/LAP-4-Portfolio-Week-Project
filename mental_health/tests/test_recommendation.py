from ..models.user import User
import unittest
import requests


# functional tests
    

class ApiTest(unittest.TestCase):
    api_url = "http://127.0.0.1:5000/recommendations"
    viewall_url = "{}".format(api_url)
    post_url = "{}/post".format(api_url)

    post_obj = {
        "type": "music",
	    "source": "from google",
	    "text": "boomba is amazing"
    }


    def test_get_allposts(self):
        req = requests.get(ApiTest.viewall_url)
        self.assertEqual(req.status_code, 401)

    def test_user_post(self):
        reqs = requests.post(ApiTest.post_url, json = ApiTest.post_obj)
        self.assertEqual(reqs.status_code, 401)

    def test_post_by_user(self):
        username = "dak"
        reqs = requests.get("{}/{}".format(ApiTest.post_url, username), json = ApiTest.post_obj)
        self.assertEqual(reqs.status_code, 401)
