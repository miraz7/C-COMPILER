import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import UserMixin


Base = declarative_base()


class Users(Base,UserMixin):
    __tablename__ = 'Users'

    UserIDNumber = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    FullName = Column(String(30), nullable=False)
    Username = Column(String(15), nullable=False, unique=True)
    UserType = Column(String(10), nullable=False)
    EmailAddress = Column(String(40), nullable=False)
    Password = Column(String(25), nullable=False)


    def get_id(self):
        return self.UserIDNumber


#Always stay at the end of the file
engine = create_engine('sqlite:///classroom.db')
Base.metadata.create_all(engine)
