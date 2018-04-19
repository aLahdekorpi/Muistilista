from application import db
from application.models import Base

from sqlalchemy.sql import text

class Memo(Base):

    name = db.Column(db.String(144), nullable=False)
    importance = db.Column(db.Integer, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                        nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))                    

    def __init__(self, name):
        self.name = name
        self.importance = 0
        self.category_id = 99

    @staticmethod
    def delete_memo(memo_id):
        stmt = text('DELETE FROM Memo WHERE id = :memo_id').params(memo_id = memo_id)
        db.engine.execute(stmt)

        return "deleted"