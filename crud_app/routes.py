from flask import Blueprint


from api import get_or_create_book, book_operations, new_user

bp = Blueprint('api', __name__, url_prefix='')

bp.add_url_rule('/api/users', 'new_user', new_user, methods=['POST'])
bp.add_url_rule('/api/book', 'get_or_create_book', get_or_create_book, methods=["GET", "POST"])
bp.add_url_rule('/api/book/<int:book_id>', 'book_operations', book_operations, methods=["GET", "PUT", "DELETE"])




