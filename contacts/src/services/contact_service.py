from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.repository.contact_repository import *
from src.database.models import Contact
from src.schemas import ContactCreate

def get_all_contacts(db: Session, skip: int = 0, limit: int = 100):
    return get_contacts(db, skip, limit)

def create_new_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(
        first_name=contact.first_name,
        last_name=contact.last_name,
        email=contact.email,
        phone_number=contact.phone_number,
        birthdate=contact.birthdate,
        additional_data=contact.additional_data
    )
    return create_contact(db, db_contact)

def update_existing_contact(db: Session, contact_id: int, contact_data: dict):
    return update_contact(db, contact_id, contact_data)

def delete_existing_contact(db: Session, contact_id: int):
    return delete_contact(db, contact_id)

def get_existing_contact(db: Session, contact_id: int):
    contact = get_contact_by_id(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact