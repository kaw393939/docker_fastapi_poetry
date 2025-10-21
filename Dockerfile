# Dockerfile - Instructions to Build Docker Image
#
# A Dockerfile contains a series of instructions to create a Docker image.
# Each instruction creates a "layer" in the image. Layers are cached for efficiency.
#
# Key Concepts:
# - Image: A template for creating containers (like a class in OOP)
# - Container: A running instance of an image (like an object in OOP)
# - Layer: Each instruction (FROM, RUN, COPY, etc.) creates a layer
# - Layer Caching: Unchanged layers are reused, speeding up builds
#
# Build Process:
# 1. Docker reads Dockerfile top to bottom
# 2. Executes each instruction
# 3. Creates a new layer for each instruction
# 4. Final image is the combination of all layers
#
# Build Command: docker build -t myapp .
# Run Command: docker run -p 8000:8000 myapp

# FROM - Base Image
# Start from an official Python image
# python:3.11-slim is a minimal Debian-based image with Python 3.11
# "slim" variant is smaller (fewer system packages) than "full" variant
# Alternative options:
# - python:3.11        : Full version with more tools (larger)
# - python:3.11-alpine : Minimal Alpine Linux (smallest, but harder to use)
FROM python:3.11-slim

# WORKDIR - Set Working Directory
# All subsequent commands run from this directory
# Like running: mkdir /app && cd /app
# If the directory doesn't exist, Docker creates it
WORKDIR /app

# RUN - Execute Command During Build
# Install Poetry package manager
# This runs during image build (not container runtime)
# Each RUN command creates a new layer in the image
RUN pip install poetry

# Configure Poetry Settings
# virtualenvs.create false: Don't create virtual environment
# Inside containers, virtual environments are unnecessary because
# the entire container is already isolated
RUN poetry config virtualenvs.create false

# COPY - Copy Files from Host to Image
# Copy dependency files first (before application code)
# This is a Docker best practice for layer caching
# If only app code changes, this layer is reused from cache
# poetry.lock* : The * makes it optional (won't fail if missing)
COPY pyproject.toml poetry.lock* ./

# Install Dependencies
# --no-interaction: Don't ask for user input (required in automated builds)
# --no-ansi: Disable colored output (cleaner logs)
# --no-root: Don't install the project itself, just dependencies
# This layer is cached unless pyproject.toml or poetry.lock changes
# Meaning: If you only change app code, dependencies aren't reinstalled!
RUN poetry install --no-interaction --no-ansi --no-root

# Copy Application Code
# Copy everything from current directory (.) to /app in container
# This happens AFTER dependency installation for better caching
# .dockerignore file controls what's excluded (like .gitignore)
COPY . .

# EXPOSE - Document Port Usage
# Declares that the container listens on port 8000
# This is documentation only - doesn't actually publish the port
# Actual port publishing happens with: docker run -p 8000:8000
EXPOSE 8000

# CMD - Default Command
# Defines the command to run when container starts
# Can be overridden with: docker run myapp <different-command>
# Format: ["executable", "param1", "param2", ...]
#
# Command Breakdown:
# - uvicorn           : ASGI web server
# - app.main:app      : Import path (app/main.py, variable named 'app')
# - --host 0.0.0.0    : Listen on all network interfaces (required for Docker)
# - --port 8000       : Port to listen on inside container
# - --reload          : Auto-restart on code changes (DEVELOPMENT ONLY!)
#
# Production Note: Remove --reload in production for better performance
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Multi-Stage Build Example (Advanced)
# Use this pattern to keep images smaller by excluding build tools from final image
#
# FROM python:3.11-slim as builder
# WORKDIR /app
# RUN pip install poetry
# COPY pyproject.toml poetry.lock ./
# RUN poetry export -f requirements.txt > requirements.txt
#
# FROM python:3.11-slim
# WORKDIR /app
# COPY --from=builder /app/requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

