"""Pydantic models for API requests and responses."""

from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional


class QueryRequest(BaseModel):
    """Request model for search queries.
    
    Attributes:
        query: The search query string
    """
    query: str = Field(..., description="The search query string")


class CompanyMetadata(BaseModel):
    """Model for company metadata.
    
    This is a flexible model that can accommodate different fields
    in the company metadata.
    """
    name: Optional[str] = Field(None, description="Company name")
    description: Optional[str] = Field(None, description="Company description")
    website: Optional[str] = Field(None, description="Company website URL")
    industry: Optional[List[str]] = Field(None, description="Industry sectors")
    founding_date: Optional[str] = Field(None, description="Company founding date")
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields


class CompanyResult(BaseModel):
    """Model for company search result.
    
    Attributes:
        id: Unique company identifier
        score: Relevance score from the search
        metadata: Company metadata
    """
    id: str = Field(..., description="Unique company identifier")
    score: float = Field(..., description="Relevance score")
    metadata: Dict[str, Any] = Field(..., description="Company metadata")


class SearchResponse(BaseModel):
    """Response model for search endpoints.
    
    Attributes:
        results: List of company results
    """
    results: List[CompanyResult] = Field([], description="Search results") 