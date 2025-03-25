"""Core application functionality and configuration.

This module contains the fundamental components and settings for the YC ATLAS backend:

Key components:
- Application configuration management with environment variable integration
- Dependency injection system for service resolution
- Application lifecycle management (startup/shutdown events)
- Middleware configuration for CORS, security, and logging
- Security features including API key validation and rate limiting
- Constants and enumerations used throughout the application
- Application events and listeners for extensibility

The core module establishes the foundation for the application architecture,
ensuring proper initialization and configuration of all system components.
"""

from app.core.config import get_settings
