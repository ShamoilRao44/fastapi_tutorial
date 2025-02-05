import email
from sqlalchemy import TIMESTAMP, Column, Integer, Boolean, String, false, null, text
from .database import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable= False)
    published = Column(Boolean, server_default=text('TRUE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

class User(Base):
    __tablename__ = "users"

    u_id=Column(Integer, primary_key=True, nullable=False)
    email=Column(String, nullable=False, unique=True)
    password=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()')) 