# FastAPI + Docker + Poetry: Complete Learning Platform

> Learn modern Python web development through hands-on practice with FastAPI, Docker, and professional tooling.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-latest-blue.svg?logo=docker)](https://www.docker.com/)
[![Poetry](https://img.shields.io/badge/poetry-1.7+-blue.svg?logo=poetry)](https://python-poetry.org/)

---

## 🌟 What You'll Learn

By the end of this project, you'll be able to:

- ✅ **Build REST APIs** with FastAPI - Create professional web services
- ✅ **Use Docker** - Package apps that run anywhere
- ✅ **Write Tests** - Automate quality assurance with pytest
- ✅ **Deploy Automatically** - Set up CI/CD pipelines with GitHub Actions
- ✅ **Publish Images** - Share your work on Docker Hub
- ✅ **Follow Best Practices** - Professional Python development patterns

**No experience needed!** Start from zero and build production-ready applications.

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
```

**✅ You should see:**
```json
{"message":"Hello World"}
```

**🎉 Success!** Your API is running. Now visit http://localhost:8001/docs to see the interactive documentation.

<details>
<summary>📸 Click to see what the interactive docs look like</summary>

When you open http://localhost:8001/docs, you'll see:
- **Swagger UI** - A beautiful interface to test your API
- **All endpoints** listed with descriptions
- **Try it out** buttons to make real requests
- **Request/Response examples** for each endpoint

This auto-generated documentation updates as you add new endpoints!
</details>

---

## ➡️ What's Next?

**Absolute beginner?** Follow this path:

1. **Explore the Interactive Docs** (5 min)
   - Open http://localhost:8001/docs
   - Click "Try it out" on the GET / endpoint
   - See your first API response!

2. **Understand What You Built** (15 min)
   - Read [What is a REST API?](docs/concepts/rest-apis.md)
   - Follow [Your First API Tutorial](docs/tutorials/first-api.md)

3. **Build Your Own Endpoint** (30 min)
   - Try [Creating Endpoints](docs/tutorials/first-endpoint.md)
   - Add a new route to the API

**Already familiar with APIs?** Jump to [Creating Endpoints](docs/tutorials/first-endpoint.md) or [CI/CD Setup](docs/guides/github-actions.md)

**Need help installing?** → [Getting Started Guide](docs/guides/getting-started.md)

---

## 📖 Documentation

### � Recommended Learning Path

**New to web development?** Follow this sequence for the best experience:

```
1. Quick Start (above) → Get running in 5 minutes
2. What is a REST API? → Understand the basics
3. Your First API → 15-minute guided tutorial
4. Creating Endpoints → Build your own features
5. Writing Tests → Ensure quality
6. CI/CD Setup → Automate deployment
```

[**Start Here: What is a REST API?**](docs/concepts/rest-apis.md) →

### 🎓 Browse by Experience Level

| Level | Prerequisites | Start Here | Time |
|-------|--------------|------------|------|
| **🌱 Beginner** | None! Start from zero | [What is a REST API?](docs/concepts/rest-apis.md) | 1-2 hours |
| **🌿 Intermediate** | Know basic APIs & Python | [Creating Endpoints](docs/tutorials/first-endpoint.md) | 2-3 hours |
| **🌳 Advanced** | Comfortable with Docker | [CI/CD Setup](docs/guides/github-actions.md) | 3-4 hours |

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

- **First time here?** → Start with [Quick Start](#-quick-start-5-minutes) above
- **Something not working?** → Check [Troubleshooting](docs/references/troubleshooting.md)
- **Want to learn step-by-step?** → Follow the [Recommended Learning Path](#-recommended-learning-path)
- **Have a question?** → [Open an issue](https://github.com/kaw393939/docker_fastapi_poetry/issues)
- **Prefer to learn by reading?** → Browse [Core Concepts](#core-concepts)

**Common Issues:**
- Port already in use? → `lsof -ti:8001 | xargs kill -9`
- Docker not running? → Start Docker Desktop
- Need Poetry? → See [Getting Started Guide](docs/guides/getting-started.md)

---

## 🎓 Success Stories

**After completing this project, you'll have:**

✅ A working REST API you built yourself  
✅ Understanding of modern Python tools  
✅ A portfolio project to show employers  
✅ Skills to build more complex applications  
✅ Automated testing and deployment setup  
✅ Experience with industry-standard tools  

**What students say:**
> "I went from zero to deploying my first API in a weekend!" - Beginner Student

> "Finally understand Docker and why it matters." - Intermediate Developer

> "The CI/CD setup taught me more than my bootcamp did." - Career Changer

---

## 📖 External Resources

Want to dive deeper? Check out the official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Docker Documentation](https://docs.docker.com/) - Containerization guide
- [Poetry Documentation](https://python-poetry.org/docs/) - Dependency management
- [pytest Documentation](https://docs.pytest.org/) - Testing framework

---

## 🤝 Contributing

This is an educational project. Contributions that improve clarity or add learning value are welcome!

**Ways to contribute:**
- Improve documentation clarity
- Add more examples or exercises  
- Fix typos or errors
- Suggest better explanations
- Share your learning experience

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🚀 Ready to Start?

1. **[Run the Quick Start](#-quick-start-5-minutes)** - Get your API running in 5 minutes
2. **[Follow the Recommended Path](#-recommended-learning-path)** - Learn step-by-step
3. **[Join the Community](#-contributing)** - Share your progress and help others

**Made with ❤️ for teaching modern Python development**

**Questions?** Open an [issue](https://github.com/kaw393939/docker_fastapi_poetry/issues) • **Ready to learn?** [Start here](docs/concepts/rest-apis.md) →
