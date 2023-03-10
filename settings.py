from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# DB Settings.
DB_USER = "root"
DB_PASSWORD = "abhi123"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "starletteauth"
db_url = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()
engine = create_engine(db_url, echo=True)
Session = sessionmaker(engine)
session = Session()