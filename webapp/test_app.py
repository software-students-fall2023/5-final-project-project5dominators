import pytest
from app import app as flask_app
from bson import ObjectId
import json


BASE64_IMAGE = "data:image/png;base64," \
               "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"


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


def test_convert_to_sketch(client, mocked_mongo):
    with client:
        client.post('/login', data={'username': 'testuser'}, follow_redirects=True)
        response = client.post('/convert_to_sketch', data={
            'message': 'Sketch me!',
            'image': BASE64_IMAGE
        })
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'message' in data
        assert data['message'] == 'Sketch me!'
        assert 'photo' in data
        assert data['photo'].startswith('data:image/jpeg;base64,')


def test_convert_to_cartoon(client, mocked_mongo):
    with client:
        client.post('/login', data={'username': 'testuser'}, follow_redirects=True)
        response = client.post('/convert_to_cartoon', data={
            'message': 'Cartoonize me!',
            'image': BASE64_IMAGE
        })
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'message' in data
        assert data['message'] == 'Cartoonize me!'
        assert 'photo' in data
        assert data['photo'].startswith('data:image/jpeg;base64,')



