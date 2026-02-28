import json

def run():
    f = open("users.json")
    data = json.load(f)
    f.close()
    
    # This is the clear, step-by-step way we learned
    for user in data:
        if user["active"]:
            print(f"Active: {user['name']}")

if __name__ == "__main__":
    run()