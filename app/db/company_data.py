"""Database operations for company data stored in MongoDB."""

import os
import json
import logging
from fastapi import HTTPException
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
import certifi
from typing import List, Dict, Any, Optional

from app.core.config import get_settings

# Get settings
settings = get_settings()

# MongoDB Connection setup with improved error handling
try:
    client = MongoClient(
        settings.mongo_uri,
        server_api=ServerApi('1'),
        tls=True,
        tlsCAFile=certifi.where(),
        connectTimeoutMS=30000,
        socketTimeoutMS=30000
    )
    
    # Test connection
    client.admin.command('ping')
    logging.info("Successfully connected to MongoDB")
    
    # Get database and collection
    db = client.get_database(name='sample_mflix')
    collection = db[settings.mongo_collection]
except Exception as e:
    logging.error(f"Failed to connect to MongoDB: {e}")
    # Don't raise here to allow application to start even if DB is temporarily down


def convert_objectid(obj: Any) -> Any:
    """Recursively converts ObjectId fields to strings in a dictionary or list.
    
    This function ensures MongoDB ObjectId instances are converted to strings
    for JSON serialization.
    
    Args:
        obj: The object to convert (dict, list, ObjectId, or other)
        
    Returns:
        The object with ObjectId instances converted to strings
    """
    if isinstance(obj, dict):
        return {k: convert_objectid(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_objectid(v) for v in obj]
    elif isinstance(obj, ObjectId):
        return str(obj)
    else:
        return obj


def return_data(id: str) -> Dict[str, Any]:
    """Get company data by ID or name.
    
    Args:
        id: Company ID or name
        
    Returns:
        Dict[str, Any]: Company data
        
    Raises:
        HTTPException: If company not found or other errors occur
    """
    try:
        data = search_company_by_name(id)
        
        if not data or len(data) == 0:
            raise HTTPException(status_code=404, detail="Company not found")
            
        return convert_objectid(data[0])
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logging.error(f"Error retrieving company data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


def search_company_by_name(name: str) -> List[Dict[str, Any]]:
    """Search for companies by name in MongoDB.
    
    Args:
        name: Company name or partial name
        
    Returns:
        List[Dict[str, Any]]: List of matching companies
        
    Raises:
        HTTPException: If no companies found or other errors occur
    """
    try:
        results = list(collection.find({"name": {"$regex": name, "$options": "i"}}).limit(10))
        if not results:
            raise HTTPException(status_code=404, detail="No companies found")
        return results
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logging.error(f"Error searching for company: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") 