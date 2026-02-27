import os

def extract_domain(email):
    # .strip() cleans spaces, .lower() keeps it uniform
    return email.strip().lower().split('@')[-1]

domain_counts = {}

# Check if file exists
if os.path.exists("emails.txt"):
    with open("emails.txt", "r") as file:
        for line in file:
            if "@" in line:
                domain = extract_domain(line)
                # Quick logic: get current count or 0, then add 1
                domain_counts[domain] = domain_counts.get(domain, 0) + 1

    print("--- Domain Results ---")
    for domain, count in domain_counts.items():
        print(f"{domain}: {count}")
else:
    print("Error: Please put 'emails.txt' in this folder.")