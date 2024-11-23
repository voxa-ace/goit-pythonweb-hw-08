from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/contacts/", response_model=schemas.ContactResponse)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db=db, contact=contact)

@app.get("/contacts/", response_model=list[schemas.ContactResponse])
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_contacts(db=db, skip=skip, limit=limit)

@app.get("/contacts/{contact_id}", response_model=schemas.ContactResponse)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact(db=db, contact_id=contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.put("/contacts/{contact_id}", response_model=schemas.ContactResponse)
def update_contact(contact_id: int, updates: schemas.ContactUpdate, db: Session = Depends(get_db)):
    contact = crud.update_contact(db=db, contact_id=contact_id, updates=updates)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.delete("/contacts/{contact_id}", response_model=schemas.ContactResponse)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.delete_contact(db=db, contact_id=contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.get("/search/", response_model=list[schemas.ContactResponse])
def search(query: str, db: Session = Depends(get_db)):
    return crud.search_contacts(db=db, query=query)

@app.get("/birthdays/", response_model=list[schemas.ContactResponse])
def birthdays(db: Session = Depends(get_db)):
    return crud.get_upcoming_birthdays(db=db)
