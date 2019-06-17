from app.model import BaseModel
from app.extension import db


class PostModel(db.Model, BaseModel):
    __tablename__ = 'post'

    id = db.Column(
        db.Integer,
        nullable=False,
        primary_key=True
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    content = db.Column(
        db.String(200),
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    def __init__(self, title, content, category, name):
        self.title = title
        self.content = content
        self.category = category
        self.name = name
