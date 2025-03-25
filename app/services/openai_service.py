"""Service for interacting with OpenAI API."""

from openai import OpenAI
import logging
from typing import List, Any
from app.core.config import get_settings
from app.services.prompts import SystemPrompt, SystemPrompt_Question

# Get settings
settings = get_settings()

# Initialize OpenAI client
client = OpenAI(api_key=settings.openai_api_key)


def create_embeddings(content: str) -> List[float]:
    """Generate embeddings using OpenAI API.
    
    This function converts text content into a vector embedding
    that can be used for semantic search.
    
    Args:
        content: The text content to embed
        
    Returns:
        List[float]: Vector embedding of the content
        
    Raises:
        Exception: If there is an issue generating embeddings
    """
    try:
        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=content
        )
        return response.data[0].embedding
    except Exception as e:
        logging.error(f"Error generating embeddings: {e}")
        raise


def explain_user_query(query: str) -> str:
    """Refine user query using OpenAI's GPT model.
    
    This function enhances the user's query by generating a more detailed
    and focused description to improve search quality.
    
    Args:
        query: The original user query
        
    Returns:
        str: Refined and expanded query
        
    Raises:
        Exception: If there is an issue with the OpenAI API
    """
    try:
        messages = [
            {"role": "system", "content": SystemPrompt},
            {"role": "user", "content": query}
        ]
        
        response = client.chat.completions.create(
            messages=messages,
            model="gpt-4o-mini",
            temperature=0.9
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error explaining user query: {e}")
        # Fall back to original query if the API call fails
        return query


def deep_question(query: str) -> List[str]:
    """Generate research questions based on the query.
    
    This function creates multiple related questions to broaden
    the search and find more relevant results.
    
    Args:
        query: The original user query
        
    Returns:
        List[str]: List of generated research questions
        
    Raises:
        Exception: If there is an issue with the OpenAI API
    """
    try:
        messages = [
            {"role": "system", "content": SystemPrompt_Question},
            {"role": "user", "content": query}
        ]
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        
        return response.choices[0].message.content.split("\n")
    except Exception as e:
        logging.error(f"Error generating deep questions: {e}")
        # Fall back to just the original query
        return [query] 