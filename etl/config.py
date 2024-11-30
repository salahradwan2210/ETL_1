"""Configuration settings for the ETL pipeline."""

# Data source configuration
SOURCE_URL = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"

# Database configuration (using SQLite for local storage)
DATABASE_PATH = "data/covid_data.db"

# ETL schedule configuration (in seconds)
SCHEDULE_INTERVAL = 3600  # Run every hour