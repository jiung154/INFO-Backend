from werkzeug.security import generate_password_hash

from app.model import BaseModel
from app.extension import db


class AccountModel(db.Model, BaseModel):
    __tablename__ = 'user'

    id = db.Column(
        db.String(100),
        unique=True,
        nullable=False,
        primary_key=True
    )

    pw = db.Column(
        db.String(200),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    def __init__(self, id, pw, name):
        self.id = id
        self.name = name

        self.password_hash(pw)

    def password_hash(self, pw):
        self.pw = generate_password_hash(pw)
