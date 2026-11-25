# Todo API

A RESTful Todo API built with FastAPI, SQLAlchemy, PostgreSql, Pydantic, and JWT authentication.

The project provides user registration and login, protected Todo operations, public Todo retrieval, priority and completion tracking, and automatic interactive API documentation.

## Features

- User registration and login
- JWT bearer-token authentication
- Password hashing with Passlib and bcrypt
- Create, read, update, and delete Todo operations
- Todo priority and completion status
- Public/private Todo visibility
- SQLAlchemy and PostgreSql persistence
- Pydantic request and response validation
- Automatic Swagger UI and OpenAPI documentation
- Layered project structure with routers, services, schemas, and models

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Postgres
- Pydantic
- PyJWT
- Passlib
- bcrypt
- Alembic

## Project Structure

```text
todoApp/
|-- core/           # Application settings
|-- db/             # Database engine and session dependency
|-- errors/         # Shared HTTP errors
|-- models/         # SQLAlchemy database models
|-- routers/        # Authentication and Todo API routes
|-- schemas/        # Pydantic request and response models
|-- security/       # Password hashing and verification
|-- services/       # Authentication and Todo business logic
|-- main.py         # FastAPI application entry point
|-- requirements.txt
`-- todosapp.db
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/charlesaloaye/Todo.git
cd Todo
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment

Create a `.env` file in the project root:

```env
SECRET_KEY=replace-this-with-a-long-random-secret
ALGORITHM=HS256
ACCESS_EXPIRY_TIME=30
```

> `ALGORITHM` and `ACCESS_EXPIRY_TIME` are optional when using the application's default values.

### 5. Run the server

```bash
fastapi dev main.py
```

The API is available at `http://127.0.0.1:8000`.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## API Endpoints

### Authentication

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/auth/register` | Register a user | No |
| POST | `/auth/token` | Log in and receive a JWT | No |

### Todos

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| GET | `/todos/` | Retrieve public Todos | No |
| GET | `/todos/{todo_id}` | Retrieve a Todo by ID | No |
| GET | `/todos/status/{todo_status}` | Filter Todos by completion status | No |
| POST | `/todos/` | Create a Todo | Bearer token |
| PUT | `/todos/{todo_id}` | Update a Todo | Bearer token |
| DELETE | `/todos/{todo_id}` | Delete a Todo | Bearer token |

## Authentication Example

### Register

```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "demo_user",
    "email": "demo@example.com",
    "password": "password123",
    "status": true,
    "role": "user"
  }'
```

### Log in

```bash
curl -X POST "http://127.0.0.1:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=demo_user&password=password123"
```

The response contains an access token:

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

### Create a Todo

```bash
curl -X POST "http://127.0.0.1:8000/todos/" \
  -H "Authorization: Bearer <jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Build and document a REST API",
    "priority": "high",
    "completed": false,
    "is_public": true
  }'
```

## Screenshots

### API Documentation

![Swagger UI](docs/screenshots/swagger-ui.png)

### Authentication

![User registration and login](docs/screenshots/authentication.png)

### Todo Operations

![Todo CRUD operations](docs/screenshots/todo-crud.png)

## What I Learned

As a senior developer learning to adopt another framework, this project helped me:

- Understand FastAPI routing and application organization
- Use dependency injection for database sessions and authenticated users
- Combine Python type hints with Pydantic validation
- Implement JWT authentication and OAuth2 password flows
- Integrate SQLAlchemy with an PostgreSql database
- Separate API routes, business logic, schemas, and data models
- Generate interactive API documentation from code
- Design REST endpoints and consistent HTTP responses
- Apply password hashing and secure credential handling

The project reinforced an important lesson: framework adoption is easier when core backend principles such as separation of concerns, secure authentication, data validation, and maintainable architecture are already established.

## License

This project is available for learning and demonstration purposes. Add a license before distributing it as a reusable package. 
