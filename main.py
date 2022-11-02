from typing import List
from uuid import uuid4
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User


app = FastAPI()


db: List[User] = [
    User(
        id=1,
        first_name="Ayeni",
        last_name="Oluwaseun",
        middle_name= "Isaac",
        gender= Gender.male,
        roles = [Role.student]
    ),
      User(
        id=2,
        first_name="Neila",
        last_name="Johnson",
        middle_name= "Novi",
        gender= Gender.female,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello: world"} 

@app.get("/api/v1/users")   
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delate_user(user_id: str):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: User, user_id: int):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"

    )


 