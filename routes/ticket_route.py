from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import Ticket
from schemas import TicketCreate, TicketUpdate, TicketResponse
from config.database import get_db
from controllers.ticket_controller import create_ticket, get_all_tickets

router = APIRouter()

@router.post("/tickets/", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(ticket, db)
    
    
@router.get("/tickets/", response_model=List[TicketResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    return get_all_tickets(db)