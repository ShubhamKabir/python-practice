import datetime

def save_log(msg):
    # Get current time and format it professionally
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Use "a" to append so we don't delete previous work logs
    with open("work_log.txt", "a") as f:
        f.write(f"[{time}] {msg}\n")

if __name__ == "__main__":
    save_log("Pushing program 06 to GitHub.")
    print("Activity logged.")