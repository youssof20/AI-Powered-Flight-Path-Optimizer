import unittest
import pandas as pd
from src.data_loader import load_airports, load_flights

class TestDataLoader(unittest.TestCase):
    def test_load_airports(self):
        airports = load_airports('data/airports.csv')
        self.assertIsInstance(airports, pd.DataFrame)

    def test_load_flights(self):
        flights = load_flights('data/flights.csv')
        self.assertIsInstance(flights, pd.DataFrame)

if __name__ == "__main__":
    unittest.main()
