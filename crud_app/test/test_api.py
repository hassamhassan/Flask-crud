# import requests
import pytest
from flask import url_for
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
#
#
# def test_book_creation(client):
#     """Test API can create a book (POST request)"""
#     data = {"title": "12 years a slave"}
#     res = client.post('/api/book', data=data,
#                        headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})
#     # assertEqual(res.status_code, 201)
#     assert'12 years a slave' in b64decode(res.text.encode()).decode()

class TestBook(object):
    def test_api_can_get_all_books(app, client):
        """Test API can get a books (GET request)."""
        """Test API can create a book (POST request)"""

        res = client.post('/api/book',
                          headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})
        assert 'History of Mughals' in b64decode(res.text.encode()).decode()

#
# def test_api_can_get_book_by_id(client):
#     """Test API can get a single book by using it's id."""
#     """Test API can create a book (POST request)"""
#     res = client.get('http://127.0.0.1:5000/api/book/2',
#                        headers={"Authorization": "Basic {user}".format(user=b64encode(b"hassam:123456").decode())})
#     # assertEqual(res.status_code, 201)
#     assert 'History of Mughals' in b64decode(res.text.encode()).decode()

#
# def test_book_can_be_edited(self):
#     """Test API can edit an existing book. (PUT request)"""
#     rv = self.client().post('/api/book/', data={'name': 'test book title'})
#     self.assertEqual(rv.status_code, 201)
#     rv = self.client().put('/api/book/1', data={"title": "new test book title"})
#     self.assertEqual(rv.status_code, 200)
#     results = self.client().get('/api/book/1')
#     self.assertIn('new test book title', str(results.data))
#
#
# def test_book_deletion(self):
#     """Test API can delete an existing book. (DELETE request)."""
#     rv = self.client().post('/api/book/', data={'name': 'test book title'})
#     self.assertEqual(rv.status_code, 201)
#     res = self.client().delete('/api/book/1')
#     self.assertEqual(res.status_code, 200)
#     # Test to see if it exists, should return a 404
#     result = self.client().get('/api/book/1')
#     self.assertEqual(result.status_code, 404)

#
# def tearDown(self):
#     """teardown all initialized variables."""
#     with self.app.app_context():
#         # drop all tables
#         self.db.session.remove()


# Make the tests conveniently executable
# if __name__ == "__main__":
#     unittest.main()
