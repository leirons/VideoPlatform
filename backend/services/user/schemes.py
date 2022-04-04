from typing import Optional, Union

from pydantic import BaseModel, validator, ValidationError

from .validate import validate_email


class UserBase(BaseModel):
    email: str

    @validator("email")
    def validate_email(cls, email):
        if validate_email(email):
            return email
        return ValidationError("Email does not correct")


class UserCreate(UserBase):
    password: str
    login: str

    @validator("login")
    def validate_login(cls, login):
        if len(login) > 30:
            return ValidationError("Login should not have more then 30 symbols ")
        return login


class User(UserBase):
    id: int
    login: str
    hash_password: str

    class Config:
        orm_mode = True


class UserPatch(BaseModel):
    login: Optional[Union[str, None]] = None
    email: Optional[Union[str, None]] = None
    password: Optional[Union[str, None]] = None

    @validator("login")
    def validate_login(cls, login):
        if len(login) > 30 and login is not None:
            return ValidationError("Login should not have more then 30 symbols ")
        return login

    @validator("email")
    def validate_email(cls, email):
        if email is None:
            return email
        if validate_email(email):
            return email
        return ValidationError("Email does not correct")


class UserToken(BaseModel):
    password: str
    login: str

    class Config:
        orm_mode = True
