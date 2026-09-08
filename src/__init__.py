"""
Weather Application - Data Engineering Learning Project

A complete weather application built through the full data engineering lifecycle.

This package implements a complete data engineering pipeline that:
- Extracts weather data from external APIs
- Transforms and validates the data
- Loads the data into a SQLite database
- Serves the data through an interactive dashboard
- Demonstrates key data engineering concepts

Package Structure:
- config.py: Configuration management from environment variables
- api_client.py: Weather API integration with retry logic
- database.py: SQLite database operations and schema management
- pipeline.py: Data processing pipeline orchestration
- dashboard.py: Terminal-based user interface

Why this matters: This package demonstrates the complete data engineering
lifecycle from data collection to data serving, using clean function-based
architecture suitable for learning and understanding core concepts.
"""

# Package version information
# Used for: Version tracking and compatibility checks
# Why: Helps users know which version they're using and enables version-dependent features
__version__ = "1.0.0"

# Package author information
# Used for: Attribution and contact information
# Why: Provides credit and contact details for the package maintainers
__author__ = "Weather Project Team"
