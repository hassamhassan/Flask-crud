import pytest
import json
from instance import create_app
from base64 import b64encode, b64decode


@pytest.fixture
def app(request):

    config_name = "testing"
    app = create_app(config_name)
    app.config['SERVER_NAME'] = 'localhost'
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_book_creation(client):
    """Test API can create a book (POST request)"""

    res = client.post('/api/book',
                      headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())},
                      data={'title': 'test book title'})
    res_dict = json.loads(b64decode(res.data).decode())
    assert 'test book title' == res_dict.get('title')
    client.delete('/api/book/'+str(res_dict.get('id')),
                  headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})


def test_api_can_get_all_books(client):
    """Test API can get a books (GET request)."""
    res1 = client.post('/api/book',
                       headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())},
                       data={'title': 'test book title1'})
    res2 = client.post('/api/book',
                       headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())},
                       data={'title': 'test book title2'})
    res3 = client.get('/api/book',
                      headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})

    res_dict1 = json.loads(b64decode(res1.data).decode())
    res_dict2 = json.loads(b64decode(res2.data).decode())
    res3 = b64decode(res3.data).decode()

    assert 'test book title1' in res3
    assert 'test book title2' in res3

    client.delete('/api/book/' + str(res_dict1.get('id')),
                  headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})

    client.delete('/api/book/' + str(res_dict2.get('id')),
                  headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})


def test_api_can_get_book_by_id(client):
    """Test API can get a single book by using it's id."""

    res1 = client.post('/api/book',
                       headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())},
                       data={'title': 'test book title1'})
    res_dict1 = json.loads(b64decode(res1.data).decode())

    res = client.get('/api/book/' + str(res_dict1.get('id')),
                     headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})
    res = b64decode(res.data).decode()
    assert 'test book title1' in res

    client.delete('/api/book/' + str(res_dict1.get('id')),
                  headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})


def test_book_can_be_edited(client):
    """Test API can edit an existing book. (PUT request)"""
    res1 = client.post('/api/book',
                       headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())},
                       data={'title': 'test book title1'})
    res_dict1 = json.loads(b64decode(res1.data).decode())

    res = client.put('/api/book/' + str(res_dict1.get('id')),
                     headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())},
                     data={'title': 'test book title2'})
    res = b64decode(res.data).decode()
    assert 'test book title2' in res

    client.delete('/api/book/' + str(res_dict1.get('id')),
                  headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})

