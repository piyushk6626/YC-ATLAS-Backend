"""Service for interacting with Pinecone vector database."""

from pinecone import Pinecone
import os
import logging
from typing import List, Dict, Any
from app.core.config import get_settings


# Get settings
settings = get_settings()

# Initialize Pinecone client
pc = Pinecone(api_key=settings.pinecone_api_key)


def get_index():
    """Retrieve the Pinecone index.
    
    Returns:
        Pinecone.Index: The initialized Pinecone index
    
    Raises:
        Exception: If there is an issue connecting to Pinecone
    """
    try:
        return pc.Index(host=settings.pinecone_host_url)
    except Exception as e:
        logging.error(f"Error connecting to Pinecone: {e}")
        raise


def query_index(index, query_vector: List[float], number_of_results: int = 10) -> List[Dict[str, Any]]:
    """Query Pinecone index with the provided vector.
    
    This function performs a similarity search against the Pinecone vector database
    to find the most similar vectors to the query vector.
    
    Args:
        index: The Pinecone index to query
        query_vector: Vector embedding of the query
        number_of_results: Number of results to return
    
    Returns:
        List of matching documents with their similarity scores and metadata
        
    Raises:
        Exception: If there is an issue querying the index
    """
    try:
        response = index.query_namespaces(
            vector=query_vector,
            namespaces=[""],  # Search in the default namespace
            metric="cosine",
            top_k=number_of_results,
            include_values=False,
            include_metadata=True,
            show_progress=False,
        )
        
        return response.matches if hasattr(response, 'matches') else response.get("matches", response)
    except Exception as e:
        logging.error(f"Error querying Pinecone index: {e}")
        raise 