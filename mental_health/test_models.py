from .models.user import User, Post

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username, email, and hashed_password are defined right
    """

new_user1 = User(username="dakaz", email= "dak@dak.com", hash_password="some_hashed_pass")
assert new_user1.username == "dakaz"
assert new_user1.email == "dak@dak.com"
assert new_user1.hash_password == "some_hashed_pass"

def test_new_post():
    """
    GIVEN a Post
    WHEN a new Post is created
    THEN check the username, email, and hashed_password are defined right
    """


new_post1 = Post(type="music", source="youtube", text="this is some dummy text")
assert new_post1.type == "music"
assert new_post1.source == "youtube"
assert new_post1.text == "this is some dummy text"