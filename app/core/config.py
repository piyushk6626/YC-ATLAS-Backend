"""Configuration module for the application."""

import os
import logging
from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)


class Settings(BaseSettings):
    """Application settings.
    
    Attributes:
        app_name: Name of the application
        openai_api_key: OpenAI API key
        pinecone_api_key: Pinecone API key
        pinecone_host_url: Pinecone host URL
        mongo_uri: MongoDB connection URI
        mongo_collection: MongoDB collection name
        debug: Debug mode flag
    """
    app_name: str = "YC ATLAS Backend"
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    pinecone_api_key: str = os.getenv("PINECONE_API_KEY", "")
    pinecone_host_url: str = os.getenv("PINECONE_HOST_URL2", "")
    mongo_uri: str = os.getenv("MONGO_URI", "")
    mongo_collection: str = os.getenv("COLLECTION_NAME", "companies")
    debug: bool = bool(os.getenv("DEBUG", False))


@lru_cache()
def get_settings() -> Settings:
    """Get cached application settings.
    
    Returns:
        Settings: Application settings instance
    """
    return Settings()


# Configure logging
logging.basicConfig(
    level=logging.INFO if not get_settings().debug else logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
) 