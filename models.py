from sqlalchemy import Column, Text, Integer
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    password = Column(Text)


class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    