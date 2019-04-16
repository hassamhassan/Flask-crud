from api import get_or_create_book, book_operations, new_user
from views import home, delete, update
from create_app import app

app.add_url_rule('/', 'home', home, methods=["GET", "POST"])
app.add_url_rule('/update', 'update', update, methods=["GET", "POST"])
app.add_url_rule('/delete', 'delete', delete, methods=["GET", "POST"])
app.add_url_rule('/api/users', 'new_user', new_user, methods=['POST'])

app.add_url_rule('/api/book', 'get_or_create_book', get_or_create_book, methods=["GET", "POST"])
app.add_url_rule('/api/book/<int:book_id>', 'book_operations', book_operations, methods=["GET", "PUT", "DELETE"])


if __name__ == '__main__':
    app.run()


