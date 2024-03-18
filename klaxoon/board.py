from klaxoon.author import Author
from klaxoon.idea import Idea
from typing import Any, Dict, List
import logging


class Board:
    def __init__(
        self,
        id: str = None,
        href: str = None,
        type: str = None,
        title: str | None = None,
        description: str | None = None,
        accessCode: str | None = None,
        state: str | None = None,
        author: Author | None = None,
        createdAt: str | None = None,
        updatedAt: str | None = None,
        ideas: List[Idea] | None = None,
        **kwargs: Any,
    ):
        self.id = id
        self.href = href
        self.type = type
        self.title = title
        self.description = description
        self.accessCode = accessCode
        self.state = state
        self.author = Author(**author) if author else None
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.ideas = [Idea(**idea) for idea in ideas] if ideas else []
        if kwargs:
            logging.warning(f"Board unexpected arguments: {kwargs}")

    def __str__(self):
        return f"Board(id={self.id}, title={self.title})"
