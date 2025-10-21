# Understanding REST APIs

## Learning Objectives

By the end of this lesson, you will be able to:
- Define what a REST API is
- Explain the client-server architecture
- Identify the key characteristics of RESTful services
- Understand how HTTP powers REST APIs

---

## What is a REST API?

**REST** stands for **Representational State Transfer**. It's an architectural style for building web services that applications can use to communicate over the internet.

### The Restaurant Analogy

Think of a REST API like a restaurant:

```
┌─────────────────┐                    ┌─────────────────┐
│  You (Client)   │                    │ Kitchen (Server)│
│                 │                    │                 │
│  "I want a      │ ──── Order ──────▶ │  Prepares       │
│   burger"       │                    │  your meal      │
│                 │                    │                 │
│  Receives meal  │ ◀──── Meal ─────── │  Sends it out   │
└─────────────────┘                    └─────────────────┘
```

- **You (Client)**: The customer making requests
- **Menu (API Documentation)**: Lists what you can order (available endpoints)
- **Waiter (HTTP Protocol)**: Takes your order and brings back food
- **Kitchen (Server)**: Prepares what you ordered
- **Food (Data/Response)**: What you receive

### The Technical View

```
┌──────────────┐                           ┌──────────────┐
│   Client     │ ── HTTP Request ────────▶ │   Server     │
│  (Browser,   │    GET /api/users         │  (FastAPI    │
│   Mobile     │                           │   App)       │
│   App)       │ ◀── HTTP Response ──────  │              │
│              │    {"users": [...]}       │              │
└──────────────┘                           └──────────────┘
```

---

## Key Characteristics of REST

### 1. Stateless
Each request contains all information needed to process it. The server doesn't remember previous requests.

**Example:**
```
❌ Bad (Stateful):
Request 1: "Login as Alice"
Request 2: "Get my profile"  (Server remembers you're Alice)

✅ Good (Stateless):
Request 1: "Login as Alice" → Receive token: abc123
Request 2: "Get profile for token abc123"
```

### 2. Resource-Based
Everything is a "resource" identified by a URL.

**Examples:**
```
Users:          /api/users
Specific user:  /api/users/123
User's posts:   /api/users/123/posts
Specific post:  /api/users/123/posts/456
```

### 3. Standard HTTP Methods
Uses HTTP verbs to perform actions:

| Action | HTTP Method | Example |
|--------|-------------|---------|
| Read | GET | Get user info |
| Create | POST | Create new user |
| Update | PUT/PATCH | Update user info |
| Delete | DELETE | Remove user |

### 4. JSON Format
Data is typically exchanged in JSON (JavaScript Object Notation):

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "active": true
}
```

---

## REST API Communication Flow

### Step-by-Step Example

**Scenario:** Get a list of users

```
1. Client sends request:
   GET http://api.example.com/users
   Headers:
     Authorization: Bearer abc123
     Accept: application/json

2. Server receives request:
   - Authenticates the token
   - Queries the database
   - Formats the response

3. Server sends response:
   HTTP/1.1 200 OK
   Content-Type: application/json
   
   {
     "users": [
       {"id": 1, "name": "Alice"},
       {"id": 2, "name": "Bob"}
     ]
   }

4. Client receives and processes response
```

---

## RESTful URL Structure

### Best Practices

```
✅ Good RESTful URLs:
GET    /users              - Get all users
GET    /users/123          - Get user with ID 123
POST   /users              - Create new user
PUT    /users/123          - Update user 123
DELETE /users/123          - Delete user 123
GET    /users/123/posts    - Get posts by user 123

❌ Poor URLs (Not RESTful):
/getUsers
/createNewUser
/deleteUserById?id=123
/user_posts_list
```

### URL Components

```
https://api.example.com:443/v1/users/123?active=true&sort=name#top
└─┬─┘ └────────┬────────┘└┬┘└┬┘└──┬──┘└─┬─┘└────────┬─────────┘└┬┘
  │          Domain        │  │  Path   │      Query String      │
Protocol              Port │  │        │                     Fragment
                      Version│     Resource
                        Endpoint
```

---

## Why Use REST APIs?

### Advantages

1. **Platform Independent**: Works with any programming language
2. **Scalable**: Can handle millions of requests
3. **Flexible**: Separates frontend from backend
4. **Cacheable**: Responses can be cached for performance
5. **Standard**: Uses familiar HTTP protocol

### Real-World Examples

- **Twitter API**: Post tweets, get timeline
- **Google Maps API**: Get location data, directions
- **Stripe API**: Process payments
- **GitHub API**: Access repositories, issues
- **Weather API**: Get weather forecasts

---

## Practice Exercise

### Challenge: Design a Library REST API

Design URLs for a library system that manages:
- Books
- Authors
- Borrowing records

**Questions:**
1. What URL would you use to get all books?
2. How would you get a specific book?
3. How would you create a new author?
4. How would you get all books by a specific author?

**Answers:**
```
1. GET /books
2. GET /books/{book_id}
3. POST /authors
4. GET /authors/{author_id}/books
```

---

## Key Takeaways

✅ REST APIs enable communication between different applications  
✅ They use HTTP methods (GET, POST, PUT, DELETE) for actions  
✅ Data is exchanged in JSON format  
✅ Each request is independent (stateless)  
✅ Resources are identified by URLs  

---

## Next Steps

- Learn about [HTTP Methods](http-methods.md)
- Understand [HTTP Status Codes](http-status-codes.md)
- Explore [Ports and Networking](ports-networking.md)

---

**Questions or Feedback?**  
Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
