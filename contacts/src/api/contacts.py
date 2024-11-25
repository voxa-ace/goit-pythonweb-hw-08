from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.contact_service import (
    get_all_contacts,
    create_new_contact,
    update_existing_contact,
    delete_existing_contact,
    get_existing_contact  # Імпортуємо нову функцію
)
from src.schemas import ContactCreate, ContactResponse
from src.database.db import get_db

router = APIRouter()

@router.post("/contacts/", response_model=ContactResponse)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return create_new_contact(db, contact)

@router.get("/contacts/", response_model=list[ContactResponse])
def get_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_contacts(db, skip, limit)

@router.get("/contacts/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    return get_existing_contact(db, contact_id)

@router.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact(contact_id: int, contact: ContactCreate, db: Session = Depends(get_db)):
    contact_data = contact.dict(exclude_unset=True)
    return update_existing_contact(db, contact_id, contact_data)

@router.delete("/contacts/{contact_id}", response_model=ContactResponse)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    return delete_existing_contact(db, contact_id)
