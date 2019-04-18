from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# local import
from instance.config import app_config

# initialize sql-alchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    from routes import bp
    app.register_blueprint(bp)
    return app


from create_app import app

if __name__ == '__main__':
    app.run()
