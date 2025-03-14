import yaml

with open("config/database.yaml", "r") as f:
    config = yaml.safe_load(f)

db_config = config["database"]
