from sqlalchemy import Column, Integer, String, DateTime
from core.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String, index=True)
    email = Column(String)
    hash_password = Column(String)
    register_date = Column(DateTime)
