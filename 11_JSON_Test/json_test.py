import json

f = open("data.json")
data = json.load(f)
f.close()

print("Project:", data["name"])
for task in data["tasks"]:
    print("-", task)