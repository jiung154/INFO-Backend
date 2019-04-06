from flask import request, abort
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_refresh_token_required, get_jwt_identity
)
from werkzeug.security import (
    check_password_hash, generate_password_hash
)
from app.api import data_required
from app.model.account import *


class LoginUser(Resource):
    @data_required(['id', 'pw'])
    def post(self):
        user_id = request.json['id']
        user_pw = request.json['pw']

        user = AccountModel.query.filter_by(id=user_id).first()
        db.session.close()

        if not user:
            abort(406)

        if not check_password_hash(user.pw, user_pw):
            abort(406)

        return {
            'access_token': create_access_token(identity=user_id),
            'refresh_token': create_refresh_token(identity=user_id)
        }, 200


class RegisterUser(Resource):
    @data_required(['id', 'pw', 'name'])
    def post(self):
        user_id = request.json['id']
        user_pw = request.json['pw']
        user_name = request.json['name']

        if AccountModel.query.filter_by(id=user_id).first():
            abort(409)

        hash_pw = generate_password_hash(user_pw)

        user = AccountModel(
            id=user_id,
            pw=hash_pw,
            name=user_name
        )

        db.session.add(user)
        db.session.commit()
        db.session.close()

        return "", 200


class RefreshToken(Resource):
    @jwt_refresh_token_required
    def post(self):
        user = get_jwt_identity()

        return {
            'access_token': create_access_token(identity=user)
        }
