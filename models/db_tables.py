from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime as dt
from db_admin.db_base import Base

db = Base

class Divisions(db):

    __tablename__ = 'divisions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    staff = relationship("Staff",back_populates='division',cascade='all,delete,delete-orphan')

    def __init__(self, name):
        self.name = name


class Staff(db):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    surname = Column(String)
    inn = Column(Integer)

    division_id = Column(Integer,ForeignKey('divisions.id'))

    division = relationship("Divisions",back_populates='staff') # divisions

    def __init__(self, name, fullname, surname, inn):

        self.name = name
        self.fullname = fullname
        self.surname = surname
        self.inn = inn

class QuitSheets(db):
    __tablename__ = 'quitsheets'
    id = Column(Integer,primary_key=True)
    date_create = Column(TIMESTAMP)
    user_create = Column(Integer)
    employee = Column(Integer)
    division = Column(Integer)
    reason_employee = Column(String)
    reason_hr = Column(String)

    signs = relationship("Signs",back_populates='quitsheet')

    def __init__(self, id, date_create, user_create, employee, division, reason_employee, reason_hr):
        self.date_create = date_create
        self.user_create = user_create
        self.employee = employee
        self.division = division
        self.reason_employee = reason_employee
        self.reason_hr = reason_hr

class Signs(db):
    __tablename__ = 'signs'
    id = Column(Integer,primary_key=True)
    staff = Column(Integer)
    role = Column(Integer)
    date = Column(TIMESTAMP)
    comment = Column(String)

    quitsheet_id = Column(Integer,ForeignKey("quitsheets.id"))

    quitsheet = relationship('Quitsheets',back_populates='signs')

    def __init__(self,staff,role,date,comment):
        self.staff = staff
        self.role = role
        self.date = date
        self.comment = comment

class Roles(db):
    __tablename__ = 'roles'
    id = Column(Integer,primary_key=True)
    name = Column(String(200))