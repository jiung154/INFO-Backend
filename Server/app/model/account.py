from Server.run import db


class AccountModel(db.Model):
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
