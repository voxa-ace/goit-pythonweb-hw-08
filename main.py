from fastapi import FastAPI
from src.api.contacts import router as contact_router
from src.api.birthdays import router as birthday_router

# Create FastAPI app instance
app = FastAPI()

# Include routers
app.include_router(contact_router, prefix="/api", tags=["Contacts"])
app.include_router(birthday_router, prefix="/api", tags=["Birthdays"])
