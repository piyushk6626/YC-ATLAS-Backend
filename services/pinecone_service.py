from pinecone import Pinecone
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_HOST_URL = os.getenv("PINECONE_HOST_URL2")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

def get_index():
    """Retrieve the Pinecone index."""
    return pc.Index(host=PINECONE_HOST_URL)

def query_index(index, query_vector, number_of_results):
    """Query Pinecone index with the provided vector."""
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
