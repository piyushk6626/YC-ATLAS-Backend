"""API routes for search functionality."""

from fastapi import APIRouter, HTTPException, Depends
from concurrent.futures import ThreadPoolExecutor
import logging

from app.api.models import QueryRequest, SearchResponse
from app.services.pinecone_service import get_index, query_index
from app.services.openai_service import create_embeddings, explain_user_query, deep_question
from app.utils.data_normalization import normalize_data

router = APIRouter(tags=["search"])


@router.post("/search_companies", response_model=SearchResponse)
async def search_companies(request: QueryRequest) -> SearchResponse:
    """Find similar companies based on a query string using Pinecone.
    
    Args:
        request: Search query request
        
    Returns:
        SearchResponse: Normalized search results
        
    Raises:
        HTTPException: If an error occurs during search
    """
    try:
        number_of_results = 30
        index = get_index()
        explained_query = explain_user_query(request.query)
        vector = create_embeddings(explained_query)
        results = query_index(index, vector, number_of_results)
        
        return SearchResponse(results=normalize_data(results))
    except Exception as e:
        logging.error(f"Error in search_companies: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/deep_research", response_model=SearchResponse)
async def deep_research(request: QueryRequest) -> SearchResponse:
    """Perform deep research using question generation and Pinecone search.
    
    This endpoint expands the original query into multiple questions
    and performs parallel searches with all of them to find more comprehensive results.
    
    Args:
        request: Search query request
        
    Returns:
        SearchResponse: Combined and ranked search results
        
    Raises:
        HTTPException: If an error occurs during research
    """
    try:
        questions = deep_question(request.query)
        final_data = []
        
        with ThreadPoolExecutor() as executor:
            # Create query requests for each question
            query_requests = [QueryRequest(query=q) for q in questions]
            # Execute searches in parallel
            results = list(executor.map(search_companies, query_requests))
        
        # Combine and deduplicate results
        for data in results:
            for item in data.results:
                existing_item = next((x for x in final_data if x['id'] == item['id']), None)
                if existing_item is None:
                    final_data.append(item)
                else:
                    existing_item['score'] += item['score']
        
        # Sort by final score
        final_data.sort(key=lambda x: x['score'], reverse=True)
        return SearchResponse(results=final_data)
    except Exception as e:
        logging.error(f"Error in deep_research: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") 