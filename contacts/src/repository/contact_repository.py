from sqlalchemy.orm import Session
from src.database.models import Contact

def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Contact).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: Contact):
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def update_contact(db: Session, contact_id: int, contact_data: dict):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        for key, value in contact_data.items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
        return contact
    return None

def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
        return contact
    return None

def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()