from application import db
from application.models import Base

from sqlalchemy.sql import text

class Role(Base):

    __tablename__ = "role"

    name = db.Column(db.String(144), nullable=False)
    users = db.relationship("User", backref='role', lazy=True)

    def __init__(self, name):
        self.name = name
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True