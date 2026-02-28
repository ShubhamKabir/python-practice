total = 0

# Opening the CSV file to calculate purchase costs
try:
    with open("items.csv", "r") as f:
        for line in f:
            # Splitting by comma to separate name and price
            name, val = line.strip().split(',')
            total += int(val)
            print(f"{name}: {val}")

    print(f"Total: {total}")
except FileNotFoundError:
    print("Error: items.csv not found.")