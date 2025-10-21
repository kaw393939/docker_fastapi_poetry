# HTTP Methods (Verbs)

## Learning Objectives

By the end of this lesson, you will be able to:
- Identify the five main HTTP methods
- Explain when to use each HTTP method
- Understand the concept of idempotency
- Apply HTTP methods correctly in API design

---

## What are HTTP Methods?

HTTP methods (also called "verbs") tell the server what action to perform on a resource. Think of them as action words in a sentence.

---

## The Five Main HTTP Methods

### 1. GET - Retrieve Data

**Purpose:** Read/retrieve data without modifying it

**Analogy:** Reading a book - you can read it many times without changing the content

**Example:**
```http
GET /api/users/123
```

**Response:**
```json
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com"
}
```

**Characteristics:**
- ✅ Safe: Doesn't modify data
- ✅ Idempotent: Multiple identical requests have the same effect
- ✅ Cacheable: Responses can be cached
- ❌ Should not have a request body

---

### 2. POST - Create New Data

**Purpose:** Create a new resource

**Analogy:** Writing a new chapter in a book

**Example:**
```http
POST /api/users
Content-Type: application/json

{
  "name": "Bob",
  "email": "bob@example.com"
}
```

**Response:**
```json
{
  "id": 124,
  "name": "Bob",
  "email": "bob@example.com",
  "created_at": "2025-10-21T12:00:00Z"
}
```

**Characteristics:**
- ❌ Not safe: Modifies data
- ❌ Not idempotent: Multiple requests create multiple resources
- ✅ Has a request body
- ✅ Returns the created resource

---

### 3. PUT - Update/Replace Data

**Purpose:** Update an existing resource (complete replacement)

**Analogy:** Replacing an entire chapter with new content

**Example:**
```http
PUT /api/users/123
Content-Type: application/json

{
  "name": "Alice Smith",
  "email": "alice.smith@example.com"
}
```

**Response:**
```json
{
  "id": 123,
  "name": "Alice Smith",
  "email": "alice.smith@example.com",
  "updated_at": "2025-10-21T12:30:00Z"
}
```

**Characteristics:**
- ❌ Not safe: Modifies data
- ✅ Idempotent: Multiple identical requests have the same effect
- ✅ Has a request body
- ✅ Replaces the entire resource

---

### 4. PATCH - Partial Update

**Purpose:** Update specific fields of a resource

**Analogy:** Correcting a typo in a chapter (not rewriting the whole thing)

**Example:**
```http
PATCH /api/users/123
Content-Type: application/json

{
  "email": "alice.updated@example.com"
}
```

**Response:**
```json
{
  "id": 123,
  "name": "Alice Smith",
  "email": "alice.updated@example.com",
  "updated_at": "2025-10-21T12:45:00Z"
}
```

**Characteristics:**
- ❌ Not safe: Modifies data
- ✅ Generally idempotent
- ✅ Has a request body
- ✅ Updates only specified fields

**PUT vs PATCH:**
```
PUT:   Send complete resource (all fields)
PATCH: Send only fields to update
```

---

### 5. DELETE - Remove Data

**Purpose:** Delete a resource

**Analogy:** Tearing out a chapter from a book

**Example:**
```http
DELETE /api/users/123
```

**Response:**
```http
HTTP/1.1 204 No Content
```
or
```json
{
  "message": "User deleted successfully"
}
```

**Characteristics:**
- ❌ Not safe: Modifies data
- ✅ Idempotent: Deleting the same resource multiple times has the same effect
- ❌ Usually no request body
- ✅ May return 204 No Content or confirmation message

---

## Quick Reference Table

| Method | Purpose | Idempotent | Safe | Has Body |
|--------|---------|------------|------|----------|
| GET | Read | ✅ Yes | ✅ Yes | ❌ No |
| POST | Create | ❌ No | ❌ No | ✅ Yes |
| PUT | Update (Replace) | ✅ Yes | ❌ No | ✅ Yes |
| PATCH | Update (Partial) | ✅ Yes | ❌ No | ✅ Yes |
| DELETE | Delete | ✅ Yes | ❌ No | ❌ No |

---

## Understanding Idempotency

**Idempotent**: An operation that produces the same result no matter how many times you perform it.

### Examples

**Idempotent (GET):**
```
Read page 5 of a book
Read page 5 again
Read page 5 again
→ Same result every time
```

**Not Idempotent (POST):**
```
Create new user "Alice"
Create new user "Alice" again
Create new user "Alice" again
→ Creates 3 different users named Alice
```

**Idempotent (DELETE):**
```
Delete user 123
Delete user 123 again (already deleted)
Delete user 123 again (still deleted)
→ User 123 doesn't exist (same result)
```

---

## Real-World Examples

### Blog Application

```http
# Get all blog posts
GET /api/posts

# Get specific post
GET /api/posts/42

# Create new post
POST /api/posts
{
  "title": "My First Post",
  "content": "Hello World!"
}

# Update entire post
PUT /api/posts/42
{
  "title": "Updated Title",
  "content": "Updated content"
}

# Update just the title
PATCH /api/posts/42
{
  "title": "New Title Only"
}

# Delete post
DELETE /api/posts/42
```

---

## Testing with curl

### GET Request
```bash
curl http://localhost:8001/

# Response:
{"message":"Hello World"}
```

### POST Request
```bash
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'
```

### PUT Request
```bash
curl -X PUT http://localhost:8001/users/123 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice Smith","email":"alice@example.com"}'
```

### PATCH Request
```bash
curl -X PATCH http://localhost:8001/users/123 \
  -H "Content-Type: application/json" \
  -d '{"email":"new@example.com"}'
```

### DELETE Request
```bash
curl -X DELETE http://localhost:8001/users/123
```

---

## Common Mistakes to Avoid

### ❌ Don't use GET for modifications
```http
# Wrong!
GET /api/users/123/delete
GET /api/users/create?name=Alice

# Correct!
DELETE /api/users/123
POST /api/users
```

### ❌ Don't use POST for everything
```http
# Wrong!
POST /api/getUser
POST /api/deleteUser

# Correct!
GET /api/users/123
DELETE /api/users/123
```

### ❌ Don't ignore idempotency
```http
# Risky! Might create duplicate orders
POST /api/orders

# Better! Use idempotency key
POST /api/orders
{
  "idempotency_key": "unique-id-123",
  "items": [...]
}
```

---

## Practice Exercise

### Challenge: E-commerce API

Design the HTTP methods for these operations:

1. View all products
2. View product details
3. Add product to cart
4. Update quantity in cart
5. Remove item from cart
6. Place an order

**Answers:**
```
1. GET /api/products
2. GET /api/products/{id}
3. POST /api/cart/items
4. PATCH /api/cart/items/{id}
5. DELETE /api/cart/items/{id}
6. POST /api/orders
```

---

## Key Takeaways

✅ GET retrieves data without modification  
✅ POST creates new resources  
✅ PUT replaces entire resources  
✅ PATCH updates specific fields  
✅ DELETE removes resources  
✅ Idempotent operations produce consistent results  
✅ Choose the right method for the right operation  

---

## Next Steps

- Learn about [HTTP Status Codes](http-status-codes.md)
- Understand [REST API Design](rest-apis.md)
- Practice with [curl Testing Guide](../guides/testing-with-curl.md)

---

**Questions or Feedback?**  
Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
