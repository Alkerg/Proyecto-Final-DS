from fastapi import FastAPI
from db import get_db_connection, init_db

app = FastAPI()


@app.get("/users")
async def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return {"users": users}
    except Exception as e:
        return {"error": str(e)}

@app.post("/user")
async def create_user(user:dict):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name, email) VALUES (%s, %s, %s)", (user['id'], user['name'], user['email']))
        conn.commit()
        conn.close()
        return user
    except Exception as e:
        return {"error": str(e)}

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id))
        user = cursor.fetchone()
        conn.close()
        if user:
            return {"user": user}
        else:
            return {"error": "User not found"}
    except Exception as e:
        return {"error": str(e)}

@app.on_event("startup")
async def startup():
    init_db()