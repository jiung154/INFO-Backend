from flask import Blueprint
from flask_restful import Api

post_blueprint = Blueprint('post', __name__)
api = Api(post_blueprint)
api.prefix = '/post'

from .post import ShowAllPost
api.add_resource(ShowAllPost, '/<category>')

from .post import OnePost
api.add_resource(OnePost, '/<category>/<int:idx>')
