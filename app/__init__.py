"""YC ATLAS Backend - AI-Powered YC Startup Search Engine.

This application serves as the backend for the YC ATLAS platform, providing:
1. Fast semantic search capabilities for YC startups
2. API endpoints for querying and retrieving detailed company information
3. AI-powered analysis of company data and user queries
4. Vector database integration for efficient similarity search
5. OpenAI integration for natural language processing and embeddings

The system architecture follows a modular design with separate components for:
- API routes and models (app.api)
- Database connectivity and queries (app.db)
- Core configuration and settings (app.core)
- External service integrations (app.services)
- Utility functions for data processing (app.utils)

Built with FastAPI, MongoDB, Pinecone, and OpenAI technologies.
"""

__version__ = "0.1.0"
