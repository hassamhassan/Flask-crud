
from flask import jsonify, request, g, abort, url_for
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    from models import Book, User
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


def new_user():
    """
    This method is used to add new user to the system.
    And user added from here will be used in authentication for api calls.

    :return: JSON response containing user added and its URI
    """
    from instance import db
    from models import User
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        abort(400)
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201, {'Location': url_for('api.new_user', id=user.id, _external=True)}


@auth.login_required
def get_or_create_book():
    """
    This method handles the api calls for creating a new book via POST or returning all the books via GET
    :return: Encoded JSON response
    """
    from models import Book
    from utility import local
    if request.method == "POST":
        title = local.title
        if title:
            book = Book(title=title)
            book.save()
            response = jsonify({'id': book.id, 'title': book.title})
            response.status_code = 201
            return response
        else:
            response = jsonify({'error': "title is required.", 'status_code': 400})
            return response
    else:
        books = Book.query.all()
        results = []
        for book in books:
            obj = {'id': book.id, 'title': book.title}
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response


@auth.login_required
def book_operations(book_id):
    """
    This method handles the api calls for PUT, DELETE and GET operations on a single book object
    :param book_id:
    :return: Encoded JSON response
    """
    from instance import db
    from models import Book
    book = Book.query.filter_by(id=book_id).first()
    if not book:
        return jsonify({"message": "book not found", "status_code": 404})

    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "book '{}' deleted successfully".format(book.title),
                        "status_code": 200})

    elif request.method == 'PUT':
        title = str(request.form.get('title', ''))
        if not title:
            response = jsonify({'error': "title is required.", 'status_code': 400})
            return response
        book.title = title
        book.save()
        response = jsonify({'id': book.id, 'title': book.title})
        response.status_code = 200
        return response

    elif request.method == 'GET':
        response = jsonify({'id': book.id, 'title': book.title})
        response.status_code = 200
        return response

    else:
        return jsonify({"message": "invalid request", "status_code": 400})

