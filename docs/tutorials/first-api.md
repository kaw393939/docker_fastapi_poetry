# Tutorial: Your First API

## What You'll Learn

In this tutorial, you'll:
- ✅ Set up your development environment
- ✅ Run the FastAPI application
- ✅ Make your first API request
- ✅ Understand what's happening behind the scenes

**Time:** 15-20 minutes  
**Level:** Beginner  
**Prerequisites:** Docker installed

---

## Step 1: Clone and Open the Project

### Clone the Repository

```bash
git clone git@github.com:kaw393939/docker_fastapi_poetry.git
cd docker_fastapi_poetry
```

### Explore the Structure

```bash
# View project files
ls -la

# You should see:
├── app/              # Application code
│   ├── __init__.py
│   └── main.py       # Main FastAPI app
├── tests/            # Test files
├── Dockerfile        # Docker build instructions
├── docker-compose.yml # Docker orchestration
└── pyproject.toml    # Dependencies
```

### Open in VS Code

```bash
code .
```

---

## Step 2: Start the Application

### Start Docker Container

```bash
docker-compose up
```

**What you'll see:**
```
Creating network "docker_fastapi_poetry_default" with the default driver
Creating docker_fastapi_poetry_web_1 ... done
Attaching to docker_fastapi_poetry_web_1
web_1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
web_1  | INFO:     Started reloader process [1] using statreload
web_1  | INFO:     Started server process [8]
web_1  | INFO:     Waiting for application startup.
web_1  | INFO:     Application startup complete.
```

**What's happening:**
1. Docker builds the image (first time only)
2. Installs dependencies using Poetry
3. Starts Uvicorn web server
4. App listens on port 8000 (inside container)
5. Mapped to port 8001 (on your machine)

---

## Step 3: Test Your First Endpoint

### Open a New Terminal

Keep the first terminal running, open a second one.

### Test with curl

```bash
curl http://localhost:8001/
```

**Expected Response:**
```json
{"message":"Hello World"}
```

**Congratulations! 🎉** You just made your first API request!

---

## Step 4: Understand What Happened

Let's break down what just occurred:

```
┌────────────┐                           ┌──────────────┐
│  You       │                           │   Docker     │
│  Terminal  │                           │  Container   │
└─────┬──────┘                           └──────┬───────┘
      │                                         │
      │ 1. curl http://localhost:8001/          │
      ├────────────────────────────────────────>│
      │                                         │
      │                                    2. Uvicorn receives
      │                                       request on port 8000
      │                                         │
      │                                    3. FastAPI routes
      │                                       to GET / endpoint
      │                                         │
      │                                    4. main.py returns
      │                                       {"message":"Hello World"}
      │                                         │
      │ 5. {"message":"Hello World"}            │
      │<────────────────────────────────────────┤
      │                                         │
```

### The Journey of Your Request

**1. You send HTTP request**
```bash
curl http://localhost:8001/
```

**2. Your OS forwards to Docker**
- Sees "localhost:8001"
- Maps to container port 8000

**3. Uvicorn (web server) receives**
```
INFO:     127.0.0.1:54321 - "GET / HTTP/1.1" 200 OK
```

**4. FastAPI routes to endpoint**
```python
@app.get("/")
async def read_root():
    return {"message": "Hello World"}
```

**5. Response travels back**
```
Container → Docker → Your Terminal
```

---

## Step 5: Explore the Interactive Documentation

FastAPI automatically generates interactive API documentation!

### Open Swagger UI

1. Open your browser
2. Navigate to: http://localhost:8001/docs

**What you'll see:**
- List of all endpoints
- Try out functionality
- Request/response schemas

### Try the Health Check

1. Find the `GET /health` endpoint
2. Click "Try it out"
3. Click "Execute"

**Expected Response:**
```json
{
  "status": "healthy"
}
```

### Test with ReDoc

Alternative documentation style:
- Navigate to: http://localhost:8001/redoc

---

## Step 6: Test the Health Endpoint

### Using curl

```bash
curl http://localhost:8001/health
```

**Expected Response:**
```json
{"status":"healthy"}
```

### Understanding Health Checks

Health endpoints help monitoring systems know if your app is working:

```python
@app.get("/health")
async def health_check():
    """
    Simple health check endpoint.
    Returns 200 OK if the application is running.
    """
    return {"status": "healthy"}
```

**Common uses:**
- Load balancers: "Is this instance healthy?"
- Monitoring: "Is the app up?"
- Deployment: "Is new version ready?"

---

## Step 7: Watch the Logs

### Understanding Server Logs

In your first terminal (where docker-compose is running), you'll see:

```
web_1  | INFO:     127.0.0.1:54321 - "GET / HTTP/1.1" 200 OK
web_1  | INFO:     127.0.0.1:54322 - "GET /health HTTP/1.1" 200 OK
```

**What each part means:**
```
INFO:     127.0.0.1:54321  - "GET / HTTP/1.1" 200 OK
│         │                  │    │            │
│         │                  │    │            └─ Status code
│         │                  │    └───────────── URL path
│         │                  └────────────────── HTTP method
│         └───────────────────────────────────── Client IP
└─────────────────────────────────────────────── Log level
```

---

## Step 8: Make Changes (Hot Reload)

One of Docker's coolest features: **live code updates**!

### Edit the Code

Open `app/main.py` and change:

```python
@app.get("/")
async def read_root():
    return {"message": "Hello World"}
```

To:

```python
@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}
```

### Watch the Magic

In your docker-compose terminal, you'll see:

```
web_1  | INFO:     Detected file change in 'app/main.py'
web_1  | INFO:     Reloading...
web_1  | INFO:     Application startup complete.
```

### Test the Change

```bash
curl http://localhost:8001/
```

**New Response:**
```json
{"message":"Hello from FastAPI!"}
```

**No rebuild needed!** 🚀

---

## Step 9: View Different Output Formats

### Pretty Print with jq

```bash
# Install jq (if not already)
brew install jq

# Format JSON nicely
curl http://localhost:8001/ | jq

# Output:
{
  "message": "Hello from FastAPI!"
}
```

### View Headers

```bash
curl -i http://localhost:8001/

# Output:
HTTP/1.1 200 OK
date: Mon, 21 Oct 2025 12:00:00 GMT
server: uvicorn
content-length: 35
content-type: application/json

{"message":"Hello from FastAPI!"}
```

### Verbose Mode (Debug)

```bash
curl -v http://localhost:8001/

# Shows:
# - Connection details
# - Request headers sent
# - Response headers received
# - Response body
```

---

## Step 10: Stop the Application

### Graceful Shutdown

In your docker-compose terminal, press:
```
Ctrl+C
```

**What you'll see:**
```
Gracefully stopping... (press Ctrl+C again to force)
Stopping docker_fastapi_poetry_web_1 ... done
```

### Clean Up Containers

```bash
docker-compose down
```

**What this does:**
- Stops all containers
- Removes containers
- Removes networks
- Keeps images (for faster restart)

### Full Clean Up

```bash
# Remove everything including images
docker-compose down --rmi all

# Remove volumes too
docker-compose down -v
```

---

## Common Issues & Solutions

### Issue: Port 8001 Already in Use

**Error:**
```
Error starting userland proxy: listen tcp4 0.0.0.0:8001: bind: address already in use
```

**Solution 1:** Kill the process on that port
```bash
lsof -ti:8001 | xargs kill -9
```

**Solution 2:** Use a different port
```yaml
# docker-compose.yml
ports:
  - "8002:8000"  # Use 8002 instead
```

### Issue: Docker Not Running

**Error:**
```
Cannot connect to the Docker daemon
```

**Solution:**
```bash
# Start Docker Desktop
open -a Docker
```

### Issue: Changes Not Reflecting

**Problem:** Code changes don't appear in the app

**Solution:** Restart with rebuild
```bash
docker-compose down
docker-compose up --build
```

---

## What You Learned

✅ Started a Docker container with docker-compose  
✅ Made HTTP requests with curl  
✅ Understood request/response flow  
✅ Used interactive API documentation  
✅ Modified code with hot reload  
✅ Read and understood server logs  
✅ Gracefully stopped the application  

---

## Next Steps

Now that you have the basics, try:

1. **Add a new endpoint**
   - Tutorial: [Creating Your First Endpoint](first-endpoint.md)

2. **Write tests**
   - Tutorial: [Writing Your First Test](first-test.md)

3. **Learn FastAPI features**
   - Guide: [FastAPI Patterns](../guides/fastapi-patterns.md)

4. **Deploy to production**
   - Guide: [Deployment Guide](../guides/deployment.md)

---

## Challenge Exercise

### Create a `/about` Endpoint

**Goal:** Add a new endpoint that returns information about the API

**Steps:**
1. Open `app/main.py`
2. Add a new function:
```python
@app.get("/about")
async def about():
    return {
        "name": "FastAPI Tutorial",
        "version": "1.0.0",
        "description": "Learning FastAPI with Docker"
    }
```
3. Test it:
```bash
curl http://localhost:8001/about
```

**Expected Result:**
```json
{
  "name": "FastAPI Tutorial",
  "version": "1.0.0",
  "description": "Learning FastAPI with Docker"
}
```

---

**Questions or Stuck?**  
Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)

**Completed the tutorial?**  
Great job! 🎉 Move on to [Creating Your First Endpoint](first-endpoint.md)
