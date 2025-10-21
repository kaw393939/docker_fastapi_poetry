# HTTP Status Codes

## Learning Objectives

By the end of this lesson, you will be able to:
- Identify the five categories of HTTP status codes
- Understand what each status code means
- Choose appropriate status codes for API responses
- Troubleshoot API issues using status codes

---

## What are HTTP Status Codes?

HTTP status codes are three-digit numbers that the server sends back to tell you how your request went. Think of them as the server's way of saying "here's what happened."

---

## The Five Categories

```
1xx - Informational  "Hold on, I'm working on it..."
2xx - Success        "Done! ✅"
3xx - Redirection    "Go look over there →"
4xx - Client Error   "You messed up ❌"
5xx - Server Error   "I messed up 💥"
```

---

## 2xx Success - Everything Worked!

### 200 OK
**Meaning:** Request succeeded, here's your data

**When to use:**
- GET requests that return data
- PUT/PATCH requests that update data
- Any successful operation

**Example:**
```http
GET /api/users/123

HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 123,
  "name": "Alice"
}
```

### 201 Created
**Meaning:** New resource successfully created

**When to use:**
- POST requests that create new resources

**Example:**
```http
POST /api/users

HTTP/1.1 201 Created
Location: /api/users/124

{
  "id": 124,
  "name": "Bob",
  "created_at": "2025-10-21T12:00:00Z"
}
```

### 204 No Content
**Meaning:** Success, but no data to return

**When to use:**
- DELETE requests
- Updates that don't return data

**Example:**
```http
DELETE /api/users/123

HTTP/1.1 204 No Content
```

---

## 3xx Redirection - Resource Moved

### 301 Moved Permanently
**Meaning:** Resource permanently moved to new URL

**Example:**
```http
GET /api/v1/users

HTTP/1.1 301 Moved Permanently
Location: /api/v2/users
```

### 304 Not Modified
**Meaning:** Cached version is still valid

**When to use:**
- Response to conditional GET requests
- When content hasn't changed

---

## 4xx Client Errors - You Made a Mistake

These mean **you** (the client) did something wrong.

### 400 Bad Request
**Meaning:** Your request is malformed or invalid

**Common causes:**
- Invalid JSON syntax
- Missing required fields
- Wrong data types

**Example:**
```http
POST /api/users
{"name": "Alice"  // Missing closing brace

HTTP/1.1 400 Bad Request
{
  "error": "Invalid JSON syntax"
}
```

### 401 Unauthorized
**Meaning:** You need to authenticate first

**Common causes:**
- Missing authentication token
- Invalid credentials
- Expired token

**Example:**
```http
GET /api/protected

HTTP/1.1 401 Unauthorized
{
  "error": "Authentication required"
}
```

### 403 Forbidden
**Meaning:** You're authenticated but don't have permission

**Example:**
```http
DELETE /api/admin/users

HTTP/1.1 403 Forbidden
{
  "error": "Admin access required"
}
```

**401 vs 403:**
```
401: "Who are you?" (Need to login)
403: "I know who you are, but you can't do that" (Insufficient permissions)
```

### 404 Not Found
**Meaning:** Resource doesn't exist

**Common causes:**
- Wrong URL
- Resource was deleted
- Typo in endpoint

**Example:**
```http
GET /api/users/999

HTTP/1.1 404 Not Found
{
  "error": "User not found"
}
```

### 422 Unprocessable Entity
**Meaning:** Request is valid JSON but fails validation

**Example:**
```http
POST /api/users
{
  "name": "A",           // Too short
  "email": "not-an-email" // Invalid format
}

HTTP/1.1 422 Unprocessable Entity
{
  "errors": [
    {"field": "name", "message": "Must be at least 2 characters"},
    {"field": "email", "message": "Invalid email format"}
  ]
}
```

### 429 Too Many Requests
**Meaning:** You're making requests too fast (rate limited)

**Example:**
```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60

{
  "error": "Rate limit exceeded. Try again in 60 seconds"
}
```

---

## 5xx Server Errors - Server Made a Mistake

These mean the **server** has a problem.

### 500 Internal Server Error
**Meaning:** Something went wrong on the server

**Common causes:**
- Unhandled exceptions
- Code bugs
- Database connection failures

**Example:**
```http
GET /api/users

HTTP/1.1 500 Internal Server Error
{
  "error": "An unexpected error occurred"
}
```

### 502 Bad Gateway
**Meaning:** Server got invalid response from upstream server

**Common in:**
- Microservices architecture
- Proxy/load balancer scenarios

### 503 Service Unavailable
**Meaning:** Server temporarily unavailable

**Common causes:**
- Maintenance
- Overloaded server
- Service restart

**Example:**
```http
HTTP/1.1 503 Service Unavailable
Retry-After: 300

{
  "error": "Service temporarily unavailable"
}
```

---

## Quick Reference Table

| Code | Name | Meaning | Example |
|------|------|---------|---------|
| 200 | OK | Success | User data retrieved |
| 201 | Created | Resource created | New user created |
| 204 | No Content | Success, no data | User deleted |
| 400 | Bad Request | Invalid request | Malformed JSON |
| 401 | Unauthorized | Need authentication | Missing token |
| 403 | Forbidden | No permission | Not admin |
| 404 | Not Found | Resource missing | User doesn't exist |
| 422 | Unprocessable | Validation failed | Invalid email |
| 500 | Server Error | Server problem | Database crash |
| 503 | Unavailable | Service down | Maintenance |

---

## Real-World Analogies

### The Restaurant Analogy

```
200 OK          = "Here's your meal, enjoy!"
201 Created     = "Your order is ready!"
204 No Content  = "Order cancelled successfully"
400 Bad Request = "Sorry, I can't read your handwriting"
401 Unauthorized= "You need a reservation"
403 Forbidden   = "Members only section"
404 Not Found   = "That dish isn't on our menu"
422 Unprocessable= "We can't make pizza with ice cream"
500 Server Error= "The kitchen is on fire!"
503 Unavailable = "We're closed for cleaning"
```

---

## Status Code Decision Tree

```
Did the request work?
├─ Yes
│  ├─ Returning data? → 200 OK
│  ├─ Created something? → 201 Created
│  └─ No data to return? → 204 No Content
│
└─ No
   ├─ Client's fault?
   │  ├─ Invalid request? → 400 Bad Request
   │  ├─ Not logged in? → 401 Unauthorized
   │  ├─ No permission? → 403 Forbidden
   │  ├─ Not found? → 404 Not Found
   │  └─ Validation failed? → 422 Unprocessable Entity
   │
   └─ Server's fault?
      ├─ Code error? → 500 Internal Server Error
      └─ Service down? → 503 Service Unavailable
```

---

## Testing Status Codes with curl

```bash
# See status code with -i flag
curl -i http://localhost:8001/

# Output:
HTTP/1.1 200 OK
date: Mon, 21 Oct 2025 12:00:00 GMT
server: uvicorn
content-type: application/json

{"message":"Hello World"}

# Get only status code with -w flag
curl -w "%{http_code}\n" -o /dev/null -s http://localhost:8001/
# Output: 200

# Test 404
curl -i http://localhost:8001/nonexistent
# Output: HTTP/1.1 404 Not Found
```

---

## Common Patterns

### Successful CRUD Operations

```
CREATE (POST):   201 Created
READ (GET):      200 OK
UPDATE (PUT):    200 OK
DELETE (DELETE): 204 No Content
```

### Error Handling Best Practices

```json
// Good error response
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "field": "email"
  }
}

// Better error response
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format",
        "value": "not-an-email"
      },
      {
        "field": "age",
        "message": "Must be at least 18",
        "value": 15
      }
    ]
  }
}
```

---

## Troubleshooting with Status Codes

### Getting 404s?
- Check your URL spelling
- Verify the resource exists
- Check API documentation

### Getting 401s?
- Are you sending authentication token?
- Is the token valid/not expired?
- Are you using correct authentication method?

### Getting 500s?
- Check server logs
- Look for stack traces
- Verify database connections

### Getting 422s?
- Check request body format
- Validate all required fields
- Check data types match expected values

---

## Practice Exercise

### Challenge: Identify Correct Status Codes

What status code should be returned in these scenarios?

1. User successfully logs in
2. Trying to access admin page without admin rights
3. Creating a new blog post
4. Deleting a comment
5. Requesting a user that doesn't exist
6. Sending invalid JSON
7. Database connection fails

**Answers:**
```
1. 200 OK (with auth token)
2. 403 Forbidden
3. 201 Created
4. 204 No Content
5. 404 Not Found
6. 400 Bad Request
7. 500 Internal Server Error
```

---

## Key Takeaways

✅ 2xx means success  
✅ 3xx means redirection  
✅ 4xx means client error (you did something wrong)  
✅ 5xx means server error (server did something wrong)  
✅ Use specific codes to communicate what happened  
✅ Include helpful error messages  
✅ Status codes help with debugging  

---

## Next Steps

- Learn about [HTTP Methods](http-methods.md)
- Understand [REST APIs](rest-apis.md)
- Practice with [curl Testing Guide](../guides/testing-with-curl.md)
- Read [Error Handling Best Practices](../guides/error-handling.md)

---

**Questions or Feedback?**  
Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
