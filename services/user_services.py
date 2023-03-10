
from settings import *
from models.User import User
import bcrypt

def create_user(username, email, password):
    salt = bcrypt.gensalt()
    hashedpwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    new_user = User(username = username, email = email, password = hashedpwd)
    session.add(new_user)
    session.commit()
    return new_user

def loginUser (username, password):
    user = session.query(User).filter(User.username==username).first()
    return user