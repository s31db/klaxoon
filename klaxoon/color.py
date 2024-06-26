import logging
from typing import Any


class Color:
    def __init__(
        self,
        id: str | None = None,
        href: str | None = None,
        label: str | None = None,
        value: str | None = None,
        **kwargs: Any,
    ) -> None:
        self.id = id
        self.href = href
        self.label = label
        self.value = value
        if kwargs:
            logging.warning(f"Color unexpected arguments: {kwargs}")

    def __str__(self):
        return f"Color(id={self.id}, label={self.label}, value={self.value})"
