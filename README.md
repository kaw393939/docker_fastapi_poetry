# FastAPI Hello World Application - Complete Guide

A production-ready FastAPI "Hello World" application demonstrating modern Python development practices with Docker containerization, dependency management, testing, and development workflows.

## 📚 Table of Contents

1. [Technologies Overview](#technologies-overview)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Getting Started](#getting-started)
5. [Development Workflow](#development-workflow)
6. [Testing](#testing)
7. [Docker Deep Dive](#docker-deep-dive)
8. [API Documentation](#api-documentation)
9. [Troubleshooting](#troubleshooting)

---

## 🛠 Technologies Overview

### FastAPI
**What it is:** FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.

**Why we use it:**
- Automatic interactive API documentation (Swagger UI)
- High performance (comparable to NodeJS and Go)
- Type validation using Python type hints
- Easy to learn and fast to code
- Built-in async support

**In this project:** FastAPI powers our web server and handles HTTP requests/responses.

### Uvicorn
**What it is:** An ASGI (Asynchronous Server Gateway Interface) web server implementation for Python.

**Why we use it:**
- Serves FastAPI applications
- Supports async/await syntax
- Hot-reloading during development (via `--reload` flag)
- Production-ready performance

**In this project:** Uvicorn runs our FastAPI application on port 8000.

### Poetry
**What it is:** A modern dependency management and packaging tool for Python projects.

**Why we use it:**
- Deterministic dependency resolution (creates `poetry.lock`)
- Simplified dependency management (one `pyproject.toml` file)
- Virtual environment management
- Better than traditional `requirements.txt` + `setup.py`

**Key Poetry Commands:**
```bash
poetry install          # Install dependencies
poetry add <package>    # Add a new dependency
poetry remove <package> # Remove a dependency
poetry run <command>    # Run command in virtual environment
poetry shell           # Activate virtual environment
```

**In this project:** Poetry manages all our dependencies (FastAPI, Uvicorn, pytest, etc.).

### Docker
**What it is:** A platform for developing, shipping, and running applications in containers.

**Why we use it:**
- Consistent environment across development and production
- Eliminates "works on my machine" problems
- Isolated application environment
- Easy deployment and scaling

**Key Concepts:**
- **Image:** Blueprint for containers (defined in Dockerfile)
- **Container:** Running instance of an image
- **Dockerfile:** Instructions to build an image
- **Layer:** Each instruction in Dockerfile creates a layer (cached for efficiency)

**In this project:** Docker containerizes our application for consistent execution anywhere.

### Docker Compose
**What it is:** A tool for defining and running multi-container Docker applications.

**Why we use it:**
- Define entire application stack in one YAML file
- Manage multiple services (web, database, cache, etc.)
- Volume mounting for development hot-reloading
- Easy service orchestration

**Key Docker Compose Commands:**
```bash
docker-compose up        # Start services
docker-compose up -d     # Start in detached mode
docker-compose down      # Stop and remove services
docker-compose logs      # View logs
docker-compose exec      # Execute command in service
docker-compose build     # Build/rebuild services
```

**In this project:** Docker Compose orchestrates our FastAPI service with development-friendly volume mounting.

### pytest
**What it is:** A mature full-featured Python testing framework.

**Why we use it:**
- Simple and pythonic syntax
- Detailed assertion introspection
- Fixtures for test setup/teardown
- Plugin ecosystem
- Compatible with unittest and nose tests

**Key pytest Features:**
```python
# Simple test functions
def test_something():
    assert 1 + 1 == 2

# Fixtures for setup
@pytest.fixture
def client():
    return TestClient(app)

# Parametrized tests
@pytest.mark.parametrize("input,expected", [(1, 2), (2, 3)])
def test_increment(input, expected):
    assert input + 1 == expected
```

**In this project:** pytest runs our API tests using FastAPI's TestClient.

---

## 📁 Project Structure

```
218docker/
├── app/                      # Application package
│   ├── __init__.py          # Makes 'app' a Python package
│   └── main.py              # FastAPI application and route definitions
│
├── tests/                    # Test package
│   ├── __init__.py          # Makes 'tests' a Python package
│   └── test_main.py         # API endpoint tests
│
├── docker-compose.yml        # Multi-container Docker configuration
├── Dockerfile                # Docker image build instructions
├── pyproject.toml            # Poetry dependencies and project metadata
├── poetry.lock              # Locked dependency versions (auto-generated)
├── .dockerignore            # Files to exclude from Docker build
├── .gitignore               # Files to exclude from version control
└── README.md                # This file
```

### File Explanations

**`app/main.py`**
- Contains the FastAPI application instance
- Defines API routes and endpoints
- Business logic for handling requests

**`tests/test_main.py`**
- Contains test cases for API endpoints
- Uses FastAPI's TestClient for integration testing
- Validates response status codes and data

**`Dockerfile`**
- Instructions to build the Docker image
- Installs Python, Poetry, and dependencies
- Copies application code into container
- Defines the command to run the application

**`docker-compose.yml`**
- Defines the 'web' service configuration
- Maps ports (host:container)
- Mounts volumes for development
- Sets environment variables

**`pyproject.toml`**
- Modern Python project configuration file
- Lists dependencies and their versions
- Poetry configuration and metadata
- Replaces setup.py and requirements.txt

---

## 📋 Prerequisites

### Required Software

1. **Docker Desktop** (includes Docker Engine and Docker Compose)
   - Download: https://www.docker.com/products/docker-desktop
   - Verify installation:
     ```bash
     docker --version
     docker-compose --version
     ```

2. **Python 3.11+** (for local development without Docker)
   - Download: https://www.python.org/downloads/
   - Verify installation:
     ```bash
     python --version
     ```

3. **Poetry** (for local development without Docker)
   - Install:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```
   - Add to PATH (add to `~/.zshrc` or `~/.bashrc`):
     ```bash
     export PATH="$HOME/.local/bin:$PATH"
     ```
   - Verify installation:
     ```bash
     poetry --version
     ```

### System Requirements
- macOS, Linux, or Windows with WSL2
- 4GB RAM minimum (8GB recommended)
- 10GB free disk space

---

## 🚀 Getting Started

### Option 1: Using Docker (Recommended)

This is the easiest way to get started and ensures consistency across all environments.

#### Step 1: Clone or Navigate to Project
```bash
cd /path/to/218docker
```

#### Step 2: Start Docker Desktop
Make sure Docker Desktop is running (check menu bar/system tray).

#### Step 3: Build and Run
```bash
# Build the Docker image and start the container
docker-compose up --build
```

The `--build` flag forces a rebuild of the image. First build takes 1-2 minutes.

#### Step 4: Verify It's Running
Open your browser and visit:
- **API:** http://localhost:8001/
- **Interactive Docs:** http://localhost:8001/docs
- **Alternative Docs:** http://localhost:8001/redoc

Or use curl:
```bash
curl http://localhost:8001/
# Expected output: {"message":"Hello World"}
```

#### Step 5: View Logs
```bash
# View container logs
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# View last 20 lines
docker-compose logs --tail=20
```

#### Step 6: Stop the Application
```bash
# Stop and remove containers
docker-compose down

# Stop containers but keep them
docker-compose stop

# Start stopped containers
docker-compose start
```

### Option 2: Local Development (Without Docker)

For development with faster iteration cycles and direct Python debugging.

#### Step 1: Install Poetry
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add to PATH (macOS/Linux)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Verify
poetry --version
```

#### Step 2: Install Dependencies
```bash
cd /path/to/218docker

# Install all dependencies (including dev dependencies)
poetry install
```

This creates a virtual environment and installs:
- FastAPI
- Uvicorn
- pytest
- httpx (for testing)
- pytest-asyncio

#### Step 3: Run the Application
```bash
# Run with hot-reloading
poetry run uvicorn app.main:app --reload

# Or activate the virtual environment first
poetry shell
uvicorn app.main:app --reload
```

The server starts at http://localhost:8000

#### Step 4: Test the API
```bash
# In another terminal
curl http://localhost:8000/
curl http://localhost:8000/health
```

#### Step 5: Run Tests
```bash
# Run all tests
poetry run pytest

# Verbose output
poetry run pytest -v

# With coverage
poetry run pytest --cov=app

# Run specific test
poetry run pytest tests/test_main.py::test_read_root
```

---

## 💻 Development Workflow

### Making Code Changes

#### With Docker (Hot-Reload Enabled)
1. Start the container: `docker-compose up`
2. Edit any file in `app/` directory
3. Save the file
4. Uvicorn automatically detects changes and reloads
5. Test your changes immediately

**How it works:** The `docker-compose.yml` mounts your project directory as a volume:
```yaml
volumes:
  - .:/app  # Current directory mounted to /app in container
```

#### Without Docker (Local Development)
1. Start server: `poetry run uvicorn app.main:app --reload`
2. Edit files
3. Save - server auto-reloads
4. Test changes

### Adding New Dependencies

#### Using Poetry (Recommended)
```bash
# Add a production dependency
poetry add <package-name>

# Add a development dependency
poetry add --group dev <package-name>

# Examples
poetry add sqlalchemy
poetry add --group dev black  # Code formatter
poetry add --group dev mypy   # Type checker
```

This automatically updates `pyproject.toml` and `poetry.lock`.

#### Rebuild Docker Image
After adding dependencies, rebuild the Docker image:
```bash
docker-compose down
docker-compose up --build
```

### Adding New Endpoints

1. Edit `app/main.py`
2. Add a new route:
```python
@app.get("/new-endpoint")
async def new_endpoint():
    return {"data": "some data"}
```
3. Add tests in `tests/test_main.py`
4. Run tests to verify

### Project Organization Best Practices

As your project grows, organize it like this:

```
app/
├── __init__.py
├── main.py              # Application entry point
├── models.py            # Pydantic models (request/response schemas)
├── database.py          # Database connection
├── routers/             # Route modules
│   ├── __init__.py
│   ├── users.py
│   └── items.py
└── services/            # Business logic
    ├── __init__.py
    └── user_service.py
```

---

## ✅ Testing

### Understanding the Test Setup

Our tests use:
- **pytest:** Test framework
- **TestClient:** FastAPI's test client (doesn't require running server)
- **httpx:** HTTP client library (TestClient dependency)

### Running Tests

#### In Docker Container
```bash
# Run tests in the running container
docker-compose exec web pytest

# Verbose output
docker-compose exec web pytest -v

# Run specific test file
docker-compose exec web pytest tests/test_main.py

# Run specific test function
docker-compose exec web pytest tests/test_main.py::test_read_root
```

#### Locally
```bash
# Run all tests
poetry run pytest

# With coverage report
poetry run pytest --cov=app --cov-report=html

# Stop on first failure
poetry run pytest -x

# Show print statements
poetry run pytest -s
```

### Writing New Tests

Example test structure:

```python
from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)

def test_endpoint_name():
    """Test description."""
    # Arrange: Set up test data
    test_data = {"key": "value"}
    
    # Act: Make request
    response = client.post("/endpoint", json=test_data)
    
    # Assert: Verify results
    assert response.status_code == 200
    assert response.json() == {"expected": "result"}
```

### Test Coverage

Generate a coverage report:
```bash
poetry run pytest --cov=app --cov-report=html
open htmlcov/index.html  # View in browser
```

---

## 🐳 Docker Deep Dive

### Understanding the Dockerfile

Our Dockerfile uses a multi-stage approach optimized for Python development:

```dockerfile
# Base image - Python 3.11 slim version (smaller size)
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Configure Poetry not to create virtual environments
# (not needed in containers)
RUN poetry config virtualenvs.create false

# Copy dependency files first (for layer caching)
COPY pyproject.toml poetry.lock* ./

# Install dependencies (cached if files unchanged)
RUN poetry install --no-interaction --no-ansi

# Copy application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

**Layer Caching:** Docker caches each layer. If `pyproject.toml` doesn't change, dependencies aren't reinstalled (faster builds).

### Understanding docker-compose.yml

```yaml
services:
  web:                          # Service name
    build: .                    # Build from Dockerfile in current directory
    ports:
      - "8001:8000"            # Map host port 8001 to container port 8000
    volumes:
      - .:/app                  # Mount current directory to /app (hot-reload)
      - /app/.venv              # Prevent overwriting Python virtual env
    environment:
      - PYTHONUNBUFFERED=1      # See Python output in real-time
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Docker Commands Cheat Sheet

```bash
# Build and start services
docker-compose up --build

# Start in background (detached mode)
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Execute command in running container
docker-compose exec web bash              # Open shell
docker-compose exec web pytest            # Run tests
docker-compose exec web poetry add <pkg>  # Add package

# View running containers
docker ps

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Rebuild without cache
docker-compose build --no-cache

# View resource usage
docker stats
```

### Troubleshooting Docker Issues

**Port already in use:**
```bash
# Find process using port
lsof -ti:8001

# Kill process
lsof -ti:8001 | xargs kill -9

# Or change port in docker-compose.yml
ports:
  - "8002:8000"  # Use different host port
```

**Container won't start:**
```bash
# Check logs
docker-compose logs web

# Check if container exists
docker ps -a

# Remove and recreate
docker-compose down
docker-compose up --build
```

**Changes not reflecting:**
```bash
# Ensure volume is mounted
docker-compose config  # Verify configuration

# Restart container
docker-compose restart web
```

---

## 📖 API Documentation

### Interactive Documentation

FastAPI automatically generates interactive API documentation:

1. **Swagger UI:** http://localhost:8001/docs
   - Try out endpoints directly in browser
   - See request/response schemas
   - View available endpoints

2. **ReDoc:** http://localhost:8001/redoc
   - Alternative documentation format
   - Better for reading/printing

### Available Endpoints

#### `GET /`
Returns a simple hello world message.

**Response:**
```json
{
  "message": "Hello World"
}
```

**Example:**
```bash
curl http://localhost:8001/
```

#### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy"
}
```

**Example:**
```bash
curl http://localhost:8001/health
```

### Adding Documentation to Endpoints

```python
@app.get("/endpoint", 
         summary="Short description",
         description="Long description",
         response_description="What the response contains")
async def endpoint():
    """
    Additional documentation here.
    
    This appears in the interactive docs.
    """
    return {"data": "value"}
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Poetry not found
```bash
# Add Poetry to PATH
export PATH="$HOME/.local/bin:$PATH"

# Make permanent (macOS/Linux)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

#### Docker daemon not running
```bash
# macOS: Start Docker Desktop from Applications
open -a Docker

# Verify it's running
docker ps
```

#### Port conflicts
```bash
# Find what's using the port
lsof -ti:8001

# Kill the process
lsof -ti:8001 | xargs kill -9

# Or use a different port in docker-compose.yml
```

#### Module not found errors
```bash
# Reinstall dependencies
poetry install

# Or in Docker
docker-compose down
docker-compose up --build
```

#### Hot reload not working
```bash
# Ensure volume is mounted (check docker-compose.yml)
# Ensure --reload flag is in command
# Try restarting: docker-compose restart web
```

---

## 🎓 Learning Resources

### FastAPI
- Official Docs: https://fastapi.tiangolo.com/
- Tutorial: https://fastapi.tiangolo.com/tutorial/

### Docker
- Official Docs: https://docs.docker.com/
- Get Started: https://docs.docker.com/get-started/

### Poetry
- Official Docs: https://python-poetry.org/docs/
- Basic Usage: https://python-poetry.org/docs/basic-usage/

### pytest
- Official Docs: https://docs.pytest.org/
- Getting Started: https://docs.pytest.org/en/stable/getting-started.html

---

## 📝 Next Steps

### Enhance This Project

1. **Add Database:** Integrate PostgreSQL or SQLite
   ```bash
   poetry add sqlalchemy databases[postgresql]
   ```

2. **Add Authentication:** Implement JWT or OAuth2
   ```bash
   poetry add python-jose[cryptography] passlib[bcrypt]
   ```

3. **Add CORS:** Enable cross-origin requests
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   app.add_middleware(CORSMiddleware, ...)
   ```

4. **Add Logging:** Structured logging
   ```bash
   poetry add python-json-logger
   ```

5. **Add Environment Variables:** Configuration management
   ```bash
   poetry add python-dotenv pydantic-settings
   ```

6. **Add More Services:** Database, Redis, etc.
   ```yaml
   # docker-compose.yml
   services:
     web:
       # ... existing config
     
     db:
       image: postgres:15
       environment:
         POSTGRES_PASSWORD: password
   ```

---

## 📄 License

MIT License - Feel free to use this project as a template for your own applications.

---

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

**Happy Coding! 🚀**
