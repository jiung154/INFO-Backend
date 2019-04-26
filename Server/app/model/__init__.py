from run import db


class BaseModel:
    def commit(self):
        db.session.commit()
        db.session.close()

    def save(self):
        db.session.add(self)
        self.commit()

    def delete(self):
        db.session.delete(self)
        self.commit()
