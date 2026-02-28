import json

def run():
    f = open("users.json")
    data = json.load(f)
    f.close()
    
    # Check each user and print if they are active
    for user in data:
        if user["active"] == True:
            print(f"Active: {user['name']}")

if __name__ == "__main__":
    run()