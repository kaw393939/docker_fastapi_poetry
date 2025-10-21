"""
FastAPI Application - Main Entry Point

This module defines the FastAPI application instance and all API routes.
FastAPI automatically generates interactive API documentation at
/docs and /redoc.

Key Concepts:
- FastAPI: Modern Python web framework for building APIs
- ASGI: Asynchronous Server Gateway Interface (async web server standard)
- Type Hints: Python 3.6+ feature for better IDE support and validation
- async/await: Python's built-in asynchronous programming support
"""

# Import the FastAPI class - the core of our application
from fastapi import FastAPI

# Create the FastAPI application instance
# This is the main object that handles all routing and middleware
app = FastAPI(
    title="Hello World API",  # Appears in /docs
    version="1.0.0",  # API version
    description="A simple FastAPI demo"  # Appears in /docs
)


# Route Decorator: @app.get("/") tells FastAPI to handle GET requests to "/"
# The function name doesn't matter for routing, only the decorator path matters
@app.get("/")
async def root():
    """
    Root endpoint - Returns a simple hello world message.
    
    This is the main endpoint of our API. When a client makes a GET request to
    the root URL (http://localhost:8001/), this function executes.
    
    Returns:
        dict: A JSON object with a message field

    Example Response:
        {"message": "Hello World"}

    Note:
        - 'async def' makes this an asynchronous function (non-blocking)
        - Even though we don't use 'await' here, async is good
          practice for APIs
        - FastAPI automatically converts the dict to JSON
    """
    return {"message": "Hello World"}


# Health Check Endpoint
# This is a common pattern for monitoring services in production
@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring and load balancers.
    
    Production systems often use health checks to:
    - Determine if the service is running
    - Monitor service availability
    - Trigger alerts when service is down
    - Load balancer routing decisions
    
    Returns:
        dict: Status indicator showing service is operational
        
    Example Response:
        {"status": "healthy"}
        
    Production Enhancement Ideas:
        - Check database connectivity
        - Verify external API connections
        - Return more detailed health metrics
        - Add authentication for sensitive health data
    """
    return {"status": "healthy"}


# Additional Route Examples (Commented Out)
# Uncomment and modify these to add more functionality

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     """
#     Path parameter example.
#     Access via: http://localhost:8001/items/5
#     """
#     return {"item_id": item_id}

# @app.get("/search")
# async def search(q: str = None):
#     """
#     Query parameter example.
#     Access via: http://localhost:8001/search?q=fastapi
#     """
#     return {"query": q}

# from pydantic import BaseModel
#
# class Item(BaseModel):
#     name: str
#     price: float
#
# @app.post("/items")
# async def create_item(item: Item):
#     """
#     POST request with request body validation.
#     FastAPI uses Pydantic models for automatic validation.
#     """
#     return {"item": item, "created": True}


# Application Lifecycle Events
# Use these for startup/shutdown tasks like database connections

# @app.on_event("startup")
# async def startup_event():
#     """
#     Runs once when the application starts.
#     Perfect for initializing database connections, loading models, etc.
#     """
#     print("Application starting up...")

# @app.on_event("shutdown")
# async def shutdown_event():
#     """
#     Runs once when the application shuts down.
#     Use for cleanup tasks like closing database connections.
#     """
#     print("Application shutting down...")

