from sqlalchemy import Column, Integer, String, Date
from src.database.db import Base

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, index=True)
    birthdate = Column(Date)
    additional_data = Column(String, nullable=True)
