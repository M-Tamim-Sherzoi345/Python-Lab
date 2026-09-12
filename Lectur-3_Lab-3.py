import json
import os

file_name = "config.json"

# If file does not exist, create default config
if not os.path.exists(file_name):
    config = {
        "app_name": "My App",
        "version": "1.0",
        "settings": {
            "language": "English",
            "theme": "light"
        }
    }

    with open(file_name, "w") as file:
        json.dump(config, file, indent=4)


# Load configuration
with open(file_name, "r") as file:
    config = json.load(file)

print("App:", config["app_name"])
print("Version:", config["version"])
print("Language:", config["settings"]["language"])


# Modify a setting
config["settings"]["theme"] = "dark"


# Save updated configuration
with open(file_name, "w") as file:
    json.dump(config, file, indent=4)

print("Configuration updated!")