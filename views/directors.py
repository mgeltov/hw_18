from flask_restx import Resource, Namespace

from models import Director, DirectorSchema
from setup_db import db


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors), 200
