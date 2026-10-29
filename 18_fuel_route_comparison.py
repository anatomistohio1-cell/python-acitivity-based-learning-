distance_km = 180
fuel_price = 105
reserve_litres = 2
vehicles = [
    ("City Car", 15, 20),
    ("Family Car", 12, 14),
    ("Motorcycle", 40, 8),
]

best_name = ""
best_cost = 0

print("Route distance: {} km".format(distance_km))
print("Fuel price: Rs. {:.2f} per litre".format(fuel_price))
print("Required reserve: {:.1f} litres".format(reserve_litres))
print()
print("{:<16} {:>12} {:>12} {:>12} {:>14}".format(
    "Vehicle", "Fuel (L)", "Tank (L)", "Cost (Rs.)", "Decision"
))

for vehicle in vehicles:
    name, mileage, tank_capacity = vehicle
    fuel_needed = distance_km / mileage
    trip_cost = fuel_needed * fuel_price

    if fuel_needed + reserve_litres <= tank_capacity:
        decision = "Feasible"
        if best_name == "" or trip_cost < best_cost:
            best_name = name
            best_cost = trip_cost
    else:
        decision = "Not feasible"

    print("{:<16} {:>12.2f} {:>12.2f} {:>12.2f} {:>14}".format(
        name, fuel_needed, tank_capacity, trip_cost, decision
    ))

if best_name == "":
    print("\nNo vehicle can complete the route with the required reserve.")
else:
    print("\nLowest-cost feasible vehicle: {}".format(best_name))
    print("Estimated journey cost: Rs. {:.2f}".format(best_cost))
