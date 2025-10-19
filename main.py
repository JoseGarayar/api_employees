from fastapi import FastAPI
import sqlite3
import schemas

app = FastAPI()

# SQLite database configuration
DATABASE_PATH = "employees.db"

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def init_database():
    """Initialize the database and create the employees table if it doesn't exist"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_database()

# Get all employees
@app.get("/employees")
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    result = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"employees": result}

# Get an employee by ID
@app.get("/employees/{id}")
def get_employee(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"employee": dict(row)}
    return {"message": "Employee not found"}

# Add a new employee
@app.post("/employees")
def add_employee(item: schemas.Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", (item.name, item.age))
    conn.commit()
    conn.close()
    return {"message": "Employee added successfully"}

# Modify an employee
@app.put("/employees/{id}")
def update_employee(id: int, item: schemas.Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET name=?, age=? WHERE id=?", (item.name, item.age, id))
    conn.commit()
    conn.close()
    return {"message": "Employee modified successfully"}

# Delete an employee by ID
@app.delete("/employees/{id}")
def delete_employee(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return {"message": "Employee deleted successfully"}