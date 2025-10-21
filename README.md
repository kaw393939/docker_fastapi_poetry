# FastAPI + Docker + Poetry: Complete Learning Platform

> Learn modern Python web development through hands-on practice with FastAPI, Docker, and professional tooling.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-latest-blue.svg?logo=docker)](https://www.docker.com/)
[![Poetry](https://img.shields.io/badge/poetry-1.7+-blue.svg?logo=poetry)](https://python-poetry.org/)

---

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Clone and enter directory
git clone git@github.com:kaw393939/docker_fastapi_poetry.git
cd docker_fastapi_poetry

# 2. Start the application
docker-compose up

# 3. Test it works
curl http://localhost:8001/
# {"message":"Hello World"}
```

**View your API:**
- 🌐 API: http://localhost:8001/
- 📚 Interactive Docs: http://localhost:8001/docs

**First time?** → [Getting Started Guide](docs/guides/getting-started.md)

---

## 📖 Documentation

### 🎓 Learning Paths

Choose your path based on experience:

| Level | Start Here | What You'll Learn |
|-------|-----------|-------------------|
| **🌱 Beginner** | [Your First API](docs/tutorials/first-api.md) | Get running in 15 minutes |
| **🌿 Intermediate** | [Creating Endpoints](docs/tutorials/first-endpoint.md) | Build real API features |
| **🌳 Advanced** | [CI/CD Setup](docs/guides/github-actions.md) | Production deployment |

**Not sure where to start?** Try this flow:
1. [What is a REST API?](docs/concepts/rest-apis.md) ← Understand the basics
2. [Your First API](docs/tutorials/first-api.md) ← Get hands-on
3. [Creating Endpoints](docs/tutorials/first-endpoint.md) ← Build features

### 📚 Browse by Type

Our docs follow the [Diátaxis framework](https://diataxis.fr/):

| Type | Purpose | Start With |
|------|---------|-----------|
| **💡 Concepts** | Understand how things work | [REST APIs](docs/concepts/rest-apis.md), [Docker Basics](docs/concepts/docker-basics.md) |
| **📝 Tutorials** | Learn by doing | [First API](docs/tutorials/first-api.md), [First Endpoint](docs/tutorials/first-endpoint.md) |
| **🛠️ Guides** | Solve specific problems | [Docker Hub](docs/guides/docker-hub.md), [CI/CD](docs/guides/github-actions.md) |
| **📋 Reference** | Quick lookups | [Commands](docs/references/docker-commands.md), [Troubleshooting](docs/references/troubleshooting.md) |

---

## 🎯 What's Inside

### Core Technologies

- **FastAPI** - Modern, fast Python web framework
- **Docker** - Consistent development and deployment
- **Poetry** - Professional dependency management
- **pytest** - Automated testing framework

### Key Features

✅ Complete development environment  
✅ Automated testing with coverage  
✅ CI/CD pipeline with GitHub Actions  
✅ Docker containerization  
✅ Interactive API documentation  
✅ Production-ready project structure  

---

## 🏗️ Project Structure

```
docker_fastapi_poetry/
├── app/                    # Application code
│   └── main.py            # FastAPI app
├── tests/                  # Test suite
├── docs/                   # Documentation
│   ├── concepts/          # Learn WHY
│   ├── tutorials/         # Learn HOW
│   ├── guides/            # Solve problems
│   └── references/        # Quick lookups
├── Dockerfile             # Container definition
├── docker-compose.yml     # Multi-container setup
└── pyproject.toml        # Dependencies
```

---

## 📚 Essential Documentation

### Getting Started
- [Installation & Setup](docs/guides/getting-started.md) - Get up and running
- [Your First API](docs/tutorials/first-api.md) - 15-minute tutorial
- [Project Structure](docs/references/project-structure.md) - Understand the layout

### Core Concepts
- [What is a REST API?](docs/concepts/rest-apis.md) - Client-server basics
- [HTTP Methods](docs/concepts/http-methods.md) - GET, POST, PUT, DELETE
- [HTTP Status Codes](docs/concepts/http-status-codes.md) - 200, 404, 500
- [Docker Basics](docs/concepts/docker-basics.md) - Containerization explained
- [Ports & Networking](docs/concepts/ports-networking.md) - How apps communicate

### Development
- [Creating Endpoints](docs/tutorials/first-endpoint.md) - Build API routes
- [Testing with curl](docs/concepts/curl-basics.md) - Make API requests
- [Writing Tests](docs/tutorials/first-test.md) - Automated testing
- [Docker Commands](docs/references/docker-commands.md) - Command reference
- [Poetry Commands](docs/references/poetry-commands.md) - Dependency management

### Deployment
- [Docker Hub Publishing](docs/guides/docker-hub.md) - Share your images
- [GitHub Actions CI/CD](docs/guides/github-actions.md) - Automated deployment
- [Production Deployment](docs/guides/deployment.md) - Deploy to servers

### Help
- [Troubleshooting](docs/references/troubleshooting.md) - Common issues
- [Command Reference](docs/references/docker-commands.md) - Quick lookups

---

## 🔧 Common Commands

### Docker (Recommended)

```bash
docker-compose up              # Start app
docker-compose up -d           # Start in background
docker-compose down            # Stop app
docker-compose logs -f         # View logs
docker-compose exec web pytest # Run tests
```

### Poetry (Local Development)

```bash
poetry install --no-root                     # Install dependencies
poetry run uvicorn app.main:app --reload    # Run app
poetry run pytest -v                         # Run tests
```

**Full reference:** [Docker Commands](docs/references/docker-commands.md) | [Poetry Commands](docs/references/poetry-commands.md)

---

## 💡 Learning Resources

### Tutorials (Step-by-step)
1. [Your First API](docs/tutorials/first-api.md) - Get started in 15 minutes
2. [First Endpoint](docs/tutorials/first-endpoint.md) - Build custom routes
3. [First Test](docs/tutorials/first-test.md) - Write automated tests

### Concepts (Theory)
- [REST APIs](docs/concepts/rest-apis.md) - What they are and why they matter
- [HTTP Methods](docs/concepts/http-methods.md) - How to use GET, POST, etc.
- [Docker](docs/concepts/docker-basics.md) - Containers vs virtual machines

### Guides (How-to)
- [Getting Started](docs/guides/getting-started.md) - Installation and setup
- [Docker Hub](docs/guides/docker-hub.md) - Publish your images
- [CI/CD](docs/guides/github-actions.md) - Automate everything

---

## 🆘 Need Help?

- **Getting started?** → [Getting Started Guide](docs/guides/getting-started.md)
- **Something not working?** → [Troubleshooting](docs/references/troubleshooting.md)
- **Want to learn more?** → [Learning Paths](#-learning-paths)
- **Still stuck?** → [Open an issue](https://github.com/kaw393939/docker_fastapi_poetry/issues)

---

## 🌟 What You'll Learn

By working through this project, you'll master:

- ✅ Building REST APIs with FastAPI
- ✅ Docker containerization
- ✅ Professional dependency management
- ✅ Automated testing with pytest
- ✅ CI/CD with GitHub Actions
- ✅ Publishing to Docker Hub
- ✅ Production deployment strategies

---

## 📖 External Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)

---

## 🤝 Contributing

This is an educational project. Contributions that improve clarity or add learning value are welcome!

---

## 📄 License

MIT License - See LICENSE file for details

---

**Made with ❤️ for teaching modern Python development**

**Questions?** Open an [issue](https://github.com/kaw393939/docker_fastapi_poetry/issues) • **Start learning:** [Getting Started](docs/guides/getting-started.md)
