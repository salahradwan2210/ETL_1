"""Main entry point for the ETL pipeline."""
import time
from etl import config
from etl.pipeline import run_pipeline

def main():
    """Main function to run the ETL pipeline periodically."""
    print("Starting ETL service...")
    
    while True:
        try:
            run_pipeline()
        except Exception as e:
            print(f"Error in pipeline execution: {e}")
        
        print(f"Waiting {config.SCHEDULE_INTERVAL} seconds until next run...")
        time.sleep(config.SCHEDULE_INTERVAL)

if __name__ == "__main__":
    main()