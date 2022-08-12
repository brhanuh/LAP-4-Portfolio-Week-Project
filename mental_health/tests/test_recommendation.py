def test_home(api):
    """connects viewing all posts without logging in route"""
    app = api.get('/recommendations/')
    assert app.status == '401 UNAUTHORIZED'
    