from flask import Blueprint, request
from utility import local
import base64
from api import get_or_create_book, book_operations, new_user

bp = Blueprint('api', __name__, url_prefix='')

bp.add_url_rule('/api/users', 'new_user', new_user, methods=['POST'])
bp.add_url_rule('/api/book', 'get_or_create_book', get_or_create_book, methods=["GET", "POST"])
bp.add_url_rule('/api/book/<int:book_id>', 'book_operations', book_operations, methods=["GET", "PUT", "DELETE"])


@bp.before_request
def before_request():
    title = str(request.form.get('title', ''))
    try:
        decrypted_title = base64.b64decode(bytes(title, 'utf-8'))
        local.title = decrypted_title
    except Exception:
        local.title = title


@bp.after_request
def after_request(response):
    response_data = base64.b64encode(response.data)
    response.data = response_data
    return response



