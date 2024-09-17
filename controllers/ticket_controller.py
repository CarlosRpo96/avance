from fastapi import  HTTPException
from models.ticket_model import Ticket
from schemas.ticket_schema import TicketCreate, TicketUpdate #ticketresponse delete

def create_ticket(ticket: TicketCreate, db):
    db_ticket = Ticket(title=ticket.title, description=ticket.description)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_all_ticket(db):
    return db.query(Ticket).all()


def get_ticket(ticket_id: int, db):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


def update_ticket(ticket_id: int, ticket_update: TicketUpdate, db):
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


def delete_ticket(ticket_id: int, db):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    db.delete(ticket)
    db.commit()
    return {"detail": "Ticket deleted"}
