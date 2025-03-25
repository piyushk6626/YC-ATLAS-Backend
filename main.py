# Fast API imports
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#FastAPI CORS middleware
from fastapi.middleware.cors import CORSMiddleware

# Import services
from services.pinecone_service import get_index, query_index
from services.openai_service import create_embeddings, explain_user_query, deep_question
from utils.data_normalization import normalize_data
from comapneydata import return_data
# Import logging
import logging

# Import multithreading
from concurrent.futures import ThreadPoolExecutor

# Import environment variables
from dotenv import load_dotenv
# Load environment variables
load_dotenv(override=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)


app = FastAPI()

# Allow all origins (adjust this as needed for your use case)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Or specify allowed origins, e.g., ["https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/search_companies")
def search_companies(request: QueryRequest):
    """Find similar companies based on a query string using Pinecone."""
    try:
        number_of_results = 30
        index = get_index()
        explained_query = explain_user_query(request.query)
        vector = create_embeddings(explained_query)
        results = query_index(index, vector, number_of_results)
        return normalize_data(results)
    except Exception as e:
        logging.error(f"Error in search_companies: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/deep_research")
def deep_research(request: QueryRequest):
    """Perform deep research using question generation and Pinecone search."""
    try:
        questions = deep_question(request.query)
        final_data = []
        
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda q: search_companies(QueryRequest(query=q)), questions))
        
        for data in results:
            for item in data:
                existing_item = next((x for x in final_data if x['id'] == item['id']), None)
                if existing_item is None:
                    final_data.append(item)
                else:
                    existing_item['score'] += item['score']
        
        final_data.sort(key=lambda x: x['score'], reverse=True)
        return final_data
    except Exception as e:
        logging.error(f"Error in deep_research: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/company/{id}")
def get_company(id: str):
    """Get company data by ID."""
    try:
        return return_data(id)  # Returns a valid JSON object
    except Exception as e:
        logging.error(f"Error in get_company: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

