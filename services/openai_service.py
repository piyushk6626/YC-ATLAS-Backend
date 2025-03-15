from openai import OpenAI
import os
import logging
from dotenv import load_dotenv
from .prompts import SystemPrompt, SystemPrompt_Question

# Load environment variables
load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def create_embeddings(content):
    """Generate embeddings using OpenAI API."""
    try:
        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=content
        )
        return response.data[0].embedding
    except Exception as e:
        logging.error(f"Error generating embeddings: {e}")
        return None

def explain_user_query(query: str) -> str:
    """Refine user query using OpenAI's GPT model."""
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

def deep_question(query: str) -> list:
    """Generate research questions based on the query."""
    messages = [
        {"role": "system", "content": SystemPrompt_Question},
        {"role": "user", "content": query}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    
    return response.choices[0].message.content.split("\n")
