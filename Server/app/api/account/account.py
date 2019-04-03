from flask import request, abort, session
from flask_restful import Resource
from werkzeug.security import check_password_hash

from Server.app.model.account import *


class LoginUser(Resource):
    def post(self):
        try:
            user_id = request.json['id']
            user_pw = request.json['pw']
        except KeyError:
            abort(400)

        user = AccountModel.query.filter_by(id=user_id).first()
        db.session.close()

        if not user:
            abort(406)

        if not check_password_hash(user.pw, user_pw):
            abort(406)

        session['id'] = user_id

        return "", 200
