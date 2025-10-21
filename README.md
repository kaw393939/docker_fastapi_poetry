# FastAPI + Docker + Poetry: Complete Educational Guide

> **A comprehensive, production-ready FastAPI application demonstrating modern Python development with Docker containerization, dependency management with Poetry, and automated testing with pytest.**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-latest-blue.svg?logo=docker)](https://www.docker.com/)
[![Poetry](https://img.shields.io/badge/poetry-1.7+-blue.svg?logo=poetry)](https://python-poetry.org/)
[![pytest](https://img.shields.io/badge/pytest-passing-green.svg)](https://docs.pytest.org/)

---

## 📚 **Table of Contents**

1. [Project Overview](#-project-overview)
2. [Core Concepts Explained](#-core-concepts-explained)
   - [REST APIs](#rest-apis)
   - [HTTP Methods](#http-methods)
   - [HTTP Status Codes](#http-status-codes)
   - [Ports & Networking](#ports--networking)
3. [Technologies Deep Dive](#-technologies-deep-dive)
4. [Project Structure](#-project-structure)
5. [File-by-File Explanation](#-file-by-file-explanation)
6. [Prerequisites & Setup](#-prerequisites--setup)
7. [Getting Started](#-getting-started)
8. [Testing with curl](#-testing-with-curl)
9. [Development Workflow](#-development-workflow)
10. [Running Tests](#-running-tests)
11. [Docker Explained](#-docker-explained)
12. [Common Commands](#-common-commands)
13. [Troubleshooting](#-troubleshooting)
14. [Next Steps](#-next-steps)

---

## 🎯 **Project Overview**

This project is a **Hello World** FastAPI application that demonstrates professional Python development practices. It's designed to teach you:

- **REST API Development** with FastAPI
- **Containerization** with Docker
- **Dependency Management** with Poetry
- **Automated Testing** with pytest
- **Development Workflows** with hot-reloading
- **HTTP Protocols** and client-server communication

### What You'll Learn

By studying this project, you'll understand:

✅ How to build a REST API from scratch  
✅ How Docker containers work and why they're useful  
✅ How to manage Python dependencies professionally  
✅ How to write and run automated tests  
✅ How HTTP requests and responses work  
✅ How to use curl to test APIs  
✅ How ports enable network communication  

---

## 🧠 **Core Concepts Explained**

### REST APIs

**REST (Representational State Transfer)** is an architectural style for building web services. Think of it like a waiter in a restaurant:

- **Client (You)**: Makes requests (orders food)
- **Server (Kitchen)**: Processes requests and sends responses (prepares food)
- **API**: The menu and ordering system (defines what you can request)

```
┌─────────┐                    ┌─────────┐
│ Client  │ ─── HTTP Request ──▶│ Server  │
│ (curl)  │                    │(FastAPI)│
│         │◀── HTTP Response ───│         │
└─────────┘                    └─────────┘
```

**Key Characteristics of REST:**
1. **Stateless**: Each request is independent (server doesn't remember previous requests)
2. **Resource-Based**: Everything is a resource (users, products, etc.) with a URL
3. **Standard Methods**: Uses HTTP methods (GET, POST, PUT, DELETE)
4. **JSON Format**: Data typically exchanged in JSON format

### HTTP Methods

HTTP methods (also called "verbs") tell the server what action to perform:

| Method | Purpose | Example | Analogy |
|--------|---------|---------|---------|
| **GET** | Retrieve data | Get user profile | Reading a book |
| **POST** | Create new data | Create new user | Writing a new chapter |
| **PUT** | Update existing data | Update user email | Editing a chapter |
| **DELETE** | Remove data | Delete user account | Tearing out a chapter |
| **PATCH** | Partial update | Update just the name | Correcting a typo |

**In This Project:**
- `GET /` - Retrieves a hello message
- `GET /health` - Checks if the server is running

### HTTP Status Codes

Status codes tell you if your request succeeded or failed:

| Code | Meaning | Example |
|------|---------|---------|
| **2xx** | Success | Request completed successfully |
| **200** | OK | Everything worked perfectly |
| **201** | Created | New resource was created |
| **3xx** | Redirection | Resource moved somewhere else |
| **4xx** | Client Error | You made a mistake |
| **400** | Bad Request | Invalid data sent |
| **404** | Not Found | Resource doesn't exist |
| **5xx** | Server Error | Server messed up |
| **500** | Internal Server Error | Server crashed |

**Think of it like ordering food:**
- **200 OK**: Your food arrived perfectly
- **404 Not Found**: The dish isn't on the menu
- **500 Server Error**: The kitchen is on fire

### Ports & Networking

**Ports** are like apartment numbers in a building:

- **IP Address**: The building address (e.g., `127.0.0.1` = your computer)
- **Port**: The apartment number (e.g., `:8001`)
- **Full Address**: `http://127.0.0.1:8001`

```
Your Computer (127.0.0.1)
├── Port 80: Web Server
├── Port 443: Secure Web Server
├── Port 3306: MySQL Database
├── Port 5432: PostgreSQL
└── Port 8001: Our FastAPI App ⬅️ This project
```

**Common Ports:**
- **80**: HTTP (web browsing)
- **443**: HTTPS (secure web browsing)
- **22**: SSH (remote server access)
- **3000**: React development server
- **5000**: Flask default
- **8000/8001**: Common for development servers

**In This Project:**
- **Container Port 8000**: Where FastAPI listens inside Docker
- **Host Port 8001**: Where you access it on your machine
- **Port Mapping**: `8001:8000` means "forward port 8001 to 8000"

---

## 🛠 **Technologies Deep Dive**

### 1. FastAPI

**What is it?**  
FastAPI is a modern, high-performance Python web framework for building APIs.

**Why FastAPI?**
- ⚡ **Fast**: Performance comparable to NodeJS and Go
- 📝 **Auto-docs**: Generates interactive API documentation automatically
- 🔍 **Type Safety**: Uses Python type hints for validation
- 🚀 **Modern**: Built on modern Python features (async/await)
- 📖 **Easy to Learn**: Intuitive and well-documented

**Real-World Uses:**
- Building REST APIs for web/mobile apps
- Microservices architecture
- Machine learning model serving
- Real-time data processing

**In This Project:** [`app/main.py`](#appmainpy)

### 2. Uvicorn

**What is it?**  
An ASGI web server that runs your FastAPI application.

**The Stack:**
```
Request → Uvicorn → FastAPI → Your Code → Response
```

**Key Features:**
- Runs FastAPI applications
- Supports async/await
- Hot-reloading for development (`--reload` flag)
- Production-ready performance

**Think of it as:**  
If FastAPI is your restaurant kitchen, Uvicorn is the building that houses it.

**In This Project:** Started via Docker in [`docker-compose.yml`](#docker-composeyml)

### 3. Poetry

**What is it?**  
A modern dependency manager for Python projects.

**Problems It Solves:**

**Before Poetry** (old way):
```
requirements.txt    # Production dependencies
requirements-dev.txt # Development dependencies
setup.py           # Package configuration
MANIFEST.in        # File inclusion
setup.cfg          # Additional config
```

**With Poetry** (new way):
```
pyproject.toml     # Everything in one file!
poetry.lock        # Auto-generated lock file
```

**Key Benefits:**
- 📦 **One File**: All config in `pyproject.toml`
- 🔒 **Lock File**: Ensures everyone uses same versions
- 🎯 **Smart Resolution**: Handles dependency conflicts
- 🚀 **Easy Commands**: `poetry add`, `poetry install`

**In This Project:** [`pyproject.toml`](#pyprojecttoml)

### 4. Docker

**What is it?**  
A platform for running applications in isolated containers.

**The Problem:**
```
Developer: "It works on my machine!"
Production: "It doesn't work here!"
```

**The Solution:**
```
Docker Container = Your app + All dependencies + Operating system
```

**Analogy:**  
Shipping containers revolutionized cargo shipping by standardizing how goods are transported. Docker does the same for software.

```
┌─────────────────────────────┐
│     Docker Container        │
│  ┌─────────────────────┐   │
│  │   Your FastAPI App  │   │
│  ├─────────────────────┤   │
│  │   Python 3.11       │   │
│  ├─────────────────────┤   │
│  │   All Dependencies  │   │
│  ├─────────────────────┤   │
│  │   Linux OS          │   │
│  └─────────────────────┘   │
└─────────────────────────────┘
```

**Key Concepts:**

1. **Image**: Blueprint/Template (like a recipe)
2. **Container**: Running instance (like a cooked dish)
3. **Dockerfile**: Instructions to build an image
4. **Volume**: Shared folder between host and container

**In This Project:** [`Dockerfile`](#dockerfile)

### 5. Docker Compose

**What is it?**  
A tool for defining and running multi-container Docker applications.

**Why Use It?**

**Without Docker Compose:**
```bash
# Build image
docker build -t myapp .

# Run container with long command
docker run -p 8001:8000 -v $(pwd):/app -e PYTHONUNBUFFERED=1 myapp
```

**With Docker Compose:**
```bash
# Everything defined in docker-compose.yml
docker-compose up
```

**Benefits:**
- 📝 Configuration as code
- 🎯 One command to start everything
- 🔗 Easy multi-service setup (app + database + cache)
- 🔄 Simple restart and rebuild

**In This Project:** [`docker-compose.yml`](#docker-composeyml)

### 6. pytest

**What is it?**  
A Python testing framework that makes writing tests simple.

**Why Test?**
- ✅ Catch bugs before users do
- 🔒 Ensure changes don't break existing features
- 📖 Tests serve as documentation
- 🚀 Confidence to refactor code

**Testing Pyramid:**
```
      /\
     /  \  E2E Tests (Few)
    /────\
   /      \ Integration Tests (Some)
  /────────\
 /          \ Unit Tests (Many)
/────────────\
```

**In This Project:** [`tests/test_main.py`](#teststest_mainpy)

---

## 📁 **Project Structure**

```
218docker/
│
├── 📄 .dockerignore          # Files to exclude from Docker build
├── 📄 .gitignore             # Files to exclude from version control
├── 📄 Dockerfile             # Instructions to build Docker image
├── 📄 docker-compose.yml     # Multi-container configuration
├── 📄 pyproject.toml         # Poetry dependencies & config
├── 📄 poetry.lock            # Locked dependency versions
├── 📄 README.md              # This file
│
├── 📁 app/                   # Application package
│   ├── 📄 __init__.py        # Makes 'app' a Python package
│   └── 📄 main.py            # FastAPI app & routes
│
└── 📁 tests/                 # Test package
    ├── 📄 __init__.py        # Makes 'tests' a Python package
    └── 📄 test_main.py       # API endpoint tests
```

---

## 📝 **File-by-File Explanation**

### `app/main.py`

**Purpose:** The heart of your application - defines the FastAPI app and all routes.

**What's Inside:**
```python
from fastapi import FastAPI

app = FastAPI(title="Hello World API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

**Line-by-Line:**
1. **Import FastAPI**: Brings in the FastAPI class
2. **Create app instance**: `app = FastAPI()` creates your application
3. **@app.get("/")**:  Decorator that says "when GET request comes to /, run this function"
4. **async def root()**: Asynchronous function (non-blocking)
5. **return {...}**: FastAPI automatically converts dict to JSON

**Why async?**  
Allows handling multiple requests simultaneously without blocking.

[View full file with detailed comments →](app/main.py)

### `app/__init__.py`

**Purpose:** Makes the `app` directory a Python package.

**What is a Package?**  
A directory with `__init__.py` that you can import from:
```python
from app.main import app  # This works because __init__.py exists
```

**This file can be empty!** It just needs to exist.

[View full file with detailed comments →](app/__init__.py)

### `tests/test_main.py`

**Purpose:** Contains automated tests for your API.

**What's Inside:**
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

**How Tests Work:**
1. **TestClient**: Simulates HTTP requests without running a server
2. **client.get("/")**: Makes a fake GET request
3. **assert**: Checks if condition is true; test fails if false

**Running Tests:**
```bash
poetry run pytest         # Run all tests
poetry run pytest -v      # Verbose output
```

[View full file with detailed comments →](tests/test_main.py)

### `tests/__init__.py`

**Purpose:** Makes the `tests` directory a Python package for pytest to discover.

[View full file with detailed comments →](tests/__init__.py)

### `Dockerfile`

**Purpose:** Instructions to build a Docker image.

**What's Inside:**
```dockerfile
FROM python:3.11-slim       # Start with Python base image
WORKDIR /app                # Set working directory
RUN pip install poetry      # Install Poetry
COPY pyproject.toml ./      # Copy dependency file
RUN poetry install          # Install dependencies
COPY . .                    # Copy application code
CMD ["uvicorn", ...]        # Command to run app
```

**How It Works:**
Each line creates a "layer" in the image. Docker caches layers for faster rebuilds.

**Layer Caching Example:**
```
Change app/main.py    → Only rebuild from COPY . .
Change pyproject.toml → Rebuild from RUN poetry install
```

[View full file with detailed comments →](Dockerfile)

### `docker-compose.yml`

**Purpose:** Defines how to run containers for development.

**What's Inside:**
```yaml
services:
  web:                    # Service name
    build: .             # Build from Dockerfile
    ports:
      - "8001:8000"      # Port mapping
    volumes:
      - .:/app           # Mount code for hot-reload
    command: uvicorn app.main:app --reload
```

**Key Sections:**
- **ports**: `"8001:8000"` means "map host port 8001 to container port 8000"
- **volumes**: `- .:/app` shares your code with container
- **command**: Overrides Dockerfile CMD (adds --reload for dev)

[View full file with detailed comments →](docker-compose.yml)

### `pyproject.toml`

**Purpose:** Defines project metadata and dependencies.

**What's Inside:**
```toml
[tool.poetry]
name = "fastapi-app"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.104.1"
uvicorn = {extras = ["standard"], version = "^0.24.0"}

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.3"
httpx = "^0.25.1"
```

**Version Syntax:**
- `^0.104.1` means `>=0.104.1, <0.105.0`
- `~0.104.1` means `>=0.104.1, <0.105.0`
- `>=0.104.1` means any version ≥ 0.104.1

[View full file with detailed comments →](pyproject.toml)

### `.dockerignore`

**Purpose:** Tells Docker which files to ignore when building images.

**Why?**  
Keeps image size small and build faster.

```
__pycache__/
*.pyc
.git/
.venv/
```

Similar to `.gitignore` but for Docker.

[View full file →](.dockerignore)

### `.gitignore`

**Purpose:** Tells Git which files not to track.

**Why?**  
Avoid committing:
- Auto-generated files (`__pycache__/`)
- Dependencies (`node_modules/`, `.venv/`)
- Sensitive data (`.env` files)
- OS files (`.DS_Store`)

[View full file →](.gitignore)

---

## 📋 **Prerequisites & Setup**

### Required Software

#### 1. Docker Desktop

**What:** Includes Docker Engine + Docker Compose

**Download:** https://www.docker.com/products/docker-desktop

**Installation:**
```bash
# macOS
brew install --cask docker

# Or download from website and install

# Verify installation
docker --version
docker-compose --version
```

**Start Docker Desktop:**
- macOS: Open from Applications or menu bar
- The Docker icon should appear in your system tray

#### 2. Python 3.11+ (for local development)

**Download:** https://www.python.org/downloads/

**Installation:**
```bash
# macOS with Homebrew
brew install python@3.11

# Verify
python --version  # Should show 3.11+
```

#### 3. Poetry (for local development)

**Installation:**
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add to PATH (macOS/Linux - add to ~/.zshrc or ~/.bashrc)
export PATH="$HOME/.local/bin:$PATH"

# Apply changes
source ~/.zshrc  # or source ~/.bashrc

# Verify
poetry --version
```

#### 4. curl (for testing APIs)

**Usually pre-installed on macOS/Linux**

```bash
# Verify
curl --version

# If not installed (Linux)
sudo apt-get install curl  # Ubuntu/Debian
sudo yum install curl      # CentOS/RHEL
```

### Optional Tools

- **Postman**: GUI for API testing (https://www.postman.com/)
- **HTTPie**: User-friendly curl alternative (`pip install httpie`)
- **jq**: JSON processor for pretty output (`brew install jq`)

---

## 🚀 **Getting Started**

### Option 1: Using Docker (Recommended for Beginners)

This approach ensures everything works identically on all systems.

#### Step 1: Clone/Navigate to Project
```bash
cd /path/to/218docker
```

#### Step 2: Ensure Docker is Running
Check that Docker Desktop is running:
```bash
docker ps
# Should show running containers (or empty list, not an error)
```

#### Step 3: Build and Start
```bash
# Build image and start container
docker-compose up --build

# Or run in background (detached mode)
docker-compose up --build -d
```

**What Happens:**
1. Docker reads `Dockerfile`
2. Builds image with Python + dependencies
3. Creates container from image
4. Starts Uvicorn server
5. Maps port 8001 (your computer) → 8000 (container)

#### Step 4: Verify It's Running
Open browser and visit:
- **API**: http://localhost:8001/
- **Interactive Docs**: http://localhost:8001/docs
- **Alternative Docs**: http://localhost:8001/redoc

Or use curl:
```bash
curl http://localhost:8001/
# Expected: {"message":"Hello World"}
```

#### Step 5: View Logs
```bash
# See what's happening
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# View last 50 lines
docker-compose logs --tail=50
```

#### Step 6: Stop the Application
```bash
# Stop and remove containers
docker-compose down

# Just stop (containers persist)
docker-compose stop

# Restart stopped containers
docker-compose start
```

### Option 2: Local Development (Advanced)

For faster iteration and easier debugging.

#### Step 1: Install Dependencies
```bash
cd /path/to/218docker

# Install all dependencies
poetry install

# This creates a virtual environment and installs:
# - FastAPI
# - Uvicorn
# - pytest
# - httpx
```

#### Step 2: Activate Virtual Environment (Optional)
```bash
# Option A: Use poetry shell
poetry shell

# Option B: Use poetry run for each command
poetry run <command>
```

#### Step 3: Run the Application
```bash
# If you ran 'poetry shell'
uvicorn app.main:app --reload

# If not, prefix with 'poetry run'
poetry run uvicorn app.main:app --reload
```

**Server Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Application startup complete.
```

#### Step 4: Test the API
Visit http://localhost:8000/ or use curl:
```bash
curl http://localhost:8000/
curl http://localhost:8000/health
```

#### Step 5: Run Tests
```bash
# Basic test run
poetry run pytest

# Verbose output
poetry run pytest -v

# With coverage report
poetry run pytest --cov=app

# Generate HTML coverage report
poetry run pytest --cov=app --cov-report=html
open htmlcov/index.html
```

---

## 🧪 **Testing with curl**

**curl** is a command-line tool for making HTTP requests. It's essential for API testing.

### Basic curl Syntax

```bash
curl [OPTIONS] [URL]
```

### Testing Our API

#### 1. Simple GET Request
```bash
curl http://localhost:8001/

# Response:
{"message":"Hello World"}
```

#### 2. Pretty Print JSON (with jq)
```bash
curl http://localhost:8001/ | jq

# Response (formatted):
{
  "message": "Hello World"
}
```

#### 3. Include Response Headers
```bash
curl -i http://localhost:8001/

# Response:
HTTP/1.1 200 OK
date: Mon, 21 Oct 2025 12:00:00 GMT
server: uvicorn
content-length: 27
content-type: application/json

{"message":"Hello World"}
```

#### 4. Verbose Output (See Full Request/Response)
```bash
curl -v http://localhost:8001/

# Shows:
# > GET / HTTP/1.1          (Request headers)
# > Host: localhost:8001
# > User-Agent: curl/7.79.1
# > Accept: */*
# >
# < HTTP/1.1 200 OK         (Response headers)
# < date: ...
# < server: uvicorn
# < content-type: application/json
# <
# {"message":"Hello World"}  (Response body)
```

#### 5. Test Health Endpoint
```bash
curl http://localhost:8001/health

# Response:
{"status":"healthy"}
```

#### 6. Test Non-Existent Endpoint
```bash
curl http://localhost:8001/nonexistent

# Response:
{"detail":"Not Found"}

# With status code
curl -w "\nHTTP Status: %{http_code}\n" http://localhost:8001/nonexistent

# Output:
{"detail":"Not Found"}
HTTP Status: 404
```

### Advanced curl Examples

#### POST Request (for future endpoints)
```bash
curl -X POST \
  http://localhost:8001/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Item","price":9.99}'
```

**Breakdown:**
- `-X POST`: Use POST method
- `-H`: Add header
- `-d`: Send data (request body)

#### Save Response to File
```bash
curl http://localhost:8001/ -o response.json
cat response.json
```

#### Timing Request
```bash
curl -w "Time: %{time_total}s\n" http://localhost:8001/
```

### curl Cheat Sheet

| Option | Purpose | Example |
|--------|---------|---------|
| `-X METHOD` | HTTP method | `curl -X POST` |
| `-H "Header: Value"` | Add header | `curl -H "Authorization: Bearer token"` |
| `-d '{"key":"value"}'` | Send data | `curl -d '{"name":"John"}'` |
| `-i` | Include headers | `curl -i http://...` |
| `-v` | Verbose output | `curl -v http://...` |
| `-o file` | Save to file | `curl -o out.json http://...` |
| `-w FORMAT` | Custom output | `curl -w "%{http_code}"` |

---

## 💻 **Development Workflow**

### Making Code Changes

#### With Docker (Hot-Reload Enabled)

1. **Start container:**
   ```bash
   docker-compose up
   ```

2. **Edit code:**
   Open `app/main.py` and add a new endpoint:
   ```python
   @app.get("/hello/{name}")
   async def greet(name: str):
       return {"greeting": f"Hello, {name}!"}
   ```

3. **Save file** - Uvicorn automatically detects and reloads!

4. **Test immediately:**
   ```bash
   curl http://localhost:8001/hello/Alice
   # {"greeting":"Hello, Alice!"}
   ```

**How It Works:**
The volume mount in `docker-compose.yml` shares your code:
```yaml
volumes:
  - .:/app  # Current directory → /app in container
```

Changes to files are instantly visible inside the container.

#### Without Docker (Local Development)

1. **Run with --reload:**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

2. **Edit code** and save

3. **Server auto-restarts** - Test your changes

### Adding New Dependencies

#### Using Poetry

1. **Add dependency:**
   ```bash
   # Production dependency
   poetry add requests

   # Development dependency
   poetry add --group dev black
   ```

2. **Poetry automatically:**
   - Updates `pyproject.toml`
   - Updates `poetry.lock`
   - Installs the package

3. **If using Docker, rebuild:**
   ```bash
   docker-compose down
   docker-compose up --build
   ```

### Adding New Endpoints

#### Example: Create a User Endpoint

1. **Edit `app/main.py`:**
   ```python
   from pydantic import BaseModel

   class User(BaseModel):
       name: str
       email: str
       age: int

   @app.post("/users")
   async def create_user(user: User):
       return {"user": user, "created": True}
   ```

2. **Test with curl:**
   ```bash
   curl -X POST http://localhost:8001/users \
     -H "Content-Type: application/json" \
     -d '{"name":"Alice","email":"alice@example.com","age":30}'
   ```

3. **Add test in `tests/test_main.py`:**
   ```python
   def test_create_user():
       response = client.post(
           "/users",
           json={"name": "Alice", "email": "alice@example.com", "age": 30}
       )
       assert response.status_code == 200
       assert response.json()["created"] is True
   ```

4. **Run tests:**
   ```bash
   poetry run pytest -v
   ```

---

## ✅ **Running Tests**

### In Docker Container

```bash
# Run tests in running container
docker-compose exec web pytest

# Verbose output
docker-compose exec web pytest -v

# Stop on first failure
docker-compose exec web pytest -x

# Run specific test
docker-compose exec web pytest tests/test_main.py::test_read_root
```

### Locally with Poetry

```bash
# Run all tests
poetry run pytest

# Verbose
poetry run pytest -v

# With coverage
poetry run pytest --cov=app

# HTML coverage report
poetry run pytest --cov=app --cov-report=html
open htmlcov/index.html

# Run specific file
poetry run pytest tests/test_main.py

# Run specific test
poetry run pytest tests/test_main.py::test_read_root

# Show print statements
poetry run pytest -s
```

### Understanding Test Output

```bash
$ poetry run pytest -v

tests/test_main.py::test_read_root PASSED      [ 50%]
tests/test_main.py::test_health_check PASSED   [100%]

===================== 2 passed in 0.15s =====================
```

**Breakdown:**
- `PASSED`: Test succeeded ✅
- `FAILED`: Test failed ❌
- `[ 50%]`: Progress indicator
- `2 passed in 0.15s`: Summary

### Test Coverage

**What is it?**  
Percentage of code executed by tests.

```bash
poetry run pytest --cov=app --cov-report=term-missing

Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
app/__init__.py         0      0   100%
app/main.py            10      0   100%
-------------------------------------------------
TOTAL                  10      0   100%
```

**Aim for:** 80%+ coverage for production code

---

## 🐳 **Docker Explained**

### Docker vs Virtual Machines

```
Virtual Machine:                Docker Container:
┌───────────────┐              ┌───────────────┐
│   App         │              │   App         │
├───────────────┤              ├───────────────┤
│   Libraries   │              │   Libraries   │
├───────────────┤              ├───────────────┤
│   Guest OS    │              │   (shared)    │
├───────────────┤              └───────────────┘
│   Hypervisor  │              ┌───────────────┐
├───────────────┤              │  Docker       │
│   Host OS     │              ├───────────────┤
└───────────────┘              │   Host OS     │
                               └───────────────┘
  ~GBs, Minutes                  ~MBs, Seconds
```

### Docker Workflow

```
1. Write Dockerfile
   ↓
2. Build Image (docker build)
   ↓
3. Run Container (docker run)
   ↓
4. Use Application
```

### Key Docker Commands

```bash
# Images
docker build -t myapp .           # Build image
docker images                     # List images
docker rmi image_name             # Delete image

# Containers
docker run -p 8000:8000 myapp    # Run container
docker ps                         # List running containers
docker ps -a                      # List all containers
docker stop container_id          # Stop container
docker rm container_id            # Remove container

# Logs & Debugging
docker logs container_id          # View logs
docker exec -it container_id sh   # Open shell in container

# Cleanup
docker system prune               # Remove unused data
docker volume prune               # Remove unused volumes
```

### Docker Compose Commands

```bash
# Start services
docker-compose up                 # Start and show logs
docker-compose up -d              # Start in background
docker-compose up --build         # Rebuild and start

# Stop services
docker-compose down               # Stop and remove
docker-compose stop               # Just stop

# View status
docker-compose ps                 # List containers
docker-compose logs               # View logs
docker-compose logs -f            # Follow logs

# Execute commands
docker-compose exec web bash      # Open shell
docker-compose exec web pytest    # Run tests

# Rebuild
docker-compose build              # Rebuild images
docker-compose build --no-cache   # Force full rebuild
```

---

## 🔧 **Common Commands**

### Quick Reference

```bash
# Start development server
docker-compose up

# Start in background
docker-compose up -d

# Stop everything
docker-compose down

# Rebuild and start
docker-compose up --build

# View logs
docker-compose logs -f

# Run tests
docker-compose exec web pytest -v

# Open shell in container
docker-compose exec web bash

# Add new dependency
poetry add package-name
docker-compose up --build

# Run local server
poetry run uvicorn app.main:app --reload

# Run local tests
poetry run pytest -v
```

### Port Forwarding

```bash
# Default (port 8001)
docker-compose up

# Access at: http://localhost:8001

# Change port (edit docker-compose.yml)
ports:
  - "3000:8000"  # Access at http://localhost:3000
```

---

## 🔍 **Troubleshooting**

### Port Already in Use

**Error:**
```
Bind for 0.0.0.0:8001 failed: port is already allocated
```

**Solution:**
```bash
# Find process using port
lsof -ti:8001

# Kill process
lsof -ti:8001 | xargs kill -9

# Or use different port in docker-compose.yml
ports:
  - "8002:8000"
```

### Docker Daemon Not Running

**Error:**
```
Cannot connect to the Docker daemon
```

**Solution:**
```bash
# macOS: Start Docker Desktop
open -a Docker

# Verify
docker ps
```

### Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**
```bash
# Reinstall dependencies
poetry install

# Or rebuild Docker
docker-compose up --build
```

### Hot Reload Not Working

**Problem:** Code changes don't reflect in container

**Solution:**
```bash
# Ensure volume is mounted (check docker-compose.yml)
volumes:
  - .:/app  # Must be present

# Restart container
docker-compose restart web
```

### Poetry Not Found

**Error:**
```
zsh: command not found: poetry
```

**Solution:**
```bash
# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Make permanent (add to ~/.zshrc)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Tests Failing

**Problem:** Tests pass locally but fail in CI

**Solution:**
```bash
# Clear cache
poetry run pytest --cache-clear

# Reinstall dependencies
rm -rf .venv
poetry install
```

---

## 🎓 **Next Steps**

### Enhance This Project

#### 1. Add Database Integration
```bash
poetry add sqlalchemy databases[postgresql]
```

Update `docker-compose.yml`:
```yaml
services:
  web:
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

#### 2. Add Authentication
```bash
poetry add python-jose[cryptography] passlib[bcrypt]
```

#### 3. Add CORS for Frontend
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### 4. Add Environment Variables
```bash
poetry add python-dotenv pydantic-settings
```

#### 5. Add Logging
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

### Learning Resources

#### FastAPI
- **Official Tutorial**: https://fastapi.tiangolo.com/tutorial/
- **Full Documentation**: https://fastapi.tiangolo.com/

#### Docker
- **Get Started**: https://docs.docker.com/get-started/
- **Best Practices**: https://docs.docker.com/develop/dev-best-practices/

#### Poetry
- **Basic Usage**: https://python-poetry.org/docs/basic-usage/

#### pytest
- **Getting Started**: https://docs.pytest.org/en/stable/getting-started.html

#### REST APIs
- **REST API Tutorial**: https://restfulapi.net/
- **HTTP Methods**: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

### Practice Exercises

1. Add a new endpoint that returns the current server time
2. Create a POST endpoint that accepts user data
3. Add input validation using Pydantic models
4. Write tests for your new endpoints
5. Add error handling for invalid requests
6. Implement pagination for list endpoints
7. Add query parameters for filtering data
8. Create comprehensive API documentation

---

## 📄 **License**

MIT License - Feel free to use this project for learning and teaching.

---

## 🤝 **Contributing**

This is an educational project. Contributions that improve clarity and educational value are welcome!

---

**Made with ❤️ for teaching modern Python development practices**

**Questions? Issues? Contributions?**  
Open an issue on GitHub: https://github.com/kaw393939/docker_fastapi_poetry

---

**Happy Learning! 🚀**
