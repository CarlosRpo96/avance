from pydantic import BaseModel
from typing import Optional

class TicketCreate(BaseModel):
    title: str
    description: Optional[str]

class TicketUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]

class TicketResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    create_at: str
    update_at: str

    class Config:
        orm_mode = True
