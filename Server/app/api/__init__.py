from functools import wraps
from flask import request, abort


def data_required(key):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for i in key:
                if i not in request.json:
                    abort(400)
            return f(*args, **kwargs)
        return wrapper
    return decorator


def blueprint(app):
    from app.api.account import account
    app.register_blueprint(account.api.blueprint)

    from app.api.post import post
    app.register_blueprint(post.api.blueprint)

