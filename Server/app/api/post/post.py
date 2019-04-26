from flask import Blueprint, jsonify, abort, request
from flask_restful import Api, Resource
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)

from app.model.post import *
from app.api import data_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/post'


@api.resource('/<category>')
class ShowAllPost(Resource):
    @jwt_required
    def get(self, category):
        all_post = PostModel.query.filter_by(category=category).all()
        db.session.close()

        return jsonify([{
            'id': post.id,
            'title': post.title
        } for post in all_post])


@api.resource('/write')
class WritePost(Resource):
    @jwt_required
    @data_required(['title', 'content', 'category'])
    def post(self):
        title = request.json['title']
        content = request.json['content']
        category = request.json['category']
        name = get_jwt_identity()

        PostModel(
            title=title,
            content=content,
            category=category,
            name=name
        ).save()

        return "", 201


@api.resource('/<category>/<int:idx>')
class OnePost(Resource):
    @jwt_required
    def get(self, category, idx):
        post = PostModel.query.filter_by(category=category, id=idx).first()
        db.session.close()

        if not post:
            abort(406)

        return jsonify([{
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'name': post.name
        }])

    @jwt_required
    @data_required(['title', 'content'])
    def put(self, category, idx):
        title = request.json['title']
        content = request.json['content']
        re_category = request.json['category']

        user = get_jwt_identity()
        post = PostModel.query.filter_by(category=category, id=idx).first()

        if not post:
            abort(406)

        if user != post.name:
            abort(403)

        post.title = title
        post.content = content

        if re_category:
            post.category = re_category

        post.commit()

        return "", 201

    @jwt_required
    def delete(self, category, idx):
        user = get_jwt_identity()
        post = PostModel.query.filter_by(category=category, id=idx).first()

        if not post:
            abort(406)

        if user != post.name:
            abort(403)

        post.delete()

        return "", 201
