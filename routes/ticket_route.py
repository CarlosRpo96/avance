from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from models.ticket_model import Ticket
from schemas.ticket_schema import TicketCreate, TicketUpdate, TicketResponse
from config.database import get_db
from controllers.ticket_controller import create_ticket, get_all_ticket, get_ticket, update_ticket, delete_ticket

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
    responses={
        404: {"description": "Tickets router Not found"},
    },
)

@router.post("/", response_model=TicketResponse)
def create_tickets(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(Ticket, db)
    
    
@router.get("/", response_model=List[TicketResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    return get_all_ticket(db)

@router.get("/{ticket_id}", response_model=TicketResponse)
def get_tickets(ticket_id: int, db: Session = Depends(get_db)):
    return get_ticket(ticket_id, db)

@router.put("/{ticket_id}", response_model=TicketResponse)
def update_tickets(ticket_id: int, ticket_update: TicketUpdate, db: Session = Depends(get_db)):
    return update_ticket(ticket_id, ticket_update, db)

@router.delete("/{ticket_id}", response_model=dict)
def delete_tickets(ticket_id: int, db: Session = Depends(get_db)):
    return delete_ticket(ticket_id, db)