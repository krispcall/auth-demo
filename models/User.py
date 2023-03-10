from settings import Base, engine
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    username = Column(String(), unique=True)
    email = Column(String())
    password = Column(String())

    def __repr__(self):
        return f"<User {self.username}>"