import unittest
import networkx as nx
from src.utils import visualize_flight_path

class TestUtils(unittest.TestCase):
    def test_visualize_flight_path(self):
        graph = nx.Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        visualize_flight_path(graph, ['A', 'B', 'C'])
        # Manual verification required for visualization

if __name__ == "__main__":
    unittest.main()
