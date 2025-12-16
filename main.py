from fastapi import FastAPI
import json
import os

app = FastAPI()

DATA_DIR = "users"
os.makedirs(DATA_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "FastAPI is running"}

@app.post("/user/add")
async def add_user(user: dict):
    user_id = user.get("id")
    file_path = f"{DATA_DIR}/{user_id}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(user, f, indent=2)
    return {"status": "saved", "file": file_path}

@app.get("/users")
async def list_users():
    files = os.listdir(DATA_DIR)
    return {"users": files}

@app.get("/user/{user_id}")
async def read_user(user_id: str):
    file_path = f"{DATA_DIR}/{user_id}.json"
    if not os.path.exists(file_path):
        return {"error": "user not found"}
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
