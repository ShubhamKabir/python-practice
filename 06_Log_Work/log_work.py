import datetime

def save_log(msg):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("work_log.txt", "a") as f:
        f.write(f"[{time}] {msg}\n")

save_log("Pushing program 06 to GitHub.")
print("Activity logged.")