from ..database import db_session


class CRUD(object):
    def create(self):
        db_session.add(self)
        db_session.commit()
        return self

    def delete(self):
        self.deleted = True
        db_session.commit()
        return self

    def save_changes(self):
        db_session.commit()
        return self
