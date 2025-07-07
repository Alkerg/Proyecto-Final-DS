import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        user="user",
        password="password",
        database="postgres"
    )
    return conn

def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error initializing db: {e}")