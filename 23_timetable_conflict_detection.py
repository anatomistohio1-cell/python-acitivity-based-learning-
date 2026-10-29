courses = [
    ("Math", "Monday", 2, 4, "R1"),
    ("Physics", "Monday", 3, 5, "R2"),
    ("English", "Tuesday", 1, 3, "R3"),
    ("History", "Monday", 5, 6, "R1"),
]
unavailable_rooms = ["R3"]
problem_count = 0

print("TIMETABLE VALIDATION")
print("-" * 25)

for course in courses:
    name, day, start, end, room = course
    if room in unavailable_rooms:
        print("Unavailable room: {} uses {} on {}".format(name, room, day))
        problem_count = problem_count + 1

for first_index in range(len(courses)):
    first = courses[first_index]
    first_name, first_day, first_start, first_end, first_room = first

    for second_index in range(first_index + 1, len(courses)):
        second = courses[second_index]
        second_name, second_day, second_start, second_end, second_room = second

        same_day = first_day == second_day
        periods_overlap = first_start < second_end and second_start < first_end

        if same_day and periods_overlap:
            print("Time conflict: {} and {} on {}".format(
                first_name, second_name, first_day
            ))
            problem_count = problem_count + 1

if problem_count == 0:
    print("The proposed timetable is valid.")
else:
    print("Total problems found: {}".format(problem_count))
