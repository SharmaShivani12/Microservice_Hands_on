#This file Initializes the FastAPI app and includes routes.

from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="User Microservice")
app.include_router(router)
