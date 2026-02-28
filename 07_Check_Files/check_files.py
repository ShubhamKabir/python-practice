import os

def check():
    with open("list.txt", "r") as f:
        files = [l.strip() for l in f]
    
    for file in files:
        res = "OK" if os.path.exists(file) else "MISSING"
        print(f"{file}: {res}")

check()