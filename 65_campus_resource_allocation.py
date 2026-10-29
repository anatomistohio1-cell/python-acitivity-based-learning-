available_chairs = 30
available_laptops = 8
available_microphones = 2

activities = [
    ("Coding Workshop", 20, 6, 1),
    ("Robotics Demo", 12, 4, 2),
    ("Design Talk", 10, 3, 1),
]

print("CAMPUS RESOURCE ALLOCATION")
print("Starting stock: {} chairs, {} laptops, {} microphones".format(
    available_chairs, available_laptops, available_microphones
))

for activity in activities:
    name, chairs_needed, laptops_needed, microphones_needed = activity
    chair_shortage = chairs_needed - available_chairs
    laptop_shortage = laptops_needed - available_laptops
    microphone_shortage = microphones_needed - available_microphones

    if (chair_shortage <= 0 and laptop_shortage <= 0
            and microphone_shortage <= 0):
        available_chairs = available_chairs - chairs_needed
        available_laptops = available_laptops - laptops_needed
        available_microphones = available_microphones - microphones_needed
        print("{}: allocated.".format(name))
    else:
        print("{}: not allocated.".format(name))
        if chair_shortage > 0:
            print("  Chair shortage: {}".format(chair_shortage))
        if laptop_shortage > 0:
            print("  Laptop shortage: {}".format(laptop_shortage))
        if microphone_shortage > 0:
            print("  Microphone shortage: {}".format(microphone_shortage))

print("\nRemaining resource counts: chairs={}, laptops={}, microphones={}".format(
    available_chairs, available_laptops, available_microphones
))
