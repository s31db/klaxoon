import logging
from typing import Any


class Category:
    def __init__(
        self,
        id: str | None = None,
        href: str | None = None,  # href
        label: str | None = None,
        **kwargs: Any,
    ) -> None:
        self.id = id
        self.href = href
        self.label = label
        if kwargs:
            logging.warning(f"Category unexpected arguments: {kwargs}")
