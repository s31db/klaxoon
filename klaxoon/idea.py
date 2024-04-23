from klaxoon.author import Author
from klaxoon.idea_category import Idea_Category
from klaxoon.idea_color import Idea_Color
from klaxoon.idea_dimension import IdeaDimension
import logging
from typing import Any


class Position:
    def __init__(self, x: float | int | None, y: float | int | None, z: int | None):
        self.x = x
        self.y = y
        self.z = z


class Data_Idea:
    def __init__(
        self,
        content: str | None,
        format: str | None,
        color: Idea_Color | None,
        category: Idea_Category | None,
        dimensions: dict[str, IdeaDimension] | None,
        **kwargs: Any,
    ):
        self.content = content
        self.format = format
        self.color = Idea_Color(**color) if color else color
        self.category = Idea_Category(**category) if category else category
        self.dimensions = (
            {dimension["id"]: IdeaDimension(**dimension) for dimension in dimensions}
            if dimensions
            else dimensions
        )
        if kwargs:
            logging.warning(f"Data_Idea unexpected arguments: {kwargs}")


class Idea:
    def __init__(
        self,
        position: Position | None = None,
        id: str | None = None,
        type: str | None = None,
        createdAt: str | None = None,
        updatedAt: str | None = None,
        author: Author | None = None,
        isLocked: bool | None = None,
        data: Data_Idea | None = None,
        **kwargs: Any,
    ):
        self.position = Position(**position) if position else position
        self.id = id
        self.type = type
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.author = author
        self.isLocked = isLocked
        self.data = Data_Idea(**data) if data else data

    def __str__(self):
        return f"Idea(id={self.id}, content={self.data.content})"
