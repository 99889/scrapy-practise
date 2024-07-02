# models.py
from sqlalchemy import create_engine, Column, Integer, String, Text, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quotes_tb'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    author = Column(String(255))
    tag = Column(Text)


#DATABASE_URL = ''

# engine = create_engine(DATABASE_URL)
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
