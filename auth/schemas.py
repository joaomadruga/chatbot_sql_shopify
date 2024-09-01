from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UpdateAPIToken(BaseModel):
    api_token: str


class UserResponse(UserBase):
    access_token: str
    id: int

    class Config:
        orm_mode = True
