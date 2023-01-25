# from schematics.models import Model
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class PostFilmSchema(BaseModel):
    film_name: str = Field(default=None)
    author: str = Field(default=None)
    production_year: int = Field(default=None)
    film_length: int = Field(default=None)
    when_to_watch: str = Field(default=None)
    film_description: str = Field(default=None)


class UserSchema(BaseModel):
    fullName: str = Field(default=None)
    password: str = Field(default=None)
    email: str = Field(default=None)


class UserLoginSchema(BaseModel):
    password: str = Field(default=None)
    email: str = Field(default=None)
