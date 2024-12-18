# app/main.py
from fastapi import FastAPI
from app.routes import parking_apis

app = FastAPI()

app.include_router(parking_apis.router)
