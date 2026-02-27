import json

def run():
    f = open("users.json")
    data = json.load(f)
    f.close()
    
    active = [u for u in data if u["active"]]
    for user in active:
        print(f"Active: {user['name']}")

if __name__ == "__main__":
    run()