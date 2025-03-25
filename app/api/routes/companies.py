"""API routes for company data retrieval."""

from fastapi import APIRouter, HTTPException
import logging
from typing import Dict, Any

from app.db.company_data import return_data

router = APIRouter(tags=["companies"])


@router.get("/company/{id}")
async def get_company(id: str) -> Dict[str, Any]:
    """Get company data by ID or name.
    
    Args:
        id: Company ID or name
        
    Returns:
        Dict[str, Any]: Company data with full details
        
    Raises:
        HTTPException: If company not found or other errors occur
    """
    try:
        return return_data(id)
    except Exception as e:
        logging.error(f"Error in get_company: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") 