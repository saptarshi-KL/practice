# Student Marks Calculator API

A FastAPI-based REST API to calculate average marks for students. Built with Pydantic for data validation and following FastAPI best practices.

## Features

- ✅ Calculate average marks for a single student
- ✅ Calculate average marks for multiple students in batch
- ✅ Input validation using Pydantic models
- ✅ Interactive API documentation (Swagger UI)
- ✅ Type hints throughout the codebase
- ✅ Error handling with meaningful HTTP exceptions
- ✅ Request/response schemas with examples

## Requirements

- Python 3.9+
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Pydantic 2.5.0

## Installation

1. Clone this repository or navigate to the project folder

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   - **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
python main.py
```

Or using Uvicorn directly:
```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## API Documentation

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`
- **OpenAPI JSON:** `http://127.0.0.1:8000/openapi.json`

## API Endpoints

### 1. Calculate Single Student Average

**POST** `/calculate-average`

Calculate the average marks for a single student.

**Request Body:**
```json
{
  "name": "John Doe",
  "marks": [85.5, 90.0, 78.5]
}
```

**Response:**
```json
{
  "name": "John Doe",
  "average_marks": 84.67
}
```

### 2. Calculate Multiple Students Average (Batch)

**POST** `/calculate-batch-average`

Calculate the average marks for multiple students in a single request.

**Request Body:**
```json
[
  {
    "name": "John Doe",
    "marks": [85.5, 90.0, 78.5]
  },
  {
    "name": "Jane Smith",
    "marks": [92.0, 88.5, 95.2]
  }
]
```

**Response:**
```json
[
  {
    "name": "John Doe",
    "average_marks": 84.67
  },
  {
    "name": "Jane Smith",
    "average_marks": 91.9
  }
]
```

### 3. Health Check

**GET** `/`

Returns the status of the API.

**Response:**
```json
{
  "message": "Student Marks Calculator API",
  "status": "healthy",
  "docs_url": "/docs",
  "openapi_url": "/openapi.json"
}
```

## Example Usage

### Using cURL

```bash
# Single student
curl -X POST "http://127.0.0.1:8000/calculate-average" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "marks": [85.5, 90.0, 78.5]}'

# Multiple students
curl -X POST "http://127.0.0.1:8000/calculate-batch-average" \
  -H "Content-Type: application/json" \
  -d '[{"name": "John Doe", "marks": [85.5, 90.0, 78.5]}, {"name": "Jane Smith", "marks": [92.0, 88.5, 95.2]}]'
```

### Using Python Requests

```python
import requests

# Single student
response = requests.post(
    "http://127.0.0.1:8000/calculate-average",
    json={"name": "John Doe", "marks": [85.5, 90.0, 78.5]}
)
print(response.json())

# Multiple students
response = requests.post(
    "http://127.0.0.1:8000/calculate-batch-average",
    json=[
        {"name": "John Doe", "marks": [85.5, 90.0, 78.5]},
        {"name": "Jane Smith", "marks": [92.0, 88.5, 95.2]}
    ]
)
print(response.json())
```

## Validation Rules

- **name:** Required, 1-100 characters
- **marks:** Required, at least 1 mark, accepts float values
- **average_marks:** Rounded to 2 decimal places

## Best Practices Implemented

1. **Pydantic Models:** Using Pydantic v2 for request/response validation with field descriptions
2. **Type Hints:** Full type hints throughout the application
3. **Error Handling:** Proper HTTP exceptions with meaningful error messages
4. **Documentation:** Comprehensive docstrings and OpenAPI schema examples
5. **Separation of Concerns:** Clear models for input and output
6. **Async Endpoints:** Using async functions for better performance
7. **Tags:** Organized endpoints with tags in the API documentation
8. **Config Examples:** JSON schema examples in model configuration

## Project Structure

```
.
├── main.py              # Main FastAPI application
├── requirements.txt     # Project dependencies
├── README.md           # This file
└── venv/               # Virtual environment (created during setup)
```

## License

MIT License
