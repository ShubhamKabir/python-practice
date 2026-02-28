import os

def check():
    # Read the list of required files
    with open("list.txt", "r") as f:
        content = f.readlines()
    
    # Using a standard loop for clear verification logic
    for line in content:
        filename = line.strip()
        
        # Professional "if/else" check for file existence
        if os.path.exists(filename):
            res = "OK"
        else:
            res = "MISSING"
            
        print(f"{filename}: {res}")

if __name__ == "__main__":
    check()