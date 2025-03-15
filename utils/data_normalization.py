def normalize_data(result):
    """Normalize query results for consistent output format."""
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
