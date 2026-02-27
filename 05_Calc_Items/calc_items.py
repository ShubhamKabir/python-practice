total = 0
with open("items.csv", "r") as f:
    for line in f:
        name, val = line.strip().split(',')
        total += int(val)
        print(f"{name}: {val}")

print(f"Total: {total}")