import os

def clean_domain(email):
    # Get the part after @ and convert to lowercase
    after_at = email.strip().lower().split('@')[-1]
    
    # Split by space and take the first part
    domain = after_at.split()[0]
    return domain

def run():
    path = "emails.txt"
    counts = {}
    
    if os.path.exists(path):
        with open(path, "r") as f:
            for line in f:
                if "@" in line:
                    domain = clean_domain(line)
                    # Counting logic using a dictionary
                    if domain in counts:
                        counts[domain] += 1
                    else:
                        counts[domain] = 1
        
        # Print the final counts
        for name in counts:
            print(f"{name}: {counts[name]}")
    else:
        print("Error: emails.txt not found")

if __name__ == "__main__":
    run()