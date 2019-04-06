from run import db


class PostModel(db.Model):
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

    name = db.Column(
        db.String(100),
        nullable=False
    )
