# Publishing to Docker Hub

## What is Docker Hub?

Docker Hub is a cloud-based registry where you can store and share Docker images. Think of it like GitHub, but for Docker images instead of code. When you push an image to Docker Hub, others can easily pull and run your application without building it themselves.

**Benefits:**
- 🌍 Share images globally
- 📦 Version control for Docker images
- 🔄 Automated builds with CI/CD
- 👥 Public or private repositories
- 🆓 Free tier for public images

---

## Step 1: Create a Docker Hub Account

1. Go to [Docker Hub](https://hub.docker.com/)
2. Click **"Sign Up"** and create a free account
3. Verify your email address
4. Log in to your new account

---

## Step 2: Create a Repository on Docker Hub

1. Click **"Create Repository"** button (top right)
2. Fill in the details:
   - **Name**: `docker_fastapi_poetry` (or your preferred name)
   - **Description**: "FastAPI application with Docker and Poetry"
   - **Visibility**: 
     - **Public** - Anyone can pull (free)
     - **Private** - Only you can access (requires subscription)
3. Click **"Create"**

Your repository will be available at:
```
docker.io/YOUR_USERNAME/docker_fastapi_poetry
```

---

## Step 3: Create a Docker Hub Access Token

**Why use an access token?**
- ✅ More secure than using your password
- ✅ Can be revoked without changing your password
- ✅ Can have limited permissions
- ✅ Required for automated CI/CD pipelines

### Creating the Token

1. Go to [Docker Hub → Account Settings → Security](https://hub.docker.com/settings/security)
2. Click **"New Access Token"**
3. Configure the token:
   - **Description**: `local-development` (or descriptive name)
   - **Permissions**: **Read, Write, Delete**
4. Click **"Generate"**
5. **IMPORTANT**: Copy the token immediately (you won't see it again!)

### Storing the Token Securely

**For macOS/Linux:**
```bash
# Store in a secure file (recommended)
echo "YOUR_TOKEN_HERE" > ~/.docker-hub-token
chmod 600 ~/.docker-hub-token  # Make it readable only by you
```

**For Windows:**
- Save to a secure password manager
- Or use Windows Credential Manager

---

## Step 4: Log in to Docker Hub Locally

```bash
# Log in via command line
docker login

# You'll be prompted for:
Username: YOUR_USERNAME
Password: YOUR_ACCESS_TOKEN  # Use token, not password!

# Success message:
# Login Succeeded
```

**Alternative: Login with token from file:**
```bash
cat ~/.docker-hub-token | docker login --username YOUR_USERNAME --password-stdin
```

**Verify you're logged in:**
```bash
cat ~/.docker/config.json
# Should show: "auths": { "https://index.docker.io/v1/": {...} }
```

---

## Step 5: Build and Tag Your Image

### Basic Build

```bash
# Build with your Docker Hub username
docker build -t YOUR_USERNAME/docker_fastapi_poetry:latest .

# Example:
docker build -t kaw393939/docker_fastapi_poetry:latest .
```

### Understanding Tags

Tags are versions of your Docker image:

| Tag | Purpose | Example |
|-----|---------|---------|
| `latest` | Most recent version (default) | `myapp:latest` |
| `v1.0.0` | Semantic version | `myapp:v1.0.0` |
| `main-abc123` | Branch + git hash | `myapp:main-abc123` |
| `stable` | Production-ready version | `myapp:stable` |
| `dev` | Development version | `myapp:dev` |

### Multi-Tag Build (Best Practice)

Build with multiple tags at once:

```bash
docker build -t YOUR_USERNAME/docker_fastapi_poetry:latest \
             -t YOUR_USERNAME/docker_fastapi_poetry:v1.0.0 \
             -t YOUR_USERNAME/docker_fastapi_poetry:stable .
```

---

## Step 6: Push to Docker Hub

### Push Single Tag

```bash
# Push the latest tag
docker push YOUR_USERNAME/docker_fastapi_poetry:latest

# Example:
docker push kaw393939/docker_fastapi_poetry:latest
```

**Expected output:**
```
The push refers to repository [docker.io/kaw393939/docker_fastapi_poetry]
abc123def456: Pushed
789ghi012jkl: Pushed
mno345pqr678: Pushed
latest: digest: sha256:abc123... size: 1234
```

### Push Multiple Tags

```bash
# Push all tags
docker push YOUR_USERNAME/docker_fastapi_poetry:latest
docker push YOUR_USERNAME/docker_fastapi_poetry:v1.0.0
docker push YOUR_USERNAME/docker_fastapi_poetry:stable
```

**Or use a script:**
```bash
#!/bin/bash
REPO="YOUR_USERNAME/docker_fastapi_poetry"
TAGS=("latest" "v1.0.0" "stable")

for tag in "${TAGS[@]}"; do
    docker push "$REPO:$tag"
done
```

---

## Step 7: Verify the Upload

1. Go to `https://hub.docker.com/r/YOUR_USERNAME/docker_fastapi_poetry`
2. You should see your image with all pushed tags
3. Click the **"Tags"** tab to see all available versions
4. Check the **"Last Pushed"** timestamp

**What you'll see:**
- Image name and description
- Pull count (how many times it's been downloaded)
- Last updated timestamp
- Available tags with their sizes
- Image layers and digest

---

## Pulling and Running from Docker Hub

### Pull the Image

```bash
# Pull latest version
docker pull YOUR_USERNAME/docker_fastapi_poetry:latest

# Pull specific version
docker pull YOUR_USERNAME/docker_fastapi_poetry:v1.0.0
```

### Run the Image

```bash
# Run the application
docker run -p 8001:8000 YOUR_USERNAME/docker_fastapi_poetry:latest

# Run in detached mode (background)
docker run -d -p 8001:8000 YOUR_USERNAME/docker_fastapi_poetry:latest

# Run with custom name
docker run -d -p 8001:8000 --name my-fastapi-app \
    YOUR_USERNAME/docker_fastapi_poetry:latest
```

### Share with Others

Anyone can now run your application with one command:

```bash
docker run -p 8001:8000 YOUR_USERNAME/docker_fastapi_poetry:latest
```

No need to:
- ❌ Clone the repository
- ❌ Install dependencies
- ❌ Build the image
- ❌ Configure the environment

Just pull and run! 🚀

---

## Advanced Tagging Strategies

### Semantic Versioning

```bash
# Major.Minor.Patch
docker tag myapp:latest myapp:1.0.0    # Initial release
docker tag myapp:latest myapp:1.0.1    # Bug fix
docker tag myapp:latest myapp:1.1.0    # New feature
docker tag myapp:latest myapp:2.0.0    # Breaking changes
```

### Environment-Based Tags

```bash
# Different environments
docker tag myapp:latest myapp:dev
docker tag myapp:latest myapp:staging
docker tag myapp:latest myapp:production
```

### Git-Based Tags

```bash
# Use git commit hash
GIT_HASH=$(git rev-parse --short HEAD)
docker tag myapp:latest myapp:main-$GIT_HASH

# Use git branch
GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
docker tag myapp:latest myapp:$GIT_BRANCH
```

### Date-Based Tags

```bash
# Include build date
DATE=$(date +%Y%m%d)
docker tag myapp:latest myapp:$DATE

# Example: myapp:20241021
```

---

## Managing Docker Hub Images

### View Local Images

```bash
# List all local images
docker images

# Filter by repository
docker images YOUR_USERNAME/docker_fastapi_poetry
```

### Remove Local Images

```bash
# Remove specific tag
docker rmi YOUR_USERNAME/docker_fastapi_poetry:v1.0.0

# Remove all tags of an image
docker rmi YOUR_USERNAME/docker_fastapi_poetry:latest \
           YOUR_USERNAME/docker_fastapi_poetry:v1.0.0
```

### Delete from Docker Hub

1. Go to your repository on Docker Hub
2. Click **"Tags"** tab
3. Check the tags you want to delete
4. Click **"Actions" → "Delete"**
5. Confirm deletion

**Note:** Deleting from Docker Hub doesn't affect local images

---

## Troubleshooting

### "denied: requested access to the resource is denied"

**Cause:** Not logged in or wrong credentials

**Solution:**
```bash
# Log out and log in again
docker logout
docker login

# Verify credentials
docker login --username YOUR_USERNAME
```

### "unauthorized: authentication required"

**Cause:** Token expired or invalid

**Solution:**
1. Create a new access token on Docker Hub
2. Log in with the new token
```bash
docker login --username YOUR_USERNAME
# Enter new token when prompted
```

### "name unknown: repository not found"

**Cause:** Repository doesn't exist on Docker Hub

**Solution:**
1. Check repository name spelling
2. Create repository on Docker Hub first
3. Ensure username is correct

### "repository name must be lowercase"

**Cause:** Docker Hub requires lowercase names

**Solution:**
```bash
# Wrong:
docker tag myapp YOUR_USERNAME/Docker_FastAPI_Poetry:latest

# Correct:
docker tag myapp YOUR_USERNAME/docker_fastapi_poetry:latest
```

### Rate Limiting Issues

**Problem:** Too many pulls from Docker Hub

**Free tier limits:**
- Unauthenticated: 100 pulls per 6 hours
- Authenticated: 200 pulls per 6 hours

**Solution:**
```bash
# Always log in to get higher limits
docker login

# Use local cache when possible
# Consider Docker Hub Pro for unlimited pulls
```

---

## Best Practices

### 1. Always Use Tags

```bash
# ❌ Bad (implicit :latest)
docker push YOUR_USERNAME/myapp

# ✅ Good (explicit tag)
docker push YOUR_USERNAME/myapp:v1.0.0
```

### 2. Never Use `latest` in Production

```bash
# ❌ Bad (unpredictable)
docker run myapp:latest

# ✅ Good (specific version)
docker run myapp:v1.0.0
```

### 3. Use Multi-Stage Builds

```dockerfile
# Reduces image size
FROM python:3.11-slim AS builder
# ... build steps

FROM python:3.11-slim
COPY --from=builder /app /app
```

### 4. Keep Images Small

```bash
# Check image size
docker images YOUR_USERNAME/docker_fastapi_poetry

# Use slim base images
FROM python:3.11-slim  # Not python:3.11

# Use .dockerignore
# Minimize layers
# Combine RUN commands
```

### 5. Scan for Vulnerabilities

```bash
# Use Docker Scout (built-in)
docker scout cves YOUR_USERNAME/docker_fastapi_poetry:latest

# Or use Snyk
docker scan YOUR_USERNAME/docker_fastapi_poetry:latest
```

### 6. Document Your Images

Add metadata to your Dockerfile:

```dockerfile
LABEL maintainer="you@example.com"
LABEL version="1.0.0"
LABEL description="FastAPI application with Docker and Poetry"
```

---

## Next Steps

Now that you can publish to Docker Hub, learn about:

- [GitHub Actions CI/CD](github-actions.md) - Automate builds and pushes
- [Docker Compose](docker-compose.md) - Multi-container applications
- [Environment Configuration](environment-config.md) - Manage secrets
- [Deployment Guide](deployment.md) - Deploy to production servers

---

**📖 Additional Resources:**
- [Docker Hub Documentation](https://docs.docker.com/docker-hub/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Docker Security](https://docs.docker.com/engine/security/)
