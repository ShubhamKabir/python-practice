def load_config():
    config = {}
    # Reading settings from the external configuration file
    with open("app.conf", "r") as f:
        for line in f:
            # Split by '=' to separate the setting name from the value
            key, value = line.strip().split("=")
            config[key] = value
    
    print(f"App Name: {config['name']}")
    print(f"Version: {config['version']}")
    print(f"Mode: {config['mode']}")

if __name__ == "__main__":
    load_config()