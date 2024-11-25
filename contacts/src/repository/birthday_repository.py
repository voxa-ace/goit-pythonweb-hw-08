from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from src.database.models import Contact

def get_upcoming_birthdays(db: Session, days_range: int = 7):
    today = datetime.today()
    future_date = today + timedelta(days=days_range)
    
    contacts = db.query(Contact).filter(
        Contact.birthdate >= today,
        Contact.birthdate <= future_date
    ).all()
    
    return contacts
