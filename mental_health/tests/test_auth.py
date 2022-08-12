import json


def test_register(api):
    #converts a python object into a json string
    user_data = json.dumps({'username': "tester", 'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/register', data=user_data, headers=mock_headers)

def test_login(api):
    user_data = json.dumps({'username': "tester",'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/login', data=user_data, headers=mock_headers)

def test_400(api):
    app = api.post('/login')
    assert app.status == '400 BAD REQUEST'

def test_401(api):
    app = api.post('/login')
    user_data = json.dumps({'username': "tester", 'password': ''})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/login', data=user_data, headers=mock_headers)

def test_404(api):
    app = api.get('/dakaz')
    assert app.status == '404 NOT FOUND'