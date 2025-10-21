# GitHub Actions CI/CD Setup

## What is CI/CD?

**CI/CD** stands for **Continuous Integration / Continuous Deployment**:

- **Continuous Integration (CI)**: Automatically test your code every time you push changes
- **Continuous Deployment (CD)**: Automatically build and deploy your application when tests pass

### Why Use CI/CD?

✅ **Catch bugs early** - Tests run automatically on every commit  
✅ **Prevent bad code** - Failing tests block merges to main branch  
✅ **Automate repetitive tasks** - No manual testing/building/deploying  
✅ **Maintain code quality** - Enforce standards on every change  
✅ **Fast feedback** - Know within minutes if changes break anything  
✅ **Deployment confidence** - Only tested code reaches production  

---

## Our CI/CD Pipeline

This project uses GitHub Actions to automatically:
- ✅ Run tests on every push and pull request
- 📊 Generate code coverage reports
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

---

## Understanding the Workflow File

The workflow is defined in `.github/workflows/ci-cd.yml`. Let's break down the key sections:

### Workflow Triggers

```yaml
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
```

**What this means:**
- Runs on pushes to `main` or `develop` branches
- Runs on pull requests targeting `main` branch
- Ensures all code is tested before merging

### Test Job Explained

```yaml
test:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install Poetry
      run: |
        curl -sSL https://install.python-poetry.org | python3 -
        export PATH="$HOME/.local/bin:$PATH"
    - name: Install Dependencies
      run: poetry install --no-root
    - name: Run Tests with Coverage
      run: poetry run pytest -v --cov=app --cov-report=term-missing
```

**Step by step:**
1. **runs-on: ubuntu-latest** - Uses GitHub's Ubuntu runner
2. **checkout** - Downloads your repository code
3. **Set up Python** - Installs Python 3.11
4. **Install Poetry** - Installs Poetry dependency manager
5. **Install Dependencies** - Installs project dependencies
6. **Run Tests** - Executes pytest with coverage reporting

### Build Job Explained

```yaml
build:
  needs: test
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
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ secrets.DOCKERHUB_USERNAME }}/docker_fastapi_poetry
        tags: |
          type=raw,value=latest,enable={{is_default_branch}}
          type=sha,prefix={{branch}}-
          type=ref,event=branch
    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=registry,ref=${{ secrets.DOCKERHUB_USERNAME }}/docker_fastapi_poetry:buildcache
        cache-to: type=registry,ref=${{ secrets.DOCKERHUB_USERNAME }}/docker_fastapi_poetry:buildcache,mode=max
```

**Key concepts:**
1. **needs: test** - Only runs if test job succeeds
2. **if: github.ref == 'refs/heads/main'** - Only runs on main branch
3. **Docker Buildx** - Advanced Docker builder with caching
4. **metadata-action** - Generates tags automatically based on git context
5. **build-push-action** - Builds and pushes in one step
6. **cache-from/cache-to** - Uses layer caching for faster builds

---

## Workflow Execution Patterns

### Feature Branch Workflow

```
Developer creates feature/add-users branch
    ↓
git push origin feature/add-users
    ↓
GitHub Actions triggered
    ↓
[Test Job Runs]
    ├── ✅ Tests pass → Green checkmark
    └── ❌ Tests fail → Red X, prevents merge
    
No Docker build/push (not main branch)
```

### Main Branch Workflow

```
Pull request merged to main
    ↓
[Test Job Runs]
    ├── ❌ Fails → Stop here
    └── ✅ Passes → Continue
         ↓
    [Build Job Runs]
         ├── Build Docker image
         ├── Tag with latest, main, sha
         └── Push to Docker Hub
              ↓
         Image available at:
         kaw393939/docker_fastapi_poetry:latest
```

### Pull Request Workflow

```
Developer opens PR to main
    ↓
[Test Job Runs]
    ├── ✅ Pass → "All checks passed" on PR
    └── ❌ Fail → "Some checks failed" on PR
    
Status shown on PR page
Prevents merge until fixed
```

---

## Setting Up from Scratch

### Step 1: Fork/Clone Repository

```bash
git clone https://github.com/kaw393939/docker_fastapi_poetry.git
cd docker_fastapi_poetry
```

### Step 2: Create Docker Hub Repository

1. Go to [Docker Hub](https://hub.docker.com/)
2. Click "Create Repository"
3. Name: `docker_fastapi_poetry`
4. Visibility: Public or Private
5. Click "Create"

### Step 3: Create Docker Hub Access Token

1. Go to [Docker Hub Security Settings](https://hub.docker.com/settings/security)
2. Click "New Access Token"
3. Description: `github-actions`
4. Permissions: Read, Write, Delete
5. Click "Generate"
6. **Copy the token** (won't be shown again!)

### Step 4: Add Secrets to GitHub

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**

**Add DOCKERHUB_USERNAME:**
- Name: `DOCKERHUB_USERNAME`
- Value: Your Docker Hub username
- Click "Add secret"

**Add DOCKERHUB_TOKEN:**
- Name: `DOCKERHUB_TOKEN`
- Value: The access token from Step 3
- Click "Add secret"

### Step 5: Enable GitHub Actions

1. Go to **Actions** tab
2. If prompted, click "I understand my workflows, go ahead and enable them"

### Step 6: Test the Workflow

```bash
# Make any change
echo "# Test" >> README.md

# Commit and push
git add README.md
git commit -m "Test CI/CD pipeline"
git push origin main
```

### Step 7: Monitor Execution

1. Go to **Actions** tab on GitHub
2. Click on your workflow run
3. Watch jobs execute in real-time
4. Check for green checkmarks (✅) or red X's (❌)

---

## Viewing Test Coverage

After tests run, you can see coverage in the logs:

```
---------- coverage: platform linux, python 3.11 ----------
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
app/__init__.py         0      0   100%
app/main.py             8      0   100%
-------------------------------------------------
TOTAL                   8      0   100%
```

**Coverage metrics:**
- **Stmts** - Total statements in file
- **Miss** - Statements not covered by tests
- **Cover** - Percentage covered
- **Missing** - Line numbers not tested

---

## Advanced: Customizing the Workflow

### Run on All Branches

```yaml
on:
  push:
    branches: [ '**' ]  # Matches all branches
```

### Add Multiple Python Versions

```yaml
strategy:
  matrix:
    python-version: ['3.10', '3.11', '3.12']
```

### Run Tests on Schedule

```yaml
on:
  schedule:
    - cron: '0 0 * * 0'  # Every Sunday at midnight
```

### Add Slack Notifications

```yaml
- name: Notify on failure
  if: failure()
  uses: slackapi/slack-github-action@v1
  with:
    webhook: ${{ secrets.SLACK_WEBHOOK }}
    payload: |
      {
        "text": "Build failed on ${{ github.repository }}"
      }
```

### Deploy to Production

```yaml
- name: Deploy to Production
  if: github.ref == 'refs/heads/main'
  run: |
    ssh user@server "docker pull $IMAGE && docker-compose up -d"
```

---

## Troubleshooting Common Issues

### ❌ "Error: secrets.DOCKERHUB_USERNAME is not set"

**Problem:** Secret not configured in repository settings

**Solution:**
1. Go to Settings → Secrets and variables → Actions
2. Verify both `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` exist
3. Names must match exactly (case-sensitive)

### ❌ "docker login failed: unauthorized"

**Problem:** Invalid Docker Hub credentials

**Solution:**
1. Verify token hasn't expired
2. Check token has Write permissions
3. Create a new token if needed
4. Update the `DOCKERHUB_TOKEN` secret

### ❌ Tests Pass Locally But Fail in CI

**Possible causes:**
- Different Python versions
- Missing dependencies in `pyproject.toml`
- Hardcoded paths (use relative paths)
- Time zone or locale differences

**Solution:**
```bash
# Match CI environment
python -m venv venv
source venv/bin/activate
pip install poetry
poetry install --no-root
poetry run pytest -v
```

### ❌ "Workflow doesn't trigger"

**Check:**
- Workflow file is in `.github/workflows/` directory
- File has `.yml` or `.yaml` extension
- YAML syntax is valid (use YAML linter)
- Actions are enabled in repository settings

### ❌ Docker Build Fails: "no such file or directory"

**Problem:** File exists locally but not in Docker context

**Solution:**
- Check `.dockerignore` file
- Ensure file is committed to git
- Verify `COPY` paths in Dockerfile

---

## Best Practices

### 1. Use Specific Action Versions

```yaml
# ❌ Bad (uses latest, might break)
- uses: actions/checkout@main

# ✅ Good (pinned version)
- uses: actions/checkout@v4
```

### 2. Separate Test and Deploy Jobs

```yaml
jobs:
  test:
    # ... test steps
  
  deploy:
    needs: test  # Only runs if tests pass
    # ... deploy steps
```

### 3. Use Build Caching

```yaml
cache-from: type=registry,ref=user/app:buildcache
cache-to: type=registry,ref=user/app:buildcache,mode=max
```

### 4. Set Timeouts

```yaml
jobs:
  test:
    timeout-minutes: 10  # Prevent hanging jobs
```

### 5. Use Concurrency Groups

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true  # Cancel old runs
```

### 6. Protect Secrets

```yaml
# ✅ Good - use secrets
password: ${{ secrets.MY_SECRET }}

# ❌ Bad - never hardcode
password: "my-password-123"
```

---

## Monitoring and Debugging

### View Workflow Logs

1. Go to **Actions** tab
2. Click on workflow run
3. Click on job name
4. Expand steps to see detailed logs

### Download Logs

1. Click **...** (three dots) on workflow run
2. Select "Download log archive"
3. Extract and search logs locally

### Re-run Failed Workflows

1. Click on failed workflow
2. Click "Re-run failed jobs" or "Re-run all jobs"

### Debug with SSH (Advanced)

Add this step to debug issues:

```yaml
- name: Setup tmate session
  if: failure()
  uses: mxschmitt/action-tmate@v3
```

---

## Cost Considerations

### GitHub Actions Free Tier

**For public repositories:**
- ✅ Unlimited minutes
- ✅ Unlimited storage
- ✅ All features included

**For private repositories:**
- 2,000 minutes/month (Free)
- $0.008 per minute after

### Optimizing Costs

1. **Use caching** - Faster builds use fewer minutes
2. **Cancel redundant runs** - Don't run old commits
3. **Conditional jobs** - Only build when needed
4. **Self-hosted runners** - Free, use your own hardware

---

## Next Steps

Now that you understand GitHub Actions:

- [Docker Hub Publishing](docker-hub.md) - Manual image publishing
- [Deployment Guide](deployment.md) - Deploy to production servers
- [Security Best Practices](security.md) - Secure your CI/CD pipeline
- [Monitoring Guide](monitoring.md) - Track application health

---

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Build Push Action](https://github.com/docker/build-push-action)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
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
