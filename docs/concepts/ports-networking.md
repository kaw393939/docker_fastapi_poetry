# Ports and Networking Basics

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what ports are and why they're needed
- Identify common port numbers and their uses
- Understand how port mapping works in Docker
- Troubleshoot port-related issues

---

## What are Ports?

**Ports** are like apartment numbers in a building. They help direct network traffic to the right application on a computer.

### The Building Analogy

```
Your Computer (127.0.0.1) = The Building
├── Apartment 80 (Port 80)   → Web Server
├── Apartment 443 (Port 443) → Secure Web Server
├── Apartment 3306 (Port 3306) → MySQL Database
├── Apartment 5432 (Port 5432) → PostgreSQL
└── Apartment 8001 (Port 8001) → Our FastAPI App ⬅️
```

**Full Address Format:**
```
http://127.0.0.1:8001
└─┬─┘  └────┬───┘└┬┘
  │    IP Address │
Protocol      Port Number
```

---

## Understanding IP Addresses

### localhost and 127.0.0.1

These both mean "this computer" (the one you're using):

```
localhost = 127.0.0.1 = "My Computer"
```

**Examples:**
```
http://localhost:8001     Same as →  http://127.0.0.1:8001
http://localhost:3000     Same as →  http://127.0.0.1:3000
```

### 0.0.0.0 vs 127.0.0.1

| Address | Meaning | Use Case |
|---------|---------|----------|
| 127.0.0.1 | Only this computer | Local testing |
| 0.0.0.0 | All network interfaces | Docker containers, servers |

**Why Docker uses 0.0.0.0:**
```
Inside Container: --host 0.0.0.0  (listen on all interfaces)
From Your Machine: localhost:8001 (access the container)
```

---

## Common Port Numbers

### Well-Known Ports (0-1023)

These are reserved for standard services:

| Port | Service | Example |
|------|---------|---------|
| 20/21 | FTP | File transfer |
| 22 | SSH | Remote server access |
| 25 | SMTP | Email sending |
| 53 | DNS | Domain name lookup |
| 80 | HTTP | Web traffic |
| 443 | HTTPS | Secure web traffic |

### Registered Ports (1024-49151)

| Port | Service | Example |
|------|---------|---------|
| 3000 | React dev server | Frontend development |
| 3306 | MySQL | Database |
| 5000 | Flask default | Python web apps |
| 5432 | PostgreSQL | Database |
| 6379 | Redis | Cache/database |
| 8000 | Common dev port | FastAPI, Django |
| 8001 | Our app | This project! |
| 8080 | Alternative HTTP | Development servers |
| 27017 | MongoDB | NoSQL database |

### Dynamic Ports (49152-65535)

Used for temporary connections

---

## Port Mapping in Docker

### The Concept

```
Your Computer                    Docker Container
┌─────────────────┐             ┌──────────────────┐
│                 │             │                  │
│  Port 8001 ─────┼────────────▶│  Port 8000       │
│  (Host)         │  Mapped!    │  (Container)     │
│                 │             │                  │
└─────────────────┘             └──────────────────┘
```

### docker-compose.yml Example

```yaml
services:
  web:
    ports:
      - "8001:8000"
      #  │    │
      #  │    └─ Container port (inside Docker)
      #  └────── Host port (your machine)
```

**What this means:**
1. FastAPI listens on port 8000 **inside** the container
2. Docker maps it to port 8001 on **your computer**
3. You access it at: `http://localhost:8001`

### Different Port Mapping Scenarios

```yaml
# Same port on both sides
ports:
  - "8000:8000"
# Access: localhost:8000 → container:8000

# Different ports
ports:
  - "3000:8000"
# Access: localhost:3000 → container:8000

# Multiple containers
web:
  ports:
    - "8001:8000"
api:
  ports:
    - "8002:8000"
# Both containers use 8000 internally
# But exposed as 8001 and 8002 externally
```

---

## How Network Traffic Flows

### Making a Request

```
Step 1: You type in browser
http://localhost:8001/users

Step 2: Your computer thinks
"localhost = 127.0.0.1
 Port 8001
 Path /users"

Step 3: Operating system
"Which app is listening on port 8001?
 Oh, it's Docker!"

Step 4: Docker
"Port 8001 maps to container port 8000
 Forward request to container"

Step 5: Container
"FastAPI is listening on 8000
 Process request for /users"

Step 6: FastAPI
"GET /users endpoint found
 Return user data"

Step 7: Response flows back
Container → Docker → Your browser
```

---

## Port Conflicts

### The Problem

```
❌ Error: Port already in use!

Port 8001 is already allocated
```

**This happens when:**
- Another application is using the port
- Previous container didn't stop properly
- Multiple services configured for same port

### Finding What's Using a Port

```bash
# macOS/Linux: Find process on port 8001
lsof -ti:8001

# Output: 12345 (process ID)

# Get process details
lsof -i:8001

# Output:
COMMAND   PID    USER   FD   TYPE     DEVICE SIZE/OFF NODE NAME
python    12345  user   3u   IPv4   0x...        0t0  TCP *:8001
```

### Killing a Process on a Port

```bash
# macOS/Linux
lsof -ti:8001 | xargs kill -9

# Or find and kill manually
kill -9 12345  # Replace 12345 with actual PID
```

### Changing the Port

```yaml
# docker-compose.yml
services:
  web:
    ports:
      - "8002:8000"  # Use 8002 instead
```

---

## URL Anatomy

```
https://api.example.com:443/v1/users/123?active=true#top
└─┬─┘  └──────┬──────┘└┬┘└┬┘└──┬──┘└─┬─┘└─────┬──────┘└┬┘
  │         Domain    Port│  Path  │   Query String   │
Protocol              │Version│   Resource         Fragment
              Default: 443│  Endpoint
                 (HTTPS)  │
                    API Version
```

### Protocol Defaults

```
http://example.com     = http://example.com:80
https://example.com    = https://example.com:443

# Port is optional when using defaults
http://example.com:80  → Usually just write: http://example.com
```

---

## Common Networking Terms

### Localhost
```
localhost = 127.0.0.1
"This computer"
```

### Host
```
The computer running Docker
"Your machine"
```

### Container
```
Isolated environment inside Docker
"Virtual computer"
```

### Bind/Listen
```
"I'm ready to receive connections on this port"

Example: "FastAPI is listening on 0.0.0.0:8000"
```

### Expose
```
Make a port accessible outside the container
```

---

## In This Project

### Our Port Configuration

```yaml
# docker-compose.yml
services:
  web:
    ports:
      - "8001:8000"
```

**Means:**
- FastAPI runs on port 8000 **inside container**
- Accessible on port 8001 **on your machine**
- Access via: `http://localhost:8001`

### Why Not Just Use 8000?

We use 8001 because:
1. Port 8000 might be used by other apps
2. Demonstrates port mapping concept
3. Avoids conflicts in development

**You can change it to 8000:**
```yaml
ports:
  - "8000:8000"  # Access at localhost:8000
```

---

## Troubleshooting Port Issues

### Issue: Can't Access Application

**Check 1: Is Docker running?**
```bash
docker ps
```

**Check 2: Is container running?**
```bash
docker-compose ps
```

**Check 3: Correct port?**
```bash
# Check docker-compose.yml
# Use the HOST port (left side)
ports:
  - "8001:8000"  # Use 8001
```

**Check 4: Correct address?**
```bash
# Try both
curl http://localhost:8001
curl http://127.0.0.1:8001
```

### Issue: Port Already in Use

**Solution 1: Kill the process**
```bash
lsof -ti:8001 | xargs kill -9
```

**Solution 2: Use different port**
```yaml
# docker-compose.yml
ports:
  - "8002:8000"  # Use 8002 instead
```

**Solution 3: Stop other containers**
```bash
docker-compose down
docker ps -a
docker rm container_id
```

---

## Practice Exercise

### Challenge: Port Configuration

Given this docker-compose.yml:
```yaml
services:
  web:
    ports:
      - "3000:8000"
  db:
    ports:
      - "5433:5432"
```

**Questions:**
1. What URL accesses the web app?
2. What port is FastAPI listening on inside the container?
3. What port does PostgreSQL use inside its container?
4. What port connects to PostgreSQL from your machine?

**Answers:**
```
1. http://localhost:3000
2. Port 8000
3. Port 5432
4. Port 5433
```

---

## Key Takeaways

✅ Ports are like apartment numbers for network connections  
✅ localhost and 127.0.0.1 mean "this computer"  
✅ Docker maps host ports to container ports  
✅ Format: `host_port:container_port`  
✅ Port conflicts happen when two apps use the same port  
✅ Use `lsof` to find what's using a port  
✅ Default HTTP port is 80, HTTPS is 443  

---

## Next Steps

- Learn about [Docker Basics](../guides/docker-basics.md)
- Understand [Docker Compose](../guides/docker-compose.md)
- Practice [Troubleshooting](../references/troubleshooting.md)

---

**Questions or Feedback?**  
Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
