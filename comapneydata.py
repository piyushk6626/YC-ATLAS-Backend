import os
import json
import logging
from fastapi import HTTPException
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
import certifi
import ssl


# Load environment variables
load_dotenv(override=True)

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
COLLECTION_NAME = "companies"
import os
import json
import logging
from fastapi import HTTPException
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
import certifi

# Load environment variables
load_dotenv(override=True)

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
COLLECTION_NAME = "companies"

# Make sure your MONGO_URI has the actual password (not <db_password>)
# MongoDB client with updated TLS parameters
client = MongoClient(
    MONGO_URI,
    server_api=ServerApi('1'),
    tls=True,
    tlsCAFile=certifi.where(),
    connectTimeoutMS=30000,
    socketTimeoutMS=30000
)

db = client.get_database(name='sample_mflix')
collection = db[COLLECTION_NAME]

db = client.get_database(name='sample_mflix')
collection = db[COLLECTION_NAME]
def convert_objectid(obj):
    """Recursively converts ObjectId fields to strings in a dictionary or list."""
    if isinstance(obj, dict):
        return {k: convert_objectid(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_objectid(v) for v in obj]
    elif isinstance(obj, ObjectId):
        return str(obj)
    else:
        return obj


def return_data(id: str):
    
    try:
        data=search_company_by_name(id)
        
        return convert_objectid(data[0])
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Company not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON format")

def search_company_by_name(name: str):
    """Search for companies by name in MongoDB"""
    try:
        results = list(collection.find({"name": {"$regex": name, "$options": "i"}}).limit(10))
        if not results:
            raise HTTPException(status_code=404, detail="No companies found")
        return results
    except Exception as e:
        logging.error(f"Error searching for company: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")       

   
if __name__ == "__main__":
    #print(return_data('1'))
    print(type(search_company_by_name('ZeroEntropy')))
    p=(search_company_by_name('ZeroEntropy'))
    print(p[0])
    print(type(p[0]))