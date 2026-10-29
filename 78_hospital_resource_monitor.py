wards = [
    ["General", 18, 20, 8, 7, 3, 3],
    ["Children", 12, 16, 5, 5, 4, 3],
    ["Surgery", 10, 12, 7, 5, 5, 3],
]

priority_wards = []

print("HOSPITAL WARD RESOURCE REPORT")
for ward in wards:
    name = ward[0]
    occupied_beds = ward[1]
    bed_capacity = ward[2]
    staff_needed = ward[3]
    staff_available = ward[4]
    equipment_needed = ward[5]
    equipment_available = ward[6]

    utilization = occupied_beds / bed_capacity * 100
    staff_shortage = staff_needed - staff_available
    equipment_shortage = equipment_needed - equipment_available
    shortage_count = 0

    if staff_shortage > 0:
        shortage_count = shortage_count + 1
    if equipment_shortage > 0:
        shortage_count = shortage_count + 1

    print("\n{}: bed utilization is {:.1f}%".format(name, utilization))
    if staff_shortage > 0:
        print("  Staff shortage: {}".format(staff_shortage))
    if equipment_shortage > 0:
        print("  Equipment shortage: {}".format(equipment_shortage))
    if shortage_count == 0:
        print("  All listed resources are available.")
    else:
        priority_wards.append((name, shortage_count))

for first_index in range(len(priority_wards)):
    for second_index in range(0, len(priority_wards) - first_index - 1):
        if priority_wards[second_index][1] < priority_wards[second_index + 1][1]:
            first = priority_wards[second_index]
            second = priority_wards[second_index + 1]
            priority_wards[second_index] = second
            priority_wards[second_index + 1] = first

print("\nWARDS NEEDING ATTENTION (most shortage types first)")
if len(priority_wards) == 0:
    print("No ward shortages.")
else:
    for ward_priority in priority_wards:
        name, shortage_count = ward_priority
        print("{}: {} shortage type(s)".format(name, shortage_count))
