from application import db
from application.models import Base

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