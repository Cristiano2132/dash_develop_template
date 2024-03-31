from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship



class User(SQLModel, table=True):
    """ Represents the User model"""
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: str
