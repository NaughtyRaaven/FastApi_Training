from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    model_config = ConfigDict(
        from_attributes=True
    )  # convert sqlalchemy model to pydantic model

    id: int
    created_at: datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )  # convert sqlalchemy model to pydantic model

    id: int
    email: EmailStr
    created_at: datetime
