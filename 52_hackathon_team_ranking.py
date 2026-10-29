teams = [
    ("Team Nova", ["Asha", "Ben", "Chen"], 80, 90),
    ("Team Byte", ["Devi", "Eli"], 85, 85),
    ("Team Pixel", ["Fay"], 95, 95),
    ("Team Orbit", ["Gita", "Hari", "Ira", "Jay"], 90, 80),
]
valid_teams = []

for team in teams:
    name, members, round_one, round_two = team

    if len(members) < 2 or len(members) > 4:
        print("{} is invalid: team size must be 2 to 4.".format(name))
    else:
        total = round_one + round_two
        valid_teams.append((name, len(members), round_one, round_two, total))

for first_index in range(len(valid_teams)):
    for second_index in range(0, len(valid_teams) - first_index - 1):
        first = valid_teams[second_index]
        second = valid_teams[second_index + 1]
        first_ranks_lower = first[4] < second[4]
        total_is_tied = first[4] == second[4]
        second_round_ranks_lower = first[3] < second[3]
        rounds_are_tied = first[3] == second[3]
        name_ranks_lower = first[0] > second[0]

        if (first_ranks_lower
                or (total_is_tied and second_round_ranks_lower)
                or (total_is_tied and rounds_are_tied and name_ranks_lower)):
            valid_teams[second_index] = second
            valid_teams[second_index + 1] = first

print("\nHACKATHON TEAM RANKING")
print("{:<6} {:<14} {:>8} {:>9} {:>9} {:>8}".format(
    "Rank", "Team", "Members", "Round 1", "Round 2", "Total"
))

rank = 1
for result in valid_teams:
    name, member_count, round_one, round_two, total = result
    print("{:<6} {:<14} {:>8} {:>9} {:>9} {:>8}".format(
        rank, name, member_count, round_one, round_two, total
    ))
    rank = rank + 1
