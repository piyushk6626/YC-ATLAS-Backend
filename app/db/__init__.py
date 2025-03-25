"""Database related functionality for MongoDB connections and queries.

This module provides database connectivity and query functionalities for the YC ATLAS backend:

Key components:
- MongoDB connection management with connection pooling
- Query interfaces for company data retrieval
- Text and semantic search capabilities for company information
- Data transformation and serialization for API responses
- Schema validation for database operations
- Caching mechanisms for frequently accessed data

The module implements repository pattern to abstract database operations
from the rest of the application, enhancing maintainability and testability.
"""

from app.db.company_data import return_data, search_company_by_name
