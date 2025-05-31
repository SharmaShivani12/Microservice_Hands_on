# Handles the REST API endpoints.

from fastapi import APIRouter, HTTPException
from app.models import User
from app.storage import users

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.id] = user
    return user

@router.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"detail": "User deleted"}
