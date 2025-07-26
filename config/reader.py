import json

from config.config import Config


def get_config() -> Config:
    with open('config/config.json', 'r') as f:
        config = Config.model_validate_json(f.read())
        return config
