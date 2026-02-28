with open("list.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        
        # Skip empty lines
        if clean_line:
            print(clean_line)