from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    role = Column(String, default="user")  # Default role is 'user'