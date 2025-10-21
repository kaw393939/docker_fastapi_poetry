# FastAPI + Docker + Poetry: Complete Learning Platform

> **A comprehensive, production-ready FastAPI application designed for learning modern Python development, Docker containerization, and REST API best practices.**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-latest-blue.svg?logo=docker)](https://www.docker.com/)
[![Poetry](https://img.shields.io/badge/poetry-1.7+-blue.svg?logo=poetry)](https://python-poetry.org/)
[![pytest](https://img.shields.io/badge/pytest-passing-green.svg)](https://docs.pytest.org/)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone git@github.com:kaw393939/docker_fastapi_poetry.git
cd docker_fastapi_poetry

# Start the application
docker-compose up

# Test it's working
curl http://localhost:8001/
# Response: {"message":"Hello World"}
```

**🎓 New to this?** Start with our [First API Tutorial](docs/tutorials/first-api.md)

---

## 📖 Learning Paths

Choose your learning journey based on your experience level:

### 🌱 Complete Beginner

**Goal:** Understand web APIs and get your first application running

1. **Concepts** (Start here!)
   - [What is a REST API?](docs/concepts/rest-apis.md) - Understand client-server communication
   - [Understanding Ports](docs/concepts/ports-networking.md) - How applications talk to each other
   - [Docker Basics](docs/concepts/docker-basics.md) - Containerization explained simply

2. **Hands-On Tutorials**
   - [Your First API](docs/tutorials/first-api.md) - Get the app running (15 min)
   - [Testing with curl](docs/concepts/curl-basics.md) - Make your first API requests

3. **Practice**
   - Complete the challenge exercises in each tutorial
   - Experiment with the interactive docs at http://localhost:8001/docs

### 🌿 Intermediate Developer

**Goal:** Build real endpoints and understand FastAPI patterns

1. **Core Concepts**
   - [HTTP Methods](docs/concepts/http-methods.md) - GET, POST, PUT, DELETE
   - [HTTP Status Codes](docs/concepts/http-status-codes.md) - 200, 404, 500 explained

2. **Build Features**
   - [Creating Endpoints](docs/tutorials/first-endpoint.md) - Build your own API routes
   - [Request Validation](docs/guides/validation.md) - Handle user input safely
   - [Error Handling](docs/guides/error-handling.md) - Manage failures gracefully

3. **Testing**
   - [Writing Tests](docs/tutorials/first-test.md) - Automated testing with pytest
   - [Test-Driven Development](docs/guides/tdd.md) - Write tests first

### 🌳 Advanced Developer

**Goal:** Production-ready applications and deployment

1. **Architecture**
   - [Project Structure](docs/guides/project-structure.md) - Organize large codebases
   - [Dependency Injection](docs/guides/dependency-injection.md) - FastAPI's DI system
   - [Async Patterns](docs/guides/async-patterns.md) - Asynchronous programming

2. **Production**
   - [Docker Multi-stage Builds](docs/guides/docker-multi-stage.md) - Optimize images
   - [Environment Configuration](docs/guides/environment-config.md) - Manage settings
   - [Deployment Guide](docs/guides/deployment.md) - Deploy to production

3. **Best Practices**
   - [Security](docs/guides/security.md) - HTTPS, CORS, authentication
   - [Performance](docs/guides/performance.md) - Caching, database optimization
   - [Monitoring](docs/guides/monitoring.md) - Logging and health checks

---

## 📚 Documentation Structure

Our documentation follows the **Diátaxis framework** for technical documentation:

```
docs/
├── concepts/          # 💡 Theoretical knowledge (WHY things work)
│   ├── rest-apis.md          - What are REST APIs?
│   ├── http-methods.md       - GET, POST, PUT, DELETE explained
│   ├── http-status-codes.md  - Understanding 200, 404, 500
│   ├── ports-networking.md   - How ports and networking work
│   ├── docker-basics.md      - Containers vs VMs
│   └── curl-basics.md        - Testing with curl
│
├── tutorials/         # 📝 Step-by-step learning (LEARNING by doing)
│   ├── first-api.md          - Your first API in 15 minutes
│   ├── first-endpoint.md     - Create custom endpoints
│   └── first-test.md         - Write automated tests
│
├── guides/            # 🛠️ How-to guides (HOW to solve specific problems)
│   ├── docker-compose.md     - Using Docker Compose
│   ├── validation.md         - Validate user input
│   ├── error-handling.md     - Handle errors properly
│   ├── testing-guide.md      - Comprehensive testing
│   └── deployment.md         - Deploy to production
│
└── references/        # 📋 Quick lookups (REFERENCE material)
    ├── api-endpoints.md      - All available endpoints
    ├── docker-commands.md    - Docker command cheat sheet
    ├── poetry-commands.md    - Poetry command reference
    └── troubleshooting.md    - Common issues & solutions
```

### How to Use This Documentation

**If you want to...**

- **Understand a concept** → Read `docs/concepts/`
- **Learn by doing** → Follow `docs/tutorials/`
- **Solve a specific problem** → Check `docs/guides/`
- **Look up syntax/commands** → Use `docs/references/`

---

## 🎯 What You'll Learn

### Core Technologies

| Technology | What You'll Master | Documentation |
|------------|-------------------|---------------|
| **FastAPI** | Build modern REST APIs with automatic docs | [Official Docs](https://fastapi.tiangolo.com) |
| **Docker** | Package apps with all dependencies | [Docker Basics](docs/concepts/docker-basics.md) |
| **Poetry** | Manage Python dependencies professionally | [Poetry Guide](docs/guides/poetry.md) |
| **pytest** | Write automated tests for reliability | [Testing Guide](docs/guides/testing-guide.md) |
| **Uvicorn** | Run async Python web servers | [FastAPI Docs](https://www.uvicorn.org/) |

### Skills You'll Develop

✅ **API Design** - Create RESTful endpoints following best practices  
✅ **Docker Proficiency** - Containerize applications for consistency  
✅ **Testing** - Write comprehensive automated tests  
✅ **HTTP Protocol** - Understand requests, responses, status codes  
✅ **Development Workflow** - Hot-reload, debugging, deployment  
✅ **Python Best Practices** - Type hints, async/await, project structure  

---

## 🏗️ Project Structure

```
.
├── app/                      # Application source code
│   ├── __init__.py          # Makes app a Python package
│   └── main.py              # FastAPI application & endpoints
├── tests/                    # Automated tests
│   ├── __init__.py
│   └── test_main.py         # Test cases for endpoints
├── docs/                     # 📚 Comprehensive documentation
│   ├── concepts/            # Theoretical knowledge
│   ├── tutorials/           # Step-by-step learning
│   ├── guides/              # How-to guides
│   └── references/          # Quick references
├── Dockerfile                # Docker image build instructions
├── docker-compose.yml        # Docker orchestration
├── pyproject.toml           # Poetry dependencies
├── poetry.lock              # Locked dependency versions
├── .dockerignore            # Files to exclude from Docker
└── .gitignore               # Files to exclude from Git
```

**🔍 Explore:** [Detailed Project Structure](docs/references/project-structure.md)

---

## Prerequisites & Installation

### Install Docker

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Install Poetry (for local development)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to your PATH:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**📖 Detailed Setup:** See [Installation Guide](docs/guides/installation.md)

---

## Common Commands Reference

### Docker
```bash
# Start services
docker-compose up          # Start with logs
docker-compose up -d       # Start in background
docker-compose up --build  # Rebuild and start

# Stop services
docker-compose down        # Stop and remove
docker-compose stop        # Just stop

# View logs
docker-compose logs -f     # Follow logs

# Run commands in container
docker-compose exec web pytest
docker-compose exec web bash
```

### Poetry (Local Development)
```bash
# Install dependencies
poetry install

# Add new package
poetry add package-name

# Run application
poetry run uvicorn app.main:app --reload

# Run tests
poetry run pytest -v
```

**📋 Full Reference:** [Docker Commands](docs/references/docker-commands.md) | [Poetry Commands](docs/references/poetry-commands.md)

---

## Interactive API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc

---

## Common Issues & Solutions

### Port Already in Use
```bash
# macOS/Linux: Find and kill process
lsof -ti:8001 | xargs kill -9

# Or change port in docker-compose.yml
ports:
  - "8002:8000"
```

### Poetry Not in PATH
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**🔧 More Solutions:** [Troubleshooting Guide](docs/references/troubleshooting.md)

---

## 📖 External Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)

---

## Contributing

Contributions are welcome! This project is designed for education, so improvements that make concepts clearer are especially valuable.

---

## License

MIT License - See LICENSE file for details

---

**Made with ❤️ for teaching modern Python development**

**Questions?** Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
