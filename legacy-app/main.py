from fastapi import FastAPI
from db import get_db_connection, init_db
import requests

app = FastAPI()

@app.get("/tasks")
async def get_tasks():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return {"tasks":tasks}
    except Exception as e:
        return {"error": str(e)}

@app.post("/task")
async def create_task(task: dict):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (id, name, description, user_id) VALUES (%s, %s, %s)", (task['name'], task['description'], task['user_id']))
        conn.commit()
        conn.close()
        return task
    except Exception as e:
        return {"error": str(e)}

@app.delete("/task/{task_id}")
async def delete_task(task_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id))
        conn.commit()
        conn.close()
        return {"message": f"Task {task_id} deleted"}
    except Exception as e:
        return {"error": str(e)}
    
@app.put("/task/{task_id}")
async def update_task(task_id: int, task: dict):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET name = %s, description = %s WHERE id = %s", (task['name'], task['description'], task_id))
        conn.commit()
        conn.close()
        return task
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/user-tasks/{user_id}")
async def get_user_tasks(user_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id))
        tasks = cursor.fetchall()

        user_data = requests.get(f"http://localhost:8081/users/{user_id}")

        conn.close()
        return {"tasks": tasks, "user": user_data.dumps()}
    except Exception as e:
        return {"error": str(e)}

@app.on_event("startup")
async def startup():
    init_db()