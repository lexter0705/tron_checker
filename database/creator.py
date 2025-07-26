from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class RequestTable(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    ip_address = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    tron_address = Column(String, nullable=False)