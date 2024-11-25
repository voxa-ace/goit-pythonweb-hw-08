from fastapi import FastAPI
from src.api.contacts import router as contact_router
from src.api.birthdays import router as birthday_router

app = FastAPI()

app.include_router(contact_router)
app.include_router(birthday_router)
