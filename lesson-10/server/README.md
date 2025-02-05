# FastAPI JSONPlaceholder Clone

## Overview

This project is a **JSONPlaceholder clone** built using **FastAPI**. It provides RESTful APIs for managing resources such as posts, comments, and users. The application is modular, scalable, and uses SQLite as the database for data persistence.

---

## Features

- **CRUD Operations**:
  - Create, Read, Update, and Delete resources.
  - Resources include:
    - Posts
    - Comments
    - Users
- **Modular Structure**: Each resource is managed by its own router for better code organization.
- **SQLite Database**: Data is persisted using SQLite with SQLAlchemy as the ORM.
- **API Documentation**: Automatic, interactive API docs available at `/docs` (Swagger UI) and `/redoc`.

---

## Project Structure

```
myapp/
├── main.py              # Main application entry point
├── database.py          # Database configuration and session management
├── models.py            # SQLAlchemy models for database tables
├── schemas.py           # Pydantic schemas for request and response validation
├── routers/             # Modular routers for each resource
│   ├── posts.py         # Routes for posts resource
│   ├── comments.py      # Routes for comments resource
│   ├── users.py         # Routes for users resource
│   └── __init__.py      # Router package initializer
└── README.md            # Project documentation
```

---

## Installation

### Prerequisites

- **Python 3.8+** installed on your system.
- **Virtual Environment** (recommended for Python projects).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-jsonplaceholder-clone.git
   cd fastapi-jsonplaceholder-clone
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Open the API documentation in your browser:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

### **Posts**
- `GET /posts`: Get all posts.
- `GET /posts/{id}`: Get a post by ID.
- `POST /posts`: Create a new post.
- `PUT /posts/{id}`: Update a post by ID.
- `DELETE /posts/{id}`: Delete a post by ID.

### **Comments**
- `GET /comments`: Get all comments.
- `GET /comments/{id}`: Get a comment by ID.
- `POST /comments`: Create a new comment.
- `PUT /comments/{id}`: Update a comment by ID.
- `DELETE /comments/{id}`: Delete a comment by ID.

### **Users**
- `GET /users`: Get all users.
- `GET /users/{id}`: Get a user by ID.
- `POST /users`: Create a new user.
- `PUT /users/{id}`: Update a user by ID.
- `DELETE /users/{id}`: Delete a user by ID.

---

## Example Requests

### Create a Post
```bash
POST /posts
Content-Type: application/json

{
  "title": "My First Post",
  "body": "This is the body of the post.",
  "user_id": 1
}
```

### Create a Comment
```bash
POST /comments
Content-Type: application/json

{
  "name": "Jane Doe",
  "email": "jane.doe@example.com",
  "body": "This is a comment.",
  "post_id": 1
}
```

### Create a User
```bash
POST /users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "123-456-7890",
  "website": "johndoe.com"
}
```
