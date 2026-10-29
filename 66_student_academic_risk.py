students = [
    ("Asha", 78, 90, 82),
    ("Ben", 65, 70, 72),
    ("Chen", 45, 80, 40),
    ("Devi", 50, 75, 50),
]

low_count = 0
medium_count = 0
high_count = 0

print("STUDENT ACADEMIC RISK REPORT")
print("-" * 58)

for student in students:
    name, marks, attendance, lab_score = student
    reasons = []

    if marks < 50:
        reasons.append("marks below 50")
    if attendance < 75:
        reasons.append("attendance below 75%")
    if lab_score < 50:
        reasons.append("lab score below 50")

    if len(reasons) >= 2:
        category = "High"
        high_count = high_count + 1
    elif len(reasons) == 1:
        category = "Medium"
        medium_count = medium_count + 1
    else:
        category = "Low"
        low_count = low_count + 1

    if len(reasons) == 0:
        reason_text = "No risk conditions"
    else:
        reason_text = ", ".join(reasons)

    print("{}: {} risk - {}".format(name, category, reason_text))

print("\nSummary: Low={}, Medium={}, High={}".format(
    low_count, medium_count, high_count
))
