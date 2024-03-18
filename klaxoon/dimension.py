import logging
from typing import Any


class Dimension:
    def __init__(
        self,
        href: str | None = None,
        id: str | None = None,
        label: str | None = None,
        value: str | None = None,
        **kwargs: Any,
    ) -> None:
        self.href = href
        self.id = id
        self.label = label
        value = value
        if kwargs:
            logging.warning(f"Dimension unexpected arguments: {kwargs}")
