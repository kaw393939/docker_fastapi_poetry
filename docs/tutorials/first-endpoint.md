# Tutorial: Creating Your First Endpoint

## What You'll Learn

In this tutorial, you'll:
- ✅ Create a new API endpoint
- ✅ Accept parameters from the URL
- ✅ Handle request bodies
- ✅ Return different response types
- ✅ Write tests for your endpoint

**Time:** 20-25 minutes  
**Level:** Beginner  
**Prerequisites:** Completed [Your First API](first-api.md)

---

## Step 1: Create a Simple GET Endpoint

Let's create an endpoint that greets users by name.

### Add the Code

Open `app/main.py` and add:

```python
@app.get("/greet/{name}")
async def greet_user(name: str):
    """
    Greet a user by name.
    
    Args:
        name: The user's name from the URL path
        
    Returns:
        A greeting message
    """
    return {"message": f"Hello, {name}!"}
```

### Test It

```bash
curl http://localhost:8001/greet/Alice

# Response:
{"message":"Hello, Alice!"}

curl http://localhost:8001/greet/Bob

# Response:
{"message":"Hello, Bob!"}
```

### What's Happening?

```
URL: /greet/Alice
         └────┘
           │
Path Parameter (captured as 'name')
           │
           ▼
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}
```

---

## Step 2: Add Query Parameters

Query parameters go after the `?` in URLs: `/endpoint?param=value`

### Create the Endpoint

Add to `app/main.py`:

```python
@app.get("/search")
async def search(q: str, limit: int = 10):
    """
    Search endpoint with query parameters.
    
    Args:
        q: Search query (required)
        limit: Maximum results (optional, defaults to 10)
        
    Returns:
        Search results
    """
    return {
        "query": q,
        "limit": limit,
        "results": [
            f"Result 1 for '{q}'",
            f"Result 2 for '{q}'",
            f"Result 3 for '{q}'"
        ][:limit]
    }
```

### Test It

```bash
# With required parameter
curl "http://localhost:8001/search?q=python"

# Response:
{
  "query": "python",
  "limit": 10,
  "results": [
    "Result 1 for 'python'",
    "Result 2 for 'python'",
    "Result 3 for 'python'"
  ]
}

# With optional parameter
curl "http://localhost:8001/search?q=docker&limit=2"

# Response:
{
  "query": "docker",
  "limit": 2,
  "results": [
    "Result 1 for 'docker'",
    "Result 2 for 'docker'"
  ]
}

# Missing required parameter
curl http://localhost:8001/search

# Response:
{
  "detail": [
    {
      "loc": ["query", "q"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Understanding Parameters

```python
def search(q: str, limit: int = 10):
           │        │
           │        └─ Optional (has default value)
           └────────── Required (no default)
```

**In URL:**
```
/search?q=python&limit=5
        │        │
        │        └─ Optional parameter
        └────────── Required parameter
```

---

## Step 3: Create a POST Endpoint

POST endpoints accept data in the request body.

### Define a Data Model

Add to `app/main.py`:

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """User model for validation."""
    name: str
    email: str
    age: int
    active: bool = True  # Optional with default
```

### Create the Endpoint

```python
@app.post("/users")
async def create_user(user: User):
    """
    Create a new user.
    
    Args:
        user: User data from request body
        
    Returns:
        Created user with ID
    """
    # In real app, this would save to database
    return {
        "id": 123,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "active": user.active,
        "created_at": "2025-10-21T12:00:00Z"
    }
```

### Test It

```bash
# Valid request
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Smith",
    "email": "alice@example.com",
    "age": 30
  }'

# Response:
{
  "id": 123,
  "name": "Alice Smith",
  "email": "alice@example.com",
  "age": 30,
  "active": true,
  "created_at": "2025-10-21T12:00:00Z"
}

# Invalid email
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Bob",
    "email": "not-an-email",
    "age": 25
  }'

# Response:
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

### Automatic Validation

Pydantic automatically validates:

```
✅ name must be string
✅ email must be valid email
✅ age must be integer
✅ active defaults to True
```

---

## Step 4: Path Parameters + Query Parameters

Combine both types of parameters!

### Create the Endpoint

```python
@app.get("/users/{user_id}/posts")
async def get_user_posts(
    user_id: int,
    limit: int = 10,
    offset: int = 0
):
    """
    Get posts for a specific user.
    
    Args:
        user_id: User ID from URL path
        limit: Maximum posts to return
        offset: Number of posts to skip
        
    Returns:
        List of posts
    """
    return {
        "user_id": user_id,
        "limit": limit,
        "offset": offset,
        "posts": [
            {
                "id": offset + 1,
                "title": f"Post {offset + 1}",
                "content": "Lorem ipsum..."
            },
            {
                "id": offset + 2,
                "title": f"Post {offset + 2}",
                "content": "Lorem ipsum..."
            }
        ][:limit]
    }
```

### Test It

```bash
# Get first 10 posts for user 42
curl "http://localhost:8001/users/42/posts"

# Get next 5 posts (pagination)
curl "http://localhost:8001/users/42/posts?limit=5&offset=10"
```

---

## Step 5: Response Status Codes

Control the HTTP status code returned.

### Create Endpoint with Custom Status

```python
from fastapi import status

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    """Create user and return 201 Created."""
    return {
        "id": 123,
        "name": user.name,
        "email": user.email
    }

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """Delete user and return 204 No Content."""
    # In real app, delete from database
    return  # No content returned
```

### Test Status Codes

```bash
# Check status code
curl -i -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com","age":30}'

# Response starts with:
HTTP/1.1 201 Created  ← Custom status code

# Delete returns 204
curl -i -X DELETE http://localhost:8001/users/123

# Response:
HTTP/1.1 204 No Content  ← No response body
```

---

## Step 6: Error Handling

Return proper errors when things go wrong.

### Create Endpoint with Validation

```python
from fastapi import HTTPException

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    Get user by ID.
    
    Args:
        user_id: User ID
        
    Returns:
        User data
        
    Raises:
        HTTPException: If user not found
    """
    # Simulate database lookup
    fake_db = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }
    
    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found"
        )
    
    return fake_db[user_id]
```

### Test Error Handling

```bash
# User exists
curl http://localhost:8001/users/1

# Response:
{
  "name": "Alice",
  "email": "alice@example.com"
}

# User doesn't exist
curl -i http://localhost:8001/users/999

# Response:
HTTP/1.1 404 Not Found

{
  "detail": "User 999 not found"
}
```

---

## Step 7: Complete CRUD Example

Let's build a complete resource with all operations.

### The Data Store

```python
# Fake database (in real app, use PostgreSQL/MongoDB)
todos_db = {}
next_id = 1
```

### Create (POST)

```python
class Todo(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: Todo):
    """Create a new todo item."""
    global next_id
    todo_id = next_id
    next_id += 1
    
    todos_db[todo_id] = {
        "id": todo_id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    }
    
    return todos_db[todo_id]
```

### Read (GET)

```python
@app.get("/todos")
async def get_todos():
    """Get all todos."""
    return list(todos_db.values())

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    """Get specific todo."""
    if todo_id not in todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo {todo_id} not found"
        )
    return todos_db[todo_id]
```

### Update (PUT)

```python
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    """Update a todo item."""
    if todo_id not in todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo {todo_id} not found"
        )
    
    todos_db[todo_id] = {
        "id": todo_id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    }
    
    return todos_db[todo_id]
```

### Delete (DELETE)

```python
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    """Delete a todo item."""
    if todo_id not in todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo {todo_id} not found"
        )
    
    del todos_db[todo_id]
```

### Test Complete CRUD

```bash
# Create todo
curl -X POST http://localhost:8001/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","description":"Complete tutorial"}'

# Get all todos
curl http://localhost:8001/todos

# Get specific todo
curl http://localhost:8001/todos/1

# Update todo
curl -X PUT http://localhost:8001/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","completed":true}'

# Delete todo
curl -X DELETE http://localhost:8001/todos/1
```

---

## Step 8: Write Tests

Create `tests/test_endpoints.py`:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_greet_user():
    """Test greeting endpoint."""
    response = client.get("/greet/Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alice!"}

def test_search():
    """Test search endpoint."""
    response = client.get("/search?q=python&limit=2")
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == "python"
    assert data["limit"] == 2
    assert len(data["results"]) == 2

def test_create_user():
    """Test user creation."""
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "age": 25
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"

def test_create_user_invalid_email():
    """Test user creation with invalid email."""
    user_data = {
        "name": "Test User",
        "email": "not-an-email",
        "age": 25
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 422  # Validation error
```

### Run Tests

```bash
docker-compose exec web pytest

# or locally
poetry run pytest
```

---

## What You Learned

✅ Created GET endpoints with path parameters  
✅ Used query parameters for filtering  
✅ Built POST endpoints with request bodies  
✅ Combined path and query parameters  
✅ Set custom HTTP status codes  
✅ Handled errors with HTTPException  
✅ Built complete CRUD operations  
✅ Wrote tests for all endpoints  

---

## Next Steps

1. **Add Data Validation**
   - Guide: [Request Validation](../guides/validation.md)

2. **Connect to Database**
   - Tutorial: [Using PostgreSQL](database-setup.md)

3. **Add Authentication**
   - Guide: [JWT Authentication](../guides/authentication.md)

4. **API Documentation**
   - Guide: [OpenAPI Customization](../guides/openapi.md)

---

## Challenge Exercise

### Build a Blog API

Create a simple blog API with:

**Endpoints:**
- `POST /posts` - Create post
- `GET /posts` - List all posts
- `GET /posts/{id}` - Get specific post
- `PUT /posts/{id}` - Update post
- `DELETE /posts/{id}` - Delete post

**Data Model:**
```python
class Post(BaseModel):
    title: str
    content: str
    author: str
    published: bool = False
```

**Test all endpoints!**

---

**Questions or Stuck?**  
Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
