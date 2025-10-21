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

## � Docker Hub Setup & Publishing

### What is Docker Hub?

Docker Hub is a cloud-based registry where you can store and share Docker images. Think of it like GitHub, but for Docker images instead of code. When you push an image to Docker Hub, others can easily pull and run your application without building it themselves.

### Step 1: Create a Docker Hub Account

1. Go to [Docker Hub](https://hub.docker.com/)
2. Click "Sign Up" and create a free account
3. Verify your email address
4. Log in to your new account

### Step 2: Create a Repository on Docker Hub

1. Click **"Create Repository"** button (top right)
2. Fill in the details:
   - **Name**: `docker_fastapi_poetry` (or your preferred name)
   - **Description**: "FastAPI application with Docker and Poetry"
   - **Visibility**: Public (free) or Private (requires subscription)
3. Click **"Create"**

Your repository will be available at: `docker.io/YOUR_USERNAME/docker_fastapi_poetry`

### Step 3: Log in to Docker Hub Locally

```bash
# Log in via command line
docker login

# Enter your Docker Hub username
# Enter your Docker Hub password (or access token - recommended)
```

**💡 Pro Tip:** Use an access token instead of your password for better security.

**To create an access token:**
1. Go to [Docker Hub → Account Settings → Security](https://hub.docker.com/settings/security)
2. Click **"New Access Token"**
3. Name it (e.g., "local-development")
4. Copy the token (you won't see it again!)
5. Use this token instead of your password when running `docker login`

### Step 4: Build and Tag Your Image

```bash
# Build the image with your Docker Hub username
docker build -t YOUR_USERNAME/docker_fastapi_poetry:latest .

# Example:
# docker build -t kaw393939/docker_fastapi_poetry:latest .
```

**Understanding tags:**
- `:latest` - The most recent version (default if no tag specified)
- `:v1.0.0` - Specific version number
- `:main-abc123` - Branch name with git commit hash

### Step 5: Push to Docker Hub

```bash
# Push the image to Docker Hub
docker push YOUR_USERNAME/docker_fastapi_poetry:latest

# Example:
# docker push kaw393939/docker_fastapi_poetry:latest
```

You'll see output showing each layer being pushed:
```
The push refers to repository [docker.io/kaw393939/docker_fastapi_poetry]
abc123def456: Pushed
789ghi012jkl: Pushed
latest: digest: sha256:abc123... size: 1234
```

### Step 6: Verify the Upload

1. Go to `https://hub.docker.com/r/YOUR_USERNAME/docker_fastapi_poetry`
2. You should see your image with the `latest` tag
3. The **"Tags"** tab shows all available versions

### Pull and Run from Docker Hub

Now anyone (or any server) can run your application:

```bash
# Pull the image
docker pull YOUR_USERNAME/docker_fastapi_poetry:latest

# Run it
docker run -p 8001:8000 YOUR_USERNAME/docker_fastapi_poetry:latest
```

### Multi-Tag Strategy (Best Practice)

Push multiple tags for better version management:

```bash
# Build and tag with multiple tags
docker build -t YOUR_USERNAME/docker_fastapi_poetry:latest \
             -t YOUR_USERNAME/docker_fastapi_poetry:v1.0.0 \
             -t YOUR_USERNAME/docker_fastapi_poetry:stable .

# Push all tags
docker push YOUR_USERNAME/docker_fastapi_poetry:latest
docker push YOUR_USERNAME/docker_fastapi_poetry:v1.0.0
docker push YOUR_USERNAME/docker_fastapi_poetry:stable
```

**📖 Learn More:** [Docker Hub Publishing Guide](docs/guides/docker-hub.md)

---

## 🚀 CI/CD with GitHub Actions

### What is CI/CD?

**CI/CD** stands for **Continuous Integration / Continuous Deployment**:

- **Continuous Integration (CI)**: Automatically test your code every time you push changes
- **Continuous Deployment (CD)**: Automatically build and deploy your application when tests pass

**Why use CI/CD?**
- ✅ Catch bugs before they reach production
- ✅ Ensure all tests pass before deploying
- ✅ Automate repetitive tasks (testing, building, deploying)
- ✅ Maintain code quality with every change
- ✅ Fast feedback loop for developers

### Our CI/CD Pipeline

This project includes a **GitHub Actions workflow** that automatically:

1. **Runs Tests** - Executes pytest with code coverage on every push
2. **Builds Docker Image** - Creates a production-ready Docker container
3. **Pushes to Docker Hub** - Publishes the image for deployment (on main branch)

**Workflow triggers:**
- ✅ Every `git push` to any branch runs tests
- ✅ Pushes to `main` branch also build and push Docker images
- ✅ Pull requests run tests to ensure quality before merging

### Understanding the Workflow File

The workflow is defined in `.github/workflows/ci-cd.yml`:

```yaml
name: CI/CD Pipeline

# When to run this workflow
on:
  push:
    branches: [ main, develop ]  # Run on pushes to main or develop
  pull_request:
    branches: [ main ]           # Run on PRs to main

jobs:
  # Job 1: Run Tests
  test:
    runs-on: ubuntu-latest       # Use Ubuntu Linux runner
    steps:
      - uses: actions/checkout@v4 # Download repository code
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'  # Use Python 3.11
      
      - name: Install Poetry
        run: |
          curl -sSL https://install.python-poetry.org | python3 -
          export PATH="$HOME/.local/bin:$PATH"
      
      - name: Install Dependencies
        run: poetry install --no-root
      
      - name: Run Tests with Coverage
        run: |
          poetry run pytest -v --cov=app --cov-report=term-missing
          
  # Job 2: Build and Push Docker Image (only on main branch)
  build:
    needs: test                   # Only run if tests pass
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      
      - name: Build and Push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ secrets.DOCKERHUB_USERNAME }}/docker_fastapi_poetry:latest
            ${{ secrets.DOCKERHUB_USERNAME }}/docker_fastapi_poetry:${{ github.sha }}
```

**Key concepts:**
- **jobs**: Separate tasks that can run in parallel
- **needs**: Specifies job dependencies (build needs test to pass)
- **if**: Conditional execution (only push images from main branch)
- **secrets**: Secure storage of credentials (Docker Hub username/token)

### Setting Up GitHub Actions

#### Step 1: Create Docker Hub Access Token

1. Go to [Docker Hub → Account Settings → Security](https://hub.docker.com/settings/security)
2. Click **"New Access Token"**
3. Name it: `github-actions`
4. Permissions: **Read, Write, Delete**
5. Click **"Generate"**
6. **Copy the token** (you won't see it again!)

#### Step 2: Add Secrets to GitHub Repository

1. Go to your GitHub repository
2. Click **Settings** tab
3. Navigate to **Secrets and variables → Actions**
4. Click **"New repository secret"**

**Add these two secrets:**

**Secret 1: DOCKERHUB_USERNAME**
- Name: `DOCKERHUB_USERNAME`
- Value: Your Docker Hub username (e.g., `kaw393939`)
- Click **"Add secret"**

**Secret 2: DOCKERHUB_TOKEN**
- Name: `DOCKERHUB_TOKEN`
- Value: The access token you copied in Step 1
- Click **"Add secret"**

#### Step 3: Verify Workflow is Enabled

1. Go to the **Actions** tab in your repository
2. You should see the "CI/CD Pipeline" workflow
3. If prompted, click **"I understand my workflows, go ahead and enable them"**

#### Step 4: Trigger the Workflow

```bash
# Make any change to trigger the workflow
git add .
git commit -m "Test CI/CD pipeline"
git push origin main
```

#### Step 5: Monitor the Workflow

1. Go to the **Actions** tab on GitHub
2. Click on your latest workflow run
3. Watch the jobs execute in real-time:
   - **Test** job runs first
   - **Build and Push** job runs after tests pass (main branch only)

**Success indicators:**
- ✅ Green checkmarks = All steps passed
- ❌ Red X = Something failed (click to see error logs)

### Understanding Workflow Execution

**On feature branches (e.g., `feature/add-users`):**
```
Push → Tests Run → ✅ Pass or ❌ Fail
       (no Docker build)
```

**On main branch:**
```
Push → Tests Run → ✅ Pass → Build Docker Image → Push to Docker Hub
                 ↓
                 ❌ Fail → Stop (no build/push)
```

**On pull requests:**
```
Open PR → Tests Run → ✅ Show status on PR
                    ↓
                    ❌ Block merge until fixed
```

### Viewing Test Coverage

After the workflow runs, you can see test coverage in the logs:

```
---------- coverage: platform linux, python 3.11 ----------
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
app/__init__.py         0      0   100%
app/main.py             8      0   100%
-------------------------------------------------
TOTAL                   8      0   100%
```

### Accessing Your Docker Images

After a successful workflow run on `main`:

```bash
# Pull the latest image
docker pull YOUR_USERNAME/docker_fastapi_poetry:latest

# Or pull a specific commit
docker pull YOUR_USERNAME/docker_fastapi_poetry:abc123def
```

### Common CI/CD Issues

**❌ "Error: secrets.DOCKERHUB_USERNAME is not set"**
- **Solution**: Add the secret in GitHub Settings → Secrets and variables → Actions

**❌ "docker login failed: unauthorized"**
- **Solution**: Verify your Docker Hub token is correct and has write permissions

**❌ "Tests failed" but they pass locally**
- **Solution**: 
  - Check Python version matches (3.11)
  - Ensure all dependencies are in `pyproject.toml`
  - Run `poetry lock` and commit the updated `poetry.lock`

**❌ "Workflow doesn't trigger"**
- **Solution**:
  - Ensure workflow file is in `.github/workflows/` directory
  - Check file is named with `.yml` or `.yaml` extension
  - Verify Actions are enabled in repository settings

### Customizing the Workflow

**Run tests on every branch:**
```yaml
on:
  push:
    branches: [ '**' ]  # All branches
```

**Add more test environments:**
```yaml
strategy:
  matrix:
    python-version: ['3.10', '3.11', '3.12']
```

**Send notifications on failure:**
```yaml
- name: Notify on failure
  if: failure()
  uses: slack/action@v1
  with:
    webhook: ${{ secrets.SLACK_WEBHOOK }}
```

**📖 Complete Guide:** [GitHub Actions CI/CD Setup](docs/guides/github-actions.md)

---

## �📖 External Resources

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
