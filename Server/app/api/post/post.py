from flask import jsonify, abort
from flask_restful import Resource

from app.model.post import *


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
