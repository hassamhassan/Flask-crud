from instance import db
from flask import request, render_template, redirect
from models import Book


def home():
    """
    This function loads the home page where user can add/remove and view the books.
    :return: HTTP response
    """
    if request.form:
        book = Book(title=request.form.get("title"))
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    return render_template("home.html", books=books)


def update():
    """
    This function is used to update the existing book
    :return: Redirects to main page
    """
    new_title = request.form.get("title")
    book_id = request.form.get("book_id")
    book = Book.query.get(book_id)
    book.title = new_title
    db.session.commit()
    return redirect("/")


def delete():
    """
    This function is used to delete the book
    :return: Redirects to main page
    """
    book_id = request.form.get("book_id")
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


