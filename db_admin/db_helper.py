from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import db_admin.db_settings as db_settings
from sqlalchemy.orm import sessionmaker
from db_admin.db_base import Base


class DB_helper():
    global db
    global Session

    db = Base
    Session = sessionmaker()

    def db_connect(self):
        # engine = create_engine("postgresql://postgres:HjkM10wo@localhost/imvb_1", echo=True)
        engine = create_engine(URL(**db_settings.DATABASE))
        Session.configure(bind=engine)
        db.metadata.create_all(engine)

    def get_session(self):
        session = Session()
        return session

