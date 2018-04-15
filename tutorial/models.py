
from sqlalchemy import (
    Column,
    Integer,
    Text,
    )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
    )
from zope.sqlalchemy import ZopeTransactionExtension
Session = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
Base = declarative_base()





class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    lname = Column(Text)
    jensiyat = Column(Text)
    phone = Column(Text)
    email = Column(Text)
    address = Column(Text)
    username = Column(Text)
    password = Column(Text)

class Product(Base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    Pname = Column(Text)
    description = Column(Text)
    price = Column(Text)
    state = Column(Text)
    pic = Column(Text)

class Root(object):
    def __init__(self, request):
        pass
    def tutorial ():
        pass
