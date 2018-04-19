from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    memos = db.relationship("Memo", backref='account', lazy=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),
                        nullable=False)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.role_id = 1
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    

    @staticmethod
    def find_users_no_memos():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Memo ON Memo.account_id = Account.id"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Memo.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response