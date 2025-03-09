import networkx as nx
import pandas as pd

class FlightOptimizer:
    def __init__(self, airports, flights):
        """Initialize the flight optimizer with airport and flight data."""
        self.airports = airports
        self.flights = flights
        self.graph = self._build_graph()

    def _build_graph(self):
        """Build a graph representation of the flight network."""
        graph = nx.Graph()
        for _, flight in self.flights.iterrows():
            graph.add_edge(flight['origin'], flight['destination'], weight=flight['distance'])
        return graph

    def find_shortest_path(self, origin, destination):
        """Find the shortest path between two airports."""
        return nx.shortest_path(self.graph, source=origin, target=destination, weight='weight')

    def optimize_flight_path(self, origin, destination):
        """Optimize the flight path between two airports."""
        return self.find_shortest_path(origin, destination)
