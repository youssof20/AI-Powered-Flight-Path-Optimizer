import unittest
from src.flight_optimizer import FlightOptimizer
from src.data_loader import load_airports, load_flights

class TestFlightOptimizer(unittest.TestCase):
    def setUp(self):
        self.airports = load_airports('data/airports.csv')
        self.flights = load_flights('data/flights.csv')
        self.optimizer = FlightOptimizer(self.airports, self.flights)

    def test_find_shortest_path(self):
        path = self.optimizer.find_shortest_path('JFK', 'LAX')
        self.assertIsInstance(path, list)

if __name__ == "__main__":
    unittest.main()
