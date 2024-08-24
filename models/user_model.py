from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    active = Column(Boolean, default=True)
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())
