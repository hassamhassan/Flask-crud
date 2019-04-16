import base64
from create_app import app
from flask import request

from werkzeug.local import Local, LocalManager

local = Local()
local_manager = LocalManager([local])


@app.before_request
def before_request():
    title = str(request.form.get('title', ''))
    try:
        decrypted_title = base64.b64decode(bytes(title, 'utf-8'))
        local.title = decrypted_title
    except Exception:
        local.title = title


@app.after_request
def after_request(response):
    response_data = base64.b64encode(response.data)
    response.data = response_data
    return response