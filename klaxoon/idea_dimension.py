import logging
from typing import Any


class IdeaDimension:
    def __init__(
        self,
        id: str | None = None,
        href: str | None = None,
        value: str | None = None,
        **kwargs: Any,
    ) -> None:
        self.id = id
        self.href = href
        self.value = value
        if kwargs:
            logging.warning(f"Dimension unexpected arguments: {kwargs}")

    def __str__(self):
        return f"Dimension(id={self.id}, value={self.value})"
