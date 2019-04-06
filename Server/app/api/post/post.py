from flask import jsonify, abort, request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)

from app.model.post import *
from app.api import data_required


class ShowAllPost(Resource):
    def get(self, category):
        all_post = PostModel.query.filter_by(category=category).all()
        db.session.close()

        return jsonify([{
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'name': post.name
        } for post in all_post])


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

        user = get_jwt_identity()
        post = PostModel.query.filter_by(category=category, id=idx).first()

        if not post:
            abort(406)

        if user != post.name:
            abort(403)

        post.title = title
        post.content = content

        db.session.commit()
        db.session.close()

        return "", 201

    @jwt_required
    def delete(self, category, idx):
        user = get_jwt_identity()
        post = PostModel.query.filter_by(category=category, id=idx).first()

        if not post:
            abort(406)

        if user != post.name:
            abort(403)

        db.session.delete(post)
        db.session.commit()
        db.session.close

        return "", 200
