# Read the current tags from the file
with open("tags.txt", "r") as f:
    data = f.read()

# Swap 'PC' with 'Gaming' for better channel targeting
updated = data.replace("PC", "Gaming")

# Write the updated text back to the file
with open("tags.txt", "w") as f:
    f.write(updated)

print("Text swapped.")