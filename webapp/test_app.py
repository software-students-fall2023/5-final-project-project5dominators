import pytest
from app import app as flask_app
from bson import ObjectId
import json


@pytest.fixture
def app():
    app = flask_app
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


# Mocking MongoDB Connection
class MockedMongoClient:
    def __init__(self, *args, **kwargs):
        pass

    @property
    def SnapChat(self):
        return self

    @property
    def User(self):
        return self

    @property
    def communication(self):
        return self

    def find_one(self, *args, **kwargs):
        return {'_id': ObjectId(), 'username': 'testuser'}

    def insert_one(self, *args, **kwargs):
        return type('obj', (object,), {'inserted_id': ObjectId()})

    def find(self, *args, **kwargs):
        return iter([{'_id': ObjectId(), 'username': 'testuser', 'message': 'test', 'timestamp': '2023-12-19'}])

    def delete_one(self, *args, **kwargs):
        pass


@pytest.fixture
def mocked_mongo(monkeypatch):
    monkeypatch.setattr('app.MongoClient', MockedMongoClient)


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'login' in response.data


def test_login(client, mocked_mongo):
    response = client.post('/login', data={'username': 'testuser'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'index' in response.data


def test_main(client, mocked_mongo):
    client.post('/login', data={'username': 'testuser'}, follow_redirects=True)
    response = client.get('/main')
    assert response.status_code == 200
    assert b'index' in response.data


def test_get_messages(client, mocked_mongo):
    response = client.get('/get_messages')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)


def test_delete_message(client, mocked_mongo):
    response = client.post('/delete_message/507f1f77bcf86cd799439011', follow_redirects=True)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'


def test_post_message(client, mocked_mongo):
    with client:
        client.post('/login', data={'username': 'testuser'}, follow_redirects=True)
        response = client.post('/post_message', data={
            'message': 'Hello, world!',
            'image': BASE64_IMAGE
        })
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'message' in data
        assert data['message'] == 'Hello, world!'

