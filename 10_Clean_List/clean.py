with open("list.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        if clean_line:
            print(clean_line)