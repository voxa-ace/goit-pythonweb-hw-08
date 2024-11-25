from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.services.birthday_service import get_upcoming_birthdays
from src.schemas import ContactResponse
from src.database.db import get_db

router = APIRouter()

@router.get("/birthdays/", response_model=list[ContactResponse])
def get_birthdays(days_range: int = 7, db: Session = Depends(get_db)):
    return get_upcoming_birthdays(db, days_range)