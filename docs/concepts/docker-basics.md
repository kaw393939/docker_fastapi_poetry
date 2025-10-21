# Understanding Docker

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what Docker is and why it's useful
- Understand containers vs virtual machines
- Identify Docker's key components
- Describe how Docker solves the "works on my machine" problem

---

## What is Docker?

**Docker** is a platform for developing, shipping, and running applications in **containers**. Think of it as a way to package your application with everything it needs to run, anywhere.

---

## The "Works on My Machine" Problem

### Without Docker

```
Developer's Machine:
✅ Python 3.11
✅ All dependencies installed
✅ App works perfectly

Production Server:
❌ Python 3.9
❌ Missing dependencies
❌ Different OS
❌ App crashes!
```

**Classic developer excuse:**
> "But it works on my machine! 🤷"

### With Docker

```
Developer's Machine:
✅ Docker container with Python 3.11
✅ All dependencies bundled
✅ App works

Production Server:
✅ Same Docker container
✅ Same Python 3.11
✅ Same dependencies
✅ App works!  🎉
```

**Docker promise:**
> "If it works in the container, it works everywhere!"

---

## Containers vs Virtual Machines

### Virtual Machines (The Old Way)

```
┌─────────────────────────────────────┐
│         Your Computer (Host)        │
├─────────────────────────────────────┤
│                                     │
│  ┌──────────────┐  ┌──────────────┐│
│  │  VM #1       │  │  VM #2       ││
│  ├──────────────┤  ├──────────────┤│
│  │ Guest OS     │  │ Guest OS     ││ ← Each has FULL OS
│  │ (Ubuntu)     │  │ (Windows)    ││   (GBs of space!)
│  ├──────────────┤  ├──────────────┤│
│  │ App + Deps   │  │ App + Deps   ││
│  └──────────────┘  └──────────────┘│
│                                     │
│  Hypervisor (VirtualBox, VMware)   │
├─────────────────────────────────────┤
│           Host Operating System      │
└─────────────────────────────────────┘
```

**Problems:**
- ❌ Heavy (GBs per VM)
- ❌ Slow to start (minutes)
- ❌ Resource intensive

### Docker Containers (The Modern Way)

```
┌─────────────────────────────────────┐
│         Your Computer (Host)        │
├─────────────────────────────────────┤
│                                     │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐│
│  │Container│ │Container│ │Container││
│  │  #1     │ │  #2     │ │  #3     ││
│  ├─────────┤ ├─────────┤ ├─────────┤│
│  │App+Deps │ │App+Deps │ │App+Deps ││ ← Share OS kernel
│  └─────────┘ └─────────┘ └─────────┘│   (MBs of space!)
│                                     │
│         Docker Engine               │
├─────────────────────────────────────┤
│      Host Operating System          │
└─────────────────────────────────────┘
```

**Advantages:**
- ✅ Lightweight (MBs per container)
- ✅ Fast to start (seconds)
- ✅ Efficient resource usage

---

## Key Docker Concepts

### 1. Docker Image

**What:** A blueprint/template for creating containers

**Analogy:** Like a class in programming or a recipe for a cake

```
Dockerfile → Build → Docker Image
    │                      │
    │                      │
Recipe for              Cake Mix
the app                 (ready to use)
```

**Example:**
```dockerfile
FROM python:3.11-slim    # Base: Start with Python
COPY . /app              # Add: Copy your code
RUN pip install poetry   # Setup: Install dependencies
CMD ["python", "app.py"] # Run: Start the app
```

### 2. Docker Container

**What:** A running instance of an image

**Analogy:** Like an object created from a class, or a baked cake from the mix

```
Docker Image → Run → Container
     │                    │
     │                    │
  Cake Mix           Actual Cake
 (template)          (running)
```

**One image, many containers:**
```
Python Image
    ├── Container 1 (Running app on port 8001)
    ├── Container 2 (Running app on port 8002)
    └── Container 3 (Running app on port 8003)
```

### 3. Dockerfile

**What:** Instructions to build an image

**Example:**
```dockerfile
# Start with base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN pip install poetry && \
    poetry install --no-root

# Copy application code
COPY app/ ./app/

# Expose port
EXPOSE 8000

# Command to run
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0"]
```

### 4. Docker Compose

**What:** Tool to define and run multi-container applications

**Example:**
```yaml
services:
  web:               # Your app
    build: .
    ports:
      - "8001:8000"
  
  db:                # Database
    image: postgres
    ports:
      - "5432:5432"
  
  redis:             # Cache
    image: redis
```

---

## How Docker Works

### The Build Process

```
Step 1: Write Dockerfile
FROM python:3.11-slim
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

↓

Step 2: Build Image
$ docker build -t my-app .

Processing Dockerfile...
├── Layer 1: Python base image
├── Layer 2: Copy files
├── Layer 3: Install dependencies
└── Layer 4: Set command

↓

Step 3: Image Created
my-app:latest (342 MB)

↓

Step 4: Run Container
$ docker run -p 8000:8000 my-app

↓

Step 5: Container Running
my-app-container (ID: abc123)
Listening on port 8000
```

### Image Layers (Caching Magic)

Docker builds images in layers. Each instruction = one layer.

```dockerfile
FROM python:3.11-slim     # Layer 1: 150 MB (cached)
COPY requirements.txt .   # Layer 2: 1 KB (cached)
RUN pip install -r reqs   # Layer 3: 50 MB (cached)
COPY . /app              # Layer 4: 10 KB (CHANGED!)
```

**First build:** All layers built (slow)  
**Second build:** Only changed layers rebuilt (fast!)

---

## Docker Commands Cheat Sheet

### Images

```bash
# Build image from Dockerfile
docker build -t my-app .

# List images
docker images

# Remove image
docker rmi my-app

# Pull image from Docker Hub
docker pull python:3.11
```

### Containers

```bash
# Run container
docker run my-app

# Run with port mapping
docker run -p 8000:8000 my-app

# Run in background (detached)
docker run -d my-app

# Run with name
docker run --name my-container my-app

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop container
docker stop my-container

# Start stopped container
docker start my-container

# Remove container
docker rm my-container

# View logs
docker logs my-container

# Execute command in running container
docker exec -it my-container bash
```

### Docker Compose

```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs

# Rebuild and start
docker-compose up --build
```

---

## Docker in This Project

### Our Dockerfile

```dockerfile
# Multi-stage build for optimization
FROM python:3.11-slim as builder
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry install --no-root --only main

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY app/ ./app/
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0"]
```

**Why multi-stage?**
- Stage 1: Install dependencies (large)
- Stage 2: Copy only what's needed (small final image)
- Result: Smaller, faster image

### Our docker-compose.yml

```yaml
services:
  web:
    build: .
    ports:
      - "8001:8000"  # Host:Container
    volumes:
      - .:/app       # Live code updates
    command: >
      sh -c "poetry install && 
             poetry run uvicorn app.main:app 
             --host 0.0.0.0 --reload"
```

**Features:**
- **Port mapping:** 8001 → 8000
- **Volume mount:** Changes reflect immediately
- **Hot reload:** App restarts on code changes

---

## Common Docker Workflows

### Development Workflow

```bash
# 1. Make code changes
vim app/main.py

# 2. Changes automatically reload (volume mounting)
# No need to rebuild!

# 3. View logs
docker-compose logs -f

# 4. Run tests
docker-compose exec web pytest
```

### Production Workflow

```bash
# 1. Build optimized image
docker build -t my-app:v1.0 .

# 2. Test image
docker run -p 8000:8000 my-app:v1.0

# 3. Push to registry
docker tag my-app:v1.0 myregistry/my-app:v1.0
docker push myregistry/my-app:v1.0

# 4. Deploy
docker pull myregistry/my-app:v1.0
docker run -d -p 8000:8000 myregistry/my-app:v1.0
```

---

## Benefits of Docker

### 1. Consistency
```
Same environment everywhere:
├── Developer laptop
├── Testing server
├── Production server
└── Teammate's computer
```

### 2. Isolation
```
Each app in its own container:
├── App A: Python 3.11
├── App B: Python 2.7
├── App C: Node.js
└── No conflicts!
```

### 3. Portability
```
Run anywhere Docker runs:
├── Linux
├── macOS
├── Windows
├── Cloud (AWS, Azure, GCP)
└── Your laptop
```

### 4. Efficiency
```
Traditional:
├── VM 1: 4 GB
├── VM 2: 4 GB
└── VM 3: 4 GB
Total: 12 GB

Docker:
├── Container 1: 100 MB
├── Container 2: 100 MB
└── Container 3: 100 MB
Total: 300 MB (40x smaller!)
```

---

## Common Pitfalls

### ❌ Mistake 1: Not Using .dockerignore
```
# .dockerignore
__pycache__/
*.pyc
.git/
.pytest_cache/
node_modules/
```

**Why:** Copying unnecessary files makes images huge and slow

### ❌ Mistake 2: Running as Root
```dockerfile
# Bad
USER root

# Good
USER appuser
```

**Why:** Security risk

### ❌ Mistake 3: Not Using Layer Caching
```dockerfile
# Bad (slow rebuilds)
COPY . /app
RUN pip install -r requirements.txt

# Good (fast rebuilds)
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
```

**Why:** Copy dependencies first so they're cached

---

## Practice Exercise

### Challenge: Understand Our Setup

Look at the Dockerfile and docker-compose.yml in this project:

1. What base image are we using?
2. What port does the container use internally?
3. What port do we access on our machine?
4. What happens when you change code?

**Answers:**
```
1. python:3.11-slim
2. Port 8000
3. Port 8001
4. App automatically reloads (volume + --reload flag)
```

---

## Key Takeaways

✅ Docker packages apps with all dependencies  
✅ Containers are lightweight, fast, and portable  
✅ Images are templates, containers are running instances  
✅ Dockerfile defines how to build an image  
✅ Docker Compose manages multi-container apps  
✅ Solves "works on my machine" problem  
✅ Uses layer caching for efficiency  

---

## Next Steps

- Learn about [Docker Compose](../guides/docker-compose.md)
- Practice [Docker Commands](../references/docker-commands.md)
- Understand [Multi-stage Builds](../guides/docker-multi-stage.md)
- Read [Docker Best Practices](../guides/docker-best-practices.md)

---

**Questions or Feedback?**  
Open an issue on [GitHub](https://github.com/kaw393939/docker_fastapi_poetry/issues)
