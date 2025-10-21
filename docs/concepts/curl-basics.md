# Testing APIs with curl

## Learning Objectives

By the end of this lesson, you will be able to:
- Use curl to test API endpoints
- Send different HTTP methods with curl
- Include request bodies and headers
- Interpret curl responses
- Debug API issues using curl

---

## What is curl?

**curl** (Client URL) is a command-line tool for making HTTP requests. It's like a browser, but in your terminal.

### Why Use curl?

✅ Fast - no GUI needed  
✅ Scriptable - automate tests  
✅ Powerful - full control over requests  
✅ Available everywhere - pre-installed on Mac/Linux  

---

## Basic curl Syntax

```bash
curl [options] [URL]
```

### Simplest Example

```bash
curl http://localhost:8001/

# Response:
{"message":"Hello World"}
```

---

## Common curl Options

### Essential Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `-X` | Specify HTTP method | `-X POST` |
| `-H` | Add header | `-H "Content-Type: application/json"` |
| `-d` | Send data (request body) | `-d '{"name":"Alice"}'` |
| `-i` | Include response headers | `-i` |
| `-v` | Verbose (debug mode) | `-v` |
| `-o` | Save response to file | `-o response.json` |
| `-w` | Output format | `-w "%{http_code}\n"` |
| `-s` | Silent mode | `-s` |

---

## Testing Different HTTP Methods

### GET Requests

**Retrieve data from the server**

```bash
# Basic GET
curl http://localhost:8001/

# GET with headers visible
curl -i http://localhost:8001/

# GET with verbose output
curl -v http://localhost:8001/health
```

**Output:**
```
HTTP/1.1 200 OK
date: Mon, 21 Oct 2025 12:00:00 GMT
server: uvicorn
content-length: 27
content-type: application/json

{"message":"Hello World"}
```

### POST Requests

**Create new resources**

```bash
# POST with JSON data
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'

# POST with data from file
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d @user.json

# POST with multiple headers
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer abc123" \
  -d '{"name":"Bob"}'
```

**Multi-line format (easier to read):**
```bash
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30
  }'
```

### PUT Requests

**Update (replace) existing resources**

```bash
curl -X PUT http://localhost:8001/users/123 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Smith",
    "email": "alice.smith@example.com"
  }'
```

### PATCH Requests

**Partial update of resources**

```bash
curl -X PATCH http://localhost:8001/users/123 \
  -H "Content-Type: application/json" \
  -d '{"email":"new@example.com"}'
```

### DELETE Requests

**Remove resources**

```bash
curl -X DELETE http://localhost:8001/users/123

# With authentication
curl -X DELETE http://localhost:8001/users/123 \
  -H "Authorization: Bearer abc123"
```

---

## Working with Headers

### Request Headers

```bash
# Content-Type (what you're sending)
curl -H "Content-Type: application/json" \
  http://localhost:8001/

# Accept (what you want back)
curl -H "Accept: application/json" \
  http://localhost:8001/

# Authorization
curl -H "Authorization: Bearer your-token-here" \
  http://localhost:8001/protected

# Multiple headers
curl -H "Content-Type: application/json" \
     -H "Authorization: Bearer abc123" \
     -H "X-Custom-Header: value" \
  http://localhost:8001/
```

### Viewing Response Headers

```bash
# Include headers in output
curl -i http://localhost:8001/

# Output:
HTTP/1.1 200 OK
date: Mon, 21 Oct 2025 12:00:00 GMT
server: uvicorn
content-length: 27
content-type: application/json

{"message":"Hello World"}

# Only headers (no body)
curl -I http://localhost:8001/

# Output:
HTTP/1.1 200 OK
date: Mon, 21 Oct 2025 12:00:00 GMT
server: uvicorn
content-length: 27
content-type: application/json
```

---

## Formatting and Viewing Output

### Pretty Print JSON (with jq)

```bash
# Install jq first (macOS)
brew install jq

# Use with curl
curl http://localhost:8001/ | jq

# Output:
{
  "message": "Hello World"
}

# Extract specific fields
curl http://localhost:8001/users/123 | jq '.name'
# Output: "Alice"

# Multiple fields
curl http://localhost:8001/users/123 | jq '{name, email}'
```

### Save Response to File

```bash
# Save JSON response
curl http://localhost:8001/users > users.json

# Save with headers
curl -i http://localhost:8001/users > response.txt

# Silent mode (no progress bar)
curl -s http://localhost:8001/users > users.json
```

---

## Debugging with curl

### Verbose Mode

```bash
curl -v http://localhost:8001/

# Output:
*   Trying 127.0.0.1:8001...
* Connected to localhost (127.0.0.1) port 8001 (#0)
> GET / HTTP/1.1
> Host: localhost:8001
> User-Agent: curl/7.79.1
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Mon, 21 Oct 2025 12:00:00 GMT
< server: uvicorn
< content-length: 27
< content-type: application/json
<
{"message":"Hello World"}
```

**What it shows:**
- `*` = curl's internal messages
- `>` = Request headers (what you send)
- `<` = Response headers (what you receive)

### Checking Only Status Code

```bash
# Get HTTP status code
curl -w "%{http_code}\n" -o /dev/null -s http://localhost:8001/

# Output:
200

# Check if endpoint is working
if [ $(curl -w "%{http_code}\n" -o /dev/null -s http://localhost:8001/) -eq 200 ]; then
  echo "API is up!"
else
  echo "API is down!"
fi
```

### Timing Information

```bash
curl -w "\n\nTime Total: %{time_total}s\n" \
  http://localhost:8001/

# Output:
{"message":"Hello World"}

Time Total: 0.025s
```

---

## Testing Our FastAPI App

### Test Root Endpoint

```bash
# Basic test
curl http://localhost:8001/

# Expected:
{"message":"Hello World"}

# With headers
curl -i http://localhost:8001/

# Expected:
HTTP/1.1 200 OK
...
{"message":"Hello World"}
```

### Test Health Check

```bash
curl http://localhost:8001/health

# Expected:
{"status":"healthy"}

# Verify status code
curl -w "%{http_code}\n" -o /dev/null -s http://localhost:8001/health
# Expected: 200
```

### Test Interactive Docs

```bash
# OpenAPI JSON
curl http://localhost:8001/openapi.json | jq

# Swagger UI (HTML)
curl http://localhost:8001/docs

# ReDoc (HTML)
curl http://localhost:8001/redoc
```

---

## Common curl Patterns

### Check if API is Running

```bash
#!/bin/bash
if curl -s http://localhost:8001/health > /dev/null; then
  echo "✅ API is running"
else
  echo "❌ API is down"
fi
```

### Test with Authentication

```bash
# Get token
TOKEN=$(curl -s -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"secret"}' | jq -r '.token')

# Use token
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8001/protected
```

### Upload File

```bash
curl -X POST http://localhost:8001/upload \
  -F "file=@document.pdf" \
  -F "description=My document"
```

### Download File

```bash
curl -o downloaded.pdf \
  http://localhost:8001/files/123
```

---

## Troubleshooting with curl

### Connection Refused

```bash
curl http://localhost:8001/

# Error:
curl: (7) Failed to connect to localhost port 8001: Connection refused
```

**Solutions:**
1. Check if server is running: `docker-compose ps`
2. Verify port: Check `docker-compose.yml`
3. Start server: `docker-compose up`

### 404 Not Found

```bash
curl http://localhost:8001/wrong

# Response:
{"detail":"Not Found"}
```

**Solutions:**
1. Check endpoint spelling
2. View available endpoints: `http://localhost:8001/docs`
3. Verify HTTP method is correct

### 401 Unauthorized

```bash
curl http://localhost:8001/protected

# Response:
{"detail":"Not authenticated"}
```

**Solutions:**
1. Include authentication header
2. Check token is valid
3. Ensure endpoint doesn't require auth

### 422 Unprocessable Entity

```bash
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{"name":"A"}'

# Response:
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Solutions:**
1. Check request body matches expected schema
2. Include all required fields
3. Validate data types

---

## curl vs Other Tools

| Tool | Best For |
|------|----------|
| curl | Automation, scripts, quick tests |
| Postman | GUI, collections, team collaboration |
| HTTPie | Human-friendly CLI alternative |
| Browser | Visual testing, forms |
| pytest | Automated testing, CI/CD |

### HTTPie (curl alternative)

```bash
# Install
brew install httpie

# Simpler syntax
http localhost:8001/

# POST JSON (automatic)
http POST localhost:8001/users name=Alice email=alice@example.com

# vs curl
curl -X POST localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'
```

---

## Practice Exercises

### Exercise 1: Test All Endpoints

```bash
# 1. Test root endpoint
curl http://localhost:8001/

# 2. Test health endpoint
curl http://localhost:8001/health

# 3. Check status codes
curl -w "%{http_code}\n" -o /dev/null -s http://localhost:8001/
curl -w "%{http_code}\n" -o /dev/null -s http://localhost:8001/health
```

### Exercise 2: Create Test Script

```bash
#!/bin/bash
# test-api.sh

echo "Testing API endpoints..."

# Test root
if curl -s http://localhost:8001/ | grep -q "Hello World"; then
  echo "✅ Root endpoint working"
else
  echo "❌ Root endpoint failed"
fi

# Test health
if curl -s http://localhost:8001/health | grep -q "healthy"; then
  echo "✅ Health endpoint working"
else
  echo "❌ Health endpoint failed"
fi
```

---

## Key Takeaways

✅ curl makes HTTP requests from the command line  
✅ Use `-X` for HTTP methods (GET, POST, PUT, DELETE)  
✅ Use `-H` for headers, `-d` for request body  
✅ Use `-i` to see response headers  
✅ Use `-v` for debugging  
✅ Pipe to `jq` for pretty JSON  
✅ Perfect for automation and testing  

---

## Next Steps

- Learn about [HTTP Methods](http-methods.md)
- Understand [HTTP Status Codes](http-status-codes.md)
- Practice [Writing Tests](../tutorials/first-test.md)
- Read [curl Documentation](https://curl.se/docs/)

---

**Questions or Feedback?**  
Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
