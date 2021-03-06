from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

"""
class MyModel(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    username = Column(Text)
    password = Column(Text)

class MyModel1(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    username = Column(Text)
    password = Column(Text)


Index('my_index', MyModel.username, unique=True, mysql_length=255)
#Index('my_index1', MyModel1.username, unique=True, mysql_length=255)
"""
