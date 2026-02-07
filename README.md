# async-demo

A FastAPI application demonstrating async HTTP requests to multiple APIs.

## Features

- Async API calls using `httpx`
- Parallel requests with `asyncio.gather()`
- Endpoints: `/cat-fact`, `/advice`, `/joke`, `/home`

## Running with Docker Compose

### Prerequisites
- Docker and Docker Compose installed

### Quick Start

1. **Build and start the application:**
   ```bash
   docker compose up --build
   ```
   - `--build`: Forces rebuild of the image (use on first run or after code changes)
   - `-d`: Add this flag to run in detached mode (background)

2. **Access the application:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs

3. **View logs:**
   ```bash
   docker compose logs -f
   ```
   - `-f`: Follow log output in real-time

4. **Stop the application:**
   ```bash
   docker compose down
   ```

### Useful Commands

```bash
# Start services in background
docker compose up -d

# Rebuild and start (after code/dependency changes)
docker compose up --build

# Stop services
docker compose stop

# Stop and remove containers, networks
docker compose down

# View running containers
docker compose ps

# Execute command in running container
docker compose exec web bash

# View real-time logs
docker compose logs -f web
```

## Development

The docker-compose.yml includes volume mounts, so code changes are reflected immediately thanks to uvicorn's `--reload` flag.

## Running without Docker

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```