import os
from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object):
    app = Flask(__name__, instance_path=os.getcwd()) # если убрать instance_path..., то по умолчанию корневым каталогом sqlalchemy будет считать instance
    app.config.from_object(config_object)
    configure_app(app)

    return app

def configure_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)

app = create_app(Config())
app.run()
