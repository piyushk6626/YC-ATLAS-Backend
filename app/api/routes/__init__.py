"""API routes for company search and data retrieval.

This module contains the route definitions for the YC ATLAS RESTful API:

Route categories:
- Search routes: Semantic and keyword-based company search endpoints
- Company routes: Detailed company information retrieval endpoints
- Authentication routes: User authentication and authorization
- Admin routes: Administrative functionality for data management
- Health check and monitoring endpoints
- Documentation and OpenAPI specification endpoints

Each route module follows a consistent pattern with:
- Path operation functions with appropriate HTTP methods
- Request validation using Pydantic models
- Response formatting with proper status codes
- Error handling with descriptive error messages
- Permission checks and rate limiting
- Logging and telemetry for request tracking

The routes are organized by resource type and functionality to maintain
a clean separation of concerns and improve maintainability.
"""

from app.api.routes.search import router as search_router
from app.api.routes.companies import router as companies_router
