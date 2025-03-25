"""Utility functions for data processing and normalization.

This module provides general-purpose utilities and helper functions for the YC ATLAS backend:

Key functionality:
- Data cleaning and normalization for company information
- Text processing utilities for search optimization
- Date and time manipulation functions
- Serialization/deserialization helpers for various data formats
- Caching decorators and utilities for performance optimization
- Logging and monitoring utilities
- Error handling and exception formatting
- Security utilities including encryption and hashing functions
- Performance measurement and optimization tools

These utilities are designed to be reusable across different modules
and provide consistent approaches to common tasks throughout the application.
"""

from app.utils.data_normalization import normalize_data
