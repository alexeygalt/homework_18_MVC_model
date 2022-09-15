from flask_restx import Resource, Namespace
from flask import request, abort

from dao.model.genre import genres_schema, genre_schema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200

    def post(self):
        upload_data = request.get_json()
        genre_service.create(upload_data)
        return "", 201


@genres_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        if genre_service.get_one(gid):
            return genre_schema.dump(genre_service.get_one(gid)), 200
        return f'Genre {gid} not found', 404

    def put(self, gid):
        upload_data = request.get_json()
        if not upload_data.get('id'):
            upload_data['id'] = gid
        if genre_service.update(upload_data):
            return f'Director {gid} updated', 201
        return f'Genre {gid} not found', 404

    def delete(self, gid):
        if genre_service.delete(gid):
            return "", 204
        return f'Genre {gid} not found', 404
