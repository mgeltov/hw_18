from flask import request
from flask_restx import Resource, Namespace

from models import MovieSchema, Movie
from setup_db import db

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies_query = db.session.query(Movie)
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if director_id:
            movies_query = db.session.query(Movie).filter(Movie.director_id == director_id)
        if genre_id:
            movies_query = db.session.query(Movie).filter(Movie.genre_id == genre_id)
        if director_id and genre_id:
            movies_query = db.session.query(Movie).filter(Movie.genre_id == genre_id, Movie.director_id == director_id)
        return movies_schema.dump(movies_query.all()), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)

        return 'New movie is added', 201

@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = db.session.query(Movie).get(mid)
        if not movie:
            return f"There's no movie with id {mid}", 404
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        movie = db.session.query(Movie).get(mid)

        if not movie:
            return f"There's no movie with id {mid}", 404
        movie.title = req_json.get('title')
        movie.description = req_json.get('description')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')

        db.session.add(movie)
        db.session.commit()

        return f"Movie with id {mid} is changed", 204

    def delete(self, mid):
        movie = db.session.query(Movie).get(mid)

        if not movie:
            return f"There's no director with id {mid}", 404

        db.session.delete(movie)
        db.session.commit()

        return f"Movie with id {mid} is deleted", 204