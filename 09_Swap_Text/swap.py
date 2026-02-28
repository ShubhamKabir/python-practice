with open("tags.txt", "r") as f:
    data = f.read()

updated = data.replace("PC", "Gaming")

with open("tags.txt", "w") as f:
    f.write(updated)

print("Text swapped.")