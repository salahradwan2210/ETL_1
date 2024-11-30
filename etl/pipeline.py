"""Main ETL pipeline orchestration."""
import time
from . import config
from .extract import fetch_data, parse_csv
from .transform import clean_data
from .load import init_database, load_data

def run_pipeline():
    """Execute the complete ETL pipeline."""
    print("Starting ETL pipeline...")
    
    # Initialize database
    init_database(config.DATABASE_PATH)
    
    # Extract
    print("Extracting data...")
    raw_data = fetch_data(config.SOURCE_URL)
    records = parse_csv(raw_data)
    
    # Transform
    print("Transforming data...")
    transformed_data = clean_data(records)
    
    # Load
    print("Loading data...")
    load_data(transformed_data, config.DATABASE_PATH)
    
    print("ETL pipeline completed successfully!")