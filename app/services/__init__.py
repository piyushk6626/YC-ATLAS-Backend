"""Services package for handling external API integrations and data operations.

This module implements integration with external services and data processing capabilities:

Key services:
- Pinecone vector database integration for similarity search operations
- OpenAI API integration for embeddings generation and semantic analysis
- Data processing and transformation services
- Caching and performance optimization for external service calls
- Error handling and retry mechanisms for resilient external communications
- Asynchronous processing of long-running operations
- Rate limiting and throttling to respect external API constraints
- Service monitoring and telemetry for performance tracking

The services module abstracts external dependencies behind clean interfaces,
allowing for easy testing, mocking, and potential replacement of providers.
"""

from app.services.pinecone_service import get_index, query_index
from app.services.openai_service import create_embeddings, explain_user_query, deep_question
