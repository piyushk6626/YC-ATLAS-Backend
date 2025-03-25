"""Main application module for YC ATLAS Backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.api.routes.search import router as search_router
from app.api.routes.companies import router as companies_router
from app.core.config import get_settings

# Get application settings
settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title="YC ATLAS API",
    description="AI-Powered YC Startup Search Engine",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
origins = ["*"]  # In production, replace with specific origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(search_router, prefix="/api")
app.include_router(companies_router, prefix="/api")


@app.get("/", tags=["health"])
async def root():
    """Root endpoint for API health check."""
    return {
        "status": "online",
        "app_name": settings.app_name,
        "version": "0.1.0"
    }


@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


# Run with: uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 