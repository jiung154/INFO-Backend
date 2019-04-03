def blueprint(app):
    from .account import account_blueprint
    app.register_blueprint(account_blueprint)
