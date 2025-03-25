"""Utilities for normalizing data from external sources."""

from typing import List, Dict, Any


def normalize_data(result) -> List[Dict[str, Any]]:
    """Normalize query results for consistent output format.
    
    This function takes search results in various formats and normalizes them
    to a consistent structure for the API response.
    
    Args:
        result: Input data in one of several possible formats
                (list, object with matches attribute, or dict with matches key)
    
    Returns:
        List[Dict[str, Any]]: A list of normalized items with id, score, and metadata
    """
    if isinstance(result, list):
        data = result  # Assume result is already a list
    elif hasattr(result, 'matches'):
        data = result.matches
    elif isinstance(result, dict) and "matches" in result:
        data = result["matches"]
    else:
        data = []  # Default to an empty list if the structure is unexpected
    
    normalized_data = []
    for item in data:
        normalized_item = {
            "id": item.id,
            "score": float(item.score),  # Convert score to float for JSON serialization
            "metadata": item.metadata
        }
        normalized_data.append(normalized_item)
    
    return normalized_data 