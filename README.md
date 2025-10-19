# Employee Management API

A simple REST API for managing employee records built with FastAPI and SQLite.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete employee records
- **RESTful API**: Clean and intuitive endpoints
- **SQLite Database**: Lightweight database for data persistence
- **Docker Support**: Containerized application for easy deployment
- **Pydantic Models**: Data validation and serialization

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Get all employees |
| GET | `/employees/{id}` | Get employee by ID |
| POST | `/employees` | Create a new employee |
| PUT | `/employees/{id}` | Update an employee |
| DELETE | `/employees/{id}` | Delete an employee |

## Data Model

### Employee Schema
```json
{
  "name": "string",
  "age": "integer"
}
```

## Installation & Setup

### Prerequisites
- Python 3.13+
- pip

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/JoseGarayar/api_employees.git
   cd api_employees
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi[standard] pydantic
   ```

3. **Run the application**
   ```bash
   fastapi run main.py --port 8000
   ```

4. **Access the API**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t api-employees .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 api-employees
   ```

## Usage Examples

### Get all employees
```bash
curl -X GET "http://localhost:8000/employees"
```

### Get employee by ID
```bash
curl -X GET "http://localhost:8000/employees/1"
```

### Create a new employee
```bash
curl -X POST "http://localhost:8000/employees" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 30}'
```

### Update an employee
```bash
curl -X PUT "http://localhost:8000/employees/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Smith", "age": 28}'
```

### Delete an employee
```bash
curl -X DELETE "http://localhost:8000/employees/1"
```

## Project Structure

```
api_employees/
├── main.py          # FastAPI application and endpoints
├── schemas.py       # Pydantic models for data validation
├── Dockerfile       # Docker configuration
├── README.md        # Project documentation
└── employees.db     # SQLite database (created automatically)
```

## Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
```

## Development

### Adding New Features

1. **New Endpoints**: Add new route handlers in `main.py`
2. **Data Models**: Define new Pydantic models in `schemas.py`
3. **Database Changes**: Modify the `init_database()` function for schema updates

### Testing

You can test the API using:
- **FastAPI Interactive Docs**: Visit http://localhost:8000/docs
- **curl commands**: Use the examples provided above
- **Postman/Insomnia**: Import the API endpoints
