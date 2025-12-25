import pytest
from app.store import InMemoryStore, KeyNotFoundError


def test_set_and_get_value():
    store = InMemoryStore()
    store.set_value("name", "Hosna")

    assert store.get_value("name") == "Hosna"


def test_get_nonexistent_key_raises_error():
    store = InMemoryStore()

    with pytest.raises(KeyNotFoundError):
        store.get_value("unknown")