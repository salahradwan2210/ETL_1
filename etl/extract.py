"""Data extraction module."""
import urllib.request
import csv
from io import StringIO

def fetch_data(url):
    """Fetch data from the specified URL."""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def parse_csv(data):
    """Parse CSV data into a list of dictionaries."""
    if not data:
        return []
    
    csv_file = StringIO(data)
    reader = csv.DictReader(csv_file)
    return list(reader)