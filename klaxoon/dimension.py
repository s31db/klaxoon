import logging
from typing import Any


class Dimension:
    def __init__(
        self,
        id: str | None = None,
        label: str | None = None,
        **kwargs: Any,
    ) -> None:
        self.id = id
        self.label = label
        if kwargs:
            logging.warning(f"Dimension unexpected arguments: {kwargs}")

    def __str__(self):
        return f"Dimension(id={self.id}, label={self.label})"
