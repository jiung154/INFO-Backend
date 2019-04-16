from flask import jsonify, abort, request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)

from app.model.post import *
from app.api import data_required


class ShowAllPost(Resource):
    @jwt_required
    def get(self, category):
        all_post = PostModel.query.filter_by(category=category).all()
        db.session.close()

        return jsonify([{
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'name': post.name
        } for post in all_post])


class TitleAndId(Resource):
    @jwt_required
    def get(self, category):
        all_post = PostModel.query.filter_by(category=category).all()
        db.session.close()

        return jsonify([{
            'id': post.id,
            'title': post.title
        } for post in all_post])


class WritePost(Resource):
    @jwt_required
    @data_required(['title', 'content', 'category'])
    def post(self):
        title = request.json['title']
        content = request.json['content']
        category = request.json['category']
        name = get_jwt_identity()

        post = PostModel(
            title=title,
            content=content,
            category=category,
            name=name
        )

        db.session.add(post)
        db.session.commit()
        db.session.close()

        return "", 201


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
