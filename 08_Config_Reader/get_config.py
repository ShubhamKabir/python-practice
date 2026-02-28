def load_config():
    config = {}
    with open("app.conf", "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            config[key] = value
    
    print(f"App Name: {config['name']}")
    print(f"Version: {config['version']}")
    print(f"Mode: {config['mode']}")

load_config()