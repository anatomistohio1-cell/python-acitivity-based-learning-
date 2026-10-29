registration_ids = [
    "26-CSE-0042",
    "25-ECE-1107",
    "26-ABC-0042",
    "26-CSE-042",
    "26-CSE-0042",
    "2A-IT-0099",
    "24-ME-1000",
]
valid_branches = ["CSE", "ECE", "IT", "ME"]
seen_ids = []

print("STUDENT REGISTRATION VALIDATION")

for registration_id in registration_ids:
    parts = registration_id.split("-")
    errors = []

    if len(parts) != 3:
        errors.append("expected three fields separated by hyphens")
    else:
        year = parts[0]
        branch = parts[1]
        serial = parts[2]

        if len(year) != 2 or not year.isdigit():
            errors.append("year must contain two digits")
        if branch not in valid_branches:
            errors.append("branch code is not recognized")
        if len(serial) != 4 or not serial.isdigit():
            errors.append("serial number must contain four digits")

    if len(errors) == 0 and registration_id in seen_ids:
        errors.append("duplicate registration identifier")

    if len(errors) == 0:
        seen_ids.append(registration_id)
        print("{}: VALID (year {}, branch {}, serial {})".format(
            registration_id, year, branch, serial
        ))
    else:
        print("{}: INVALID".format(registration_id))
        for error in errors:
            print("  - {}".format(error))
