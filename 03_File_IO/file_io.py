def read_it(path):
    with open(path, "r") as f:
        return f.readlines()

def write_it(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)

def run():
    try:
        content = read_it("raw_data.txt")
        
        # Using a standard loop for clear processing
        clean_lines = []
        for line in content:
            # Uppercase and strip to clean the data
            clean_lines.append(line.strip().upper() + "\n")
            
        write_it("final_report.txt", clean_lines)
        print("File processing complete.")
    except:
        print("Error: check if raw_data.txt exists.")

if __name__ == "__main__":
    run()