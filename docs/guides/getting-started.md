# Getting Started Guide

## Prerequisites

Before you begin, make sure you have these installed:

### Required
- **Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop)
- **Git** - [Download here](https://git-scm.com/downloads)

### Optional (for local development)
- **Poetry** - Python dependency manager
- **Python 3.11+** - If running without Docker

---

## Installation

### Install Docker Desktop

1. Download Docker Desktop for your operating system
2. Run the installer
3. Start Docker Desktop
4. Verify installation:
```bash
docker --version
# Should show: Docker version 20.x.x or higher
```

### Install Poetry (Optional)

Poetry is needed only if you want to run the app locally without Docker.

**macOS/Linux:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Windows (PowerShell):**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

**Add to PATH:**
```bash
# macOS/Linux (zsh)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# macOS/Linux (bash)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Verify installation:**
```bash
poetry --version
# Should show: Poetry (version 1.7.0)
```

---

## Quick Start

### Option 1: Using Docker (Recommended)

This is the easiest way to get started. No Python installation needed!

```bash
# 1. Clone the repository
git clone git@github.com:kaw393939/docker_fastapi_poetry.git
cd docker_fastapi_poetry

# 2. Start the application
docker-compose up

# You should see:
# web_1  | INFO:     Uvicorn running on http://0.0.0.0:8000
# web_1  | INFO:     Application startup complete.

# 3. Test it's working (in a new terminal)
curl http://localhost:8001/
# Response: {"message":"Hello World"}
```

**Access the API:**
- API endpoint: http://localhost:8001/
- Interactive docs: http://localhost:8001/docs
- Alternative docs: http://localhost:8001/redoc

**Stop the application:**
```bash
# Press Ctrl+C in the terminal where docker-compose is running
# Or run:
docker-compose down
```

### Option 2: Using Poetry (Local Development)

Run directly on your machine for faster development cycles.

```bash
# 1. Clone the repository
git clone git@github.com:kaw393939/docker_fastapi_poetry.git
cd docker_fastapi_poetry

# 2. Install dependencies
poetry install --no-root

# 3. Run the application
poetry run uvicorn app.main:app --reload --port 8000

# You should see:
# INFO:     Uvicorn running on http://127.0.0.1:8000
# INFO:     Application startup complete.

# 4. Test it's working (in a new terminal)
curl http://localhost:8000/
# Response: {"message":"Hello World"}
```

---

## Verifying Your Setup

### Test the Health Endpoint

```bash
curl http://localhost:8001/
```

**Expected response:**
```json
{"message":"Hello World"}
```

### Access Interactive Documentation

Open your browser and go to:
- http://localhost:8001/docs

You should see the **Swagger UI** with:
- List of available endpoints
- Try it out functionality
- Request/response examples

### Run the Tests

```bash
# Using Docker
docker-compose exec web pytest -v

# Using Poetry
poetry run pytest -v
```

**Expected output:**
```
tests/test_main.py::test_read_root PASSED
tests/test_main.py::test_health_check PASSED

========== 2 passed in 0.05s ==========
```

---

## Common Setup Issues

### "Port already in use"

**Error:**
```
Error starting userland proxy: listen tcp4 0.0.0.0:8001: bind: address already in use
```

**Solution:**
```bash
# Find what's using the port
lsof -ti:8001

# Kill the process
lsof -ti:8001 | xargs kill -9

# Or change the port in docker-compose.yml
ports:
  - "8002:8000"  # Use 8002 instead
```

### "Docker daemon not running"

**Error:**
```
Cannot connect to the Docker daemon. Is the docker daemon running?
```

**Solution:**
1. Start Docker Desktop application
2. Wait for it to fully start (whale icon in system tray)
3. Try your command again

### "Poetry not found"

**Error:**
```
zsh: command not found: poetry
```

**Solution:**
```bash
# Add Poetry to PATH
export PATH="$HOME/.local/bin:$PATH"

# Make it permanent
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### "Permission denied" (Linux/macOS)

**Error:**
```
Permission denied while trying to connect to Docker daemon
```

**Solution:**
```bash
# Add your user to docker group
sudo usermod -aG docker $USER

# Log out and log back in for changes to take effect
```

---

## Project Structure Overview

```
docker_fastapi_poetry/
├── app/                      # Your application code
│   ├── __init__.py
│   └── main.py              # FastAPI app and endpoints
├── tests/                    # Test files
│   ├── __init__.py
│   └── test_main.py
├── docs/                     # Documentation
├── Dockerfile               # How to build the Docker image
├── docker-compose.yml       # How to run the containers
├── pyproject.toml          # Python dependencies
└── poetry.lock             # Locked dependency versions
```

---

## Next Steps

Now that you're set up, where to go next?

### For Complete Beginners

1. **Understand the basics:**
   - [What is a REST API?](../concepts/rest-apis.md)
   - [Understanding Ports](../concepts/ports-networking.md)
   - [Docker Basics](../concepts/docker-basics.md)

2. **Follow the tutorial:**
   - [Your First API](../tutorials/first-api.md) (15 minutes)
   - [Testing with curl](../concepts/curl-basics.md)

### For Intermediate Developers

1. **Learn FastAPI patterns:**
   - [HTTP Methods](../concepts/http-methods.md)
   - [Creating Endpoints](../tutorials/first-endpoint.md)
   - [Writing Tests](../tutorials/first-test.md)

2. **Build something:**
   - Try adding a new endpoint
   - Implement POST requests
   - Add request validation

### For Advanced Developers

1. **Production setup:**
   - [Docker Hub Publishing](docker-hub.md)
   - [GitHub Actions CI/CD](github-actions.md)
   - [Deployment Guide](deployment.md)

2. **Optimize:**
   - [Multi-stage Docker builds](docker-multi-stage.md)
   - [Environment Configuration](environment-config.md)
   - [Performance](performance.md)

---

## Development Workflow

### Making Changes

```bash
# 1. Edit your code in app/main.py

# 2. If using Docker with hot-reload:
#    Changes are automatically detected!
#    Just refresh your browser

# 3. If using Poetry:
#    The --reload flag auto-reloads on changes

# 4. Test your changes
docker-compose exec web pytest
# or
poetry run pytest
```

### Adding Dependencies

```bash
# 1. Add the package
poetry add package-name

# 2. Rebuild Docker image
docker-compose up --build
```

### Debugging

```bash
# View logs
docker-compose logs -f web

# Access container shell
docker-compose exec web bash

# Run Python interpreter
docker-compose exec web python
```

---

## Getting Help

- **Issues?** Check [Troubleshooting Guide](../references/troubleshooting.md)
- **Questions?** Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
- **Want to learn more?** See [Learning Paths](../../README.md#learning-paths)

---

## Quick Command Reference

### Docker Commands

| Command | Description |
|---------|-------------|
| `docker-compose up` | Start the application |
| `docker-compose up -d` | Start in background |
| `docker-compose down` | Stop and remove containers |
| `docker-compose logs -f` | View logs |
| `docker-compose exec web bash` | Access container shell |
| `docker-compose exec web pytest` | Run tests |

### Poetry Commands

| Command | Description |
|---------|-------------|
| `poetry install` | Install dependencies |
| `poetry add package` | Add a new package |
| `poetry run uvicorn app.main:app --reload` | Run app with hot-reload |
| `poetry run pytest` | Run tests |
| `poetry shell` | Activate virtual environment |

**📋 Full Reference:** [Docker Commands](../references/docker-commands.md) | [Poetry Commands](../references/poetry-commands.md)
