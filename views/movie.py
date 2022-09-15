from flask_restx import Resource, Namespace
from flask import request, abort
from dao.model.movie import movies_schema, movie_schema
from implemented import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesVies(Resource):
    def get(self):
        key = request.args
        return movies_schema.dump(movie_service.get_all(key)), 200

    def post(self):
        upload_data = request.get_json()
        movie_service.create(upload_data)
        return "", 201


@movies_ns.route('/<int:mid>')
class MoviesVies(Resource):
    def get(self, mid):
        if movie_service.get_one(mid):
            return movie_schema.dump(movie_service.get_one(mid)), 200
        return f'Movie {mid} not found', 404

    def put(self, mid):
        upload_data = request.get_json()
        if not upload_data.get('id'):
            upload_data['id'] = mid
        if movie_service.update(upload_data):
            return f'Movie {mid} updated', 201
        return f'Movie {mid} not found', 404

    def patch(self, mid):
        upload_data = request.get_json()
        if not upload_data.get('id'):
            upload_data['id'] = mid
        if movie_service.update_partial(upload_data):
            return f'Movie {mid} updated', 201
        return f'Movie {mid} not found', 404

    def delete(self, mid):
        if movie_service.delete(mid):
            return "", 204
        return f'Movie {mid} not found', 404
