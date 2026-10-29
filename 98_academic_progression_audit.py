students = [
    ("Asha", [70, 65, 80], 90, [True, True]),
    ("Ben", [55, 35, 68], 82, [True, True]),
    ("Chen", [62, 70, 75], 74, [True, True]),
    ("Devi", [80, 72, 66], 88, [True, False]),
]
subject_names = ["Math", "Science", "English"]
pass_mark = 40
minimum_attendance = 75

print("UNIVERSITY ACADEMIC PROGRESSION AUDIT")

for student in students:
    name, marks, attendance, prerequisites = student
    issues = []

    for subject_index in range(len(marks)):
        if marks[subject_index] < pass_mark:
            issues.append("{} below pass mark".format(
                subject_names[subject_index]
            ))

    if attendance < minimum_attendance:
        issues.append("attendance below {}%".format(minimum_attendance))

    for prerequisite in prerequisites:
        if not prerequisite:
            issues.append("an outstanding prerequisite")
            break

    if len(issues) == 0:
        print("{}: ELIGIBLE to progress.".format(name))
    else:
        print("{}: NOT ELIGIBLE to progress.".format(name))
        for issue in issues:
            print("  - {}".format(issue))
