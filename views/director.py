from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import directors_schema, director_schema
from implemented import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_all()), 200

    def post(self):
        upload_data = request.get_json()
        director_service.create(upload_data)
        return "", 201


@directors_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did):
        if director_service.get_one(did):
            return director_schema.dump(director_service.get_one(did)), 200
        return f'Director {did} not found', 404

    def put(self, did: int):
        upload_data = request.get_json()
        if not upload_data.get('id'):
            upload_data['id'] = did
        if director_service.update(upload_data):
            return f'Director {did} updated', 201
        return f'Director {did} not found', 404

    def delete(self, did: int):
        if director_service.delete(did):
            return "", 204
        return f'Director {did} not found', 404
