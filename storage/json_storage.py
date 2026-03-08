from pathlib import Path

import json


class JsonStorage:
    def __init__(self, filename: str) -> None:
        self.path = Path(filename)
        self.path.parent.mkdir(parents=True, exist_ok=True)
    
    def save(self, data: list[dict]) -> None:
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)

    def load(self) -> list:
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
