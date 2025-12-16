from typing import Dict, Any

class KeyNotFoundError(Exception):
    pass

class InMemoryStore():
    def __init__(self) -> None:
        self._store: Dict[str, Any] = {}
        
    def set_value(self, key: str, value: Any):
        self._store[key] = value
        

    def get_value(self, key: str) -> Any:
        if key not in self._store:
            raise KeyNotFoundError(f"key {key} is not found!")
        
        return self._store[key]
