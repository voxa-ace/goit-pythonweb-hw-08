from sqlalchemy.orm import Session
from src.repository.birthday_repository import get_upcoming_birthdays
from src.database.models import Contact

def get_upcoming_birthdays(db: Session, days_range: int = 7):
    return get_upcoming_birthdays(db, days_range)
