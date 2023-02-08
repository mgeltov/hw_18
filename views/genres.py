from flask_restx import Resource, Namespace

from models import Genre, GenreSchema
from setup_db import db


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres), 200
