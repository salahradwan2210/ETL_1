This project implements an ETL (Extract, Transform, Load) pipeline for processing COVID-19 data. Here's a detailed description of its components and functionality:

Project Structure
The project is organized into modular components, each with a specific responsibility:


├── etl/
│   ├── config.py        # Configuration settings
│   ├── extract.py       # Data extraction logic
│   ├── transform.py     # Data transformation logic
│   ├── load.py         # Database loading logic
│   └── pipeline.py     # Pipeline orchestration
├── main.py             # Main entry point
└── requirements.txt    # Project dependencies
Key Components
Data Source

Fetches COVID-19 data from a public GitHub repository
Uses CSV format containing country-wise aggregated statistics
Data includes confirmed cases, recoveries, and deaths
ETL Pipeline Stages

Extract:

Downloads raw data from the source URL
Parses CSV data into a structured format
Handles network errors and data fetching issues
Transform:

Cleans and validates the raw data
Converts string values to appropriate numeric types
Handles missing or invalid data points
Structures data for database storage
Load:

Uses SQLite as the local database
Creates necessary database tables automatically
Implements upsert logic to handle data updates
Ensures data integrity with proper error handling
Automation Features

Runs continuously with configurable intervals (default: hourly)
Automatic database initialization
Error handling and recovery mechanisms
Logging of pipeline execution status
Technical Details

Built with Python standard library (no external dependencies)
Uses SQLite for portable, file-based database storage
Implements proper resource cleanup and connection handling
Modular design for easy maintenance and updates
Key Features
Automated Data Processing: Continuously updates data without manual intervention
Error Resilience: Handles network issues and data inconsistencies gracefully
Data Integrity: Ensures consistent and reliable data storage
Scalability: Modular design allows for easy extensions and modifications
Maintainability: Clear separation of concerns with focused components
Usage
The pipeline can be started by running:


python main.py
This will initiate the ETL process, which will:

Create necessary data directories and database
Fetch the latest COVID-19 data
Process and clean the data
Store it in the SQLite database
Repeat the process at configured intervals
The project is designed to be lightweight, reliable, and suitable for both local development and production environments.
