import logging
from typing import Any


class Author:
    def __init__(self, href: str | None = None, id: str | None = None, **kwargs: Any):
        self.href = href
        self.id = id
        if kwargs:
            logging.warning(f"Author unexpected arguments: {kwargs}")
