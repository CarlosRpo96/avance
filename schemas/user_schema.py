from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    email: Optional[str]
    password: Optional[str]
    active: Optional[bool]

class UserResponse(BaseModel):
    id: int
    email: str
    active: bool
    create_at: str
    update_at: str

    class Config:
        orm_mode = True
