import logging
from typing import Any


class Idea_Color:
    def __init__(
        self,
        id: str | None = None,
        href: str | None = None,
        **kwargs: Any,
    ) -> None:
        self.id = id
        self.href = href
        if kwargs:
            logging.warning(f"Idea Color unexpected arguments: {kwargs}")

    def __str__(self):
        return f"Idea Color(id={self.id})"
