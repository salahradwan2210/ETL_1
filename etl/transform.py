"""Data transformation module."""

def clean_data(records):
    """Clean and transform the raw data."""
    cleaned_records = []
    
    for record in records:
        # Convert string numbers to integers/floats
        try:
            cleaned_record = {
                'date': record['Date'],
                'country': record['Country'],
                'confirmed': int(record['Confirmed'] or 0),
                'recovered': int(record['Recovered'] or 0),
                'deaths': int(record['Deaths'] or 0)
            }
            cleaned_records.append(cleaned_record)
        except (ValueError, KeyError) as e:
            print(f"Error cleaning record: {e}")
            continue
    
    return cleaned_records