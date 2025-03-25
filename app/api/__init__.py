"""API package for routes and models.

This module implements the RESTful API interface for the YC ATLAS platform:

Key features:
- FastAPI-based RESTful endpoints for company data retrieval and search
- Pydantic models for request/response validation and documentation
- Comprehensive API documentation with Swagger UI integration
- Rate limiting and authentication mechanisms
- Error handling and custom exception responses
- Versioned API endpoints for backward compatibility
- Modular router architecture organized by resource type

The API follows REST best practices with proper HTTP status codes,
content negotiation, and hypermedia links where appropriate.
"""

from app.api.models import QueryRequest
