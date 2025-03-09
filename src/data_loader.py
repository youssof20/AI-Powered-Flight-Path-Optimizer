import pandas as pd

def load_airports(file_path):
    """Load airport data from a CSV file."""
    return pd.read_csv(file_path)

def load_flights(file_path):
    """Load flight data from a CSV file."""
    return pd.read_csv(file_path)
