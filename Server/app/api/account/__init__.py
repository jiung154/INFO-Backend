from flask import Blueprint
from flask_restful import Api

account_blueprint = Blueprint('account', __name__)
api = Api(account_blueprint)
api.prefix = '/account'

from .account import LoginUser
api.add_resource(LoginUser, '/login')
