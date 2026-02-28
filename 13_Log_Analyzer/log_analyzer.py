total = 0
errors = 0
info = 0

with open("log.txt", "r") as f:
    for line in f:
        total += 1
        if "ERROR" in line.upper():
            errors += 1
        elif "INFO" in line.upper():
            info += 1

print(f"Total Lines: {total}")
print(f"Errors: {errors}")
print(f"Info: {info}")