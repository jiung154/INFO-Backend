from flask import abort, current_app, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import os


class ImageUpload(Resource):
    @jwt_required
    def post(self):
        try:
            image = request.files['image']
        except ValueError:
            abort(400)

        try:
            filename = image.filename
            file_path = os.path.join(
                current_app.config['UPLOAD_FOLDER'], filename
            )

            image.save(file_path)
        except FileNotFoundError:
            abort(406)

        return '', 200
