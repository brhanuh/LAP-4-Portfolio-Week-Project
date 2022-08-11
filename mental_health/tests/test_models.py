from flask import Flask
import unittest

from ..database.db import db
from ..models.user import User

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

    def test_user_create(self):

        user_test_1 = User(username="test_usernames",email="user_emails", hash_password="test_passwords")
        db.session.add(user_test_1)
        db.session.commit()

if __name__ == "__main__":
    unittest.main()