prefix = "GU"

with open("usernames.txt", "w") as f:
    for day in range(1, 366):
        for year in range(2023, 2026):
            username = f"{prefix}{day:03}{year}"

            f.write(username + '\n')

print("done")