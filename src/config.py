import yaml
from pathlib import Path

class Config:
    def __init__(self, path: str = "config/settings.yaml"):
        self.path = Path(path)
        self._data = self._load()

    def _load(self):
        with open(self.path, "r") as f:
            return yaml.safe_load(f)

    def get(self, *keys):
        data = self._data
        for key in keys:
            data = data[key]
        return data

config = Config()