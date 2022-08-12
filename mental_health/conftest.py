import pytest
from mental_health import app
# from .models.entry import Entry
from .models.user import User, Post

# @pytest.fixture
# def api(monkeypatch):
#     test_entries = [ 
#     { "date_posted": "08-08-2022", "mood": 5, "energy": 5, "depression": 1, "irritability": 1, "motivation": 1, "stress": 1, "appetatite": 5, "concentration": 5, "diet": "pizza and coke", "enter": "netflix", "social": "facebook, insta, snap" }, 
#     { "date_posted": "08-08-2022", "mood": 5, "energy": 5, "depression": 1, "irritability": 1, "motivation": 1, "stress": 1, "appetatite": 5, "concentration": 5, "diet": "pizza and coke", "enter": "netflix", "social": "facebook, insta, snap" },
#     { "date_posted": "08-08-2022", "mood": 5, "energy": 5, "depression": 1, "irritability": 1, "motivation": 1, "stress": 1, "appetatite": 5, "concentration": 5, "diet": "pizza and coke", "enter": "netflix", "social": "facebook, insta, snap" },
#     { "date_posted": "08-08-2022", "mood": 5, "energy": 5, "depression": 1, "irritability": 1, "motivation": 1, "stress": 1, "appetatite": 5, "concentration": 5, "diet": "pizza and coke", "enter": "netflix", "social": "facebook, insta, snap" }, 
#     { "date_posted": "08-08-2022", "mood": 1, "energy": 5, "depression": 1, "irritability": 1, "motivation": 1, "stress": 1, "appetatite": 5, "concentration": 5, "diet": "pizza and coke", "enter": "netflix", "social": "facebook, insta, snap" } 
#     ]
#     api = main_routes.app.test_client()
#     return api


@pytest.fixture
def api():
    client = app.test_client()
    return client

@pytest.fixture(scope = 'module')
def new_user():
    test_user = User(username="test_usernames",email="user_emails", hash_password="test_passwords")
    return test_user


