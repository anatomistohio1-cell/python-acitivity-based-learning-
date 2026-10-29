routes = [
    ("Route A", 60, 45, 20, 70),
    ("Route B", 45, 55, 12, 40),
    ("Route C", 80, 70, 30, 75),
]

best_route = ""
best_efficiency = 0

print("BUS ROUTE PERFORMANCE")
print("{:<10} {:>10} {:>12} {:>12} {:>14} {:>14}".format(
    "Route", "Passengers", "Minutes", "Fuel (L)", "Pass./L", "Status"
))

for route in routes:
    name, passengers, minutes, fuel_litres, capacity = route
    efficiency = passengers / fuel_litres

    if passengers > capacity:
        status = "OVER CAPACITY"
    else:
        status = "Within capacity"

    if efficiency > best_efficiency:
        best_efficiency = efficiency
        best_route = name

    print("{:<10} {:>10} {:>12} {:>12.1f} {:>14.2f} {:>14}".format(
        name, passengers, minutes, fuel_litres, efficiency, status
    ))

print("\nBest fuel efficiency: {} ({:.2f} passengers per litre)".format(
    best_route, best_efficiency
))
