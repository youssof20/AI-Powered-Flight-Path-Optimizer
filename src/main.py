from data_loader import load_airports, load_flights
from flight_optimizer import FlightOptimizer
from utils import visualize_flight_path

def main():
    # Load data
    airports = load_airports('data/airports.csv')
    flights = load_flights('data/flights.csv')

    # Optimize flight path
    optimizer = FlightOptimizer(airports, flights)
    origin = 'JFK'
    destination = 'LAX'
    optimized_path = optimizer.optimize_flight_path(origin, destination)

    # Visualize the optimized path
    visualize_flight_path(optimizer.graph, optimized_path)

    print(f"Optimized flight path from {origin} to {destination}: {optimized_path}")

if __name__ == "__main__":
    main()
