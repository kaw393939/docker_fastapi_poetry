# GitHub Actions CI/CD Setup

This project uses GitHub Actions to automatically:
- ✅ Run tests on every push and pull request
- 🐳 Build and push Docker images to Docker Hub (on main branch only)

## Workflow Overview

### Test Job
Runs on every push and pull request:
1. Checks out code
2. Sets up Python 3.11
3. Installs Poetry
4. Caches dependencies for faster builds
5. Installs project dependencies
6. Runs pytest with coverage

### Build and Push Job
Runs only on pushes to `main` branch (after tests pass):
1. Checks out code
2. Sets up Docker Buildx
3. Logs in to Docker Hub
4. Extracts metadata (tags, labels)
5. Builds Docker image
6. Pushes to Docker Hub as `kaw393939/docker_fastapi_poetry`

## Required GitHub Secrets

You need to add these secrets to your GitHub repository:

### 1. DOCKERHUB_USERNAME
Your Docker Hub username.

**Value:** `kaw393939`

### 2. DOCKERHUB_TOKEN
A Docker Hub access token (NOT your password).

**How to create:**
1. Go to https://hub.docker.com/settings/security
2. Click "New Access Token"
3. Give it a description (e.g., "GitHub Actions")
4. Copy the token (you won't see it again!)

### Adding Secrets to GitHub

1. Go to your repository: https://github.com/kaw393939/docker_fastapi_poetry
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add both secrets:
   - Name: `DOCKERHUB_USERNAME`, Value: `kaw393939`
   - Name: `DOCKERHUB_TOKEN`, Value: `<your-token>`

## Docker Image Tags

Images are tagged with:
- `latest` - Latest build from main branch
- `main-<sha>` - Specific commit SHA from main
- `main` - Current main branch

**Example:**
```bash
# Pull latest image
docker pull kaw393939/docker_fastapi_poetry:latest

# Pull specific commit
docker pull kaw393939/docker_fastapi_poetry:main-abc1234

# Run the image
docker run -p 8001:8000 kaw393939/docker_fastapi_poetry:latest
```

## Workflow Files

- `.github/workflows/ci-cd.yml` - Main CI/CD pipeline

## Viewing Workflow Runs

1. Go to https://github.com/kaw393939/docker_fastapi_poetry/actions
2. Click on a workflow run to see details
3. Click on individual jobs to see logs

## Triggering Workflows

Workflows run automatically on:
- **Every push** to any branch (runs tests)
- **Every pull request** (runs tests)
- **Push to main** (runs tests + builds & pushes to Docker Hub)

## Build Cache

The workflow uses Docker layer caching to speed up builds:
- Cache stored as `kaw393939/docker_fastapi_poetry:buildcache`
- Significantly faster subsequent builds

## Troubleshooting

### Tests Failing
Check the test job logs to see which tests failed:
```bash
# Run tests locally first
poetry run pytest -v
```

### Docker Build Failing
- Check that Dockerfile is valid
- Test build locally:
```bash
docker build -t test .
```

### Docker Push Failing
- Verify secrets are set correctly
- Check Docker Hub token hasn't expired
- Ensure repository exists: https://hub.docker.com/r/kaw393939/docker_fastapi_poetry

### Secrets Not Working
- Secret names must match exactly (case-sensitive)
- Secrets are encrypted and can't be viewed after creation
- Delete and recreate if unsure

## Best Practices

✅ Always run tests locally before pushing  
✅ Keep Docker Hub tokens secure (never commit them)  
✅ Review workflow logs after each push  
✅ Use meaningful commit messages  
✅ Create pull requests for major changes  

## Next Steps

After setting up secrets:
1. Push a commit to trigger the workflow
2. Watch it run at https://github.com/kaw393939/docker_fastapi_poetry/actions
3. Check Docker Hub for your image: https://hub.docker.com/r/kaw393939/docker_fastapi_poetry

---

**Questions?** Open an issue on GitHub!
