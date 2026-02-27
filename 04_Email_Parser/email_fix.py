import os

def clean_domain(email):
    # This logic fixes the 'yahoo.comhello' bug
    after_at = email.strip().lower().split('@')[-1]
    domain = after_at.split()[0].split(',')[0]
    return domain

def run():
    path = "emails.txt"
    if os.path.exists(path):
        with open(path, "r") as f:
            for line in f:
                if "@" in line:
                    print(clean_domain(line))
    else:
        print("Error: emails.txt not found")

if __name__ == "__main__":
    run()