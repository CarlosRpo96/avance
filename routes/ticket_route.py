from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import Ticket
from schemas import TicketCreate, TicketUpdate, TicketResponse
from config.database import get_db
from controllers.ticket_controller import create_ticket, get_all_tickets, get_ticket, update_ticket, delete_ticket

router = APIRouter()

@router.post("/tickets/", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(ticket, db)
    
    
@router.get("/tickets/", response_model=List[TicketResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    return get_all_tickets(db)

@router.get("/tickets/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.put("/tickets/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket_update: TicketUpdate, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    if ticket_update.title:
        ticket.title = ticket_update.title
    if ticket_update.description:
        ticket.description = ticket_update.description
    if ticket_update.status:
        ticket.status = ticket_update.status
    
    db.commit()
    db.refresh(ticket)
    return ticket

@router.delete("/tickets/{ticket_id}", response_model=dict)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    db.delete(ticket)
    db.commit()
    return {"detail": "Ticket deleted"}