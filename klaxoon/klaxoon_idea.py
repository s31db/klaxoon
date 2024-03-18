from klaxoon.klaxoon_api import KlaxoonAPI
from klaxoon.idea import Idea

from typing import Dict, Any, List
from requests import Response


class KlaxoonIdea(KlaxoonAPI):
    def get_board_ideas(
        self,
        board_id: str,
        page: int = None,
        per_page: int = None,
        sort_by: List[str] = None,
        query: str = None,
        authors: List[str] = None,
        categories: List[str] = None,
        colors: List[str] = None,
    ) -> Idea:
        """https://developers.klaxoon.com/reference/v1boardideagetcollection"""
        endpoint = f"v1/boards/{board_id}/ideas"
        params = {}
        if page:
            params["page"] = page
        if per_page:
            params["perPage"] = per_page
        if sort_by:
            params["sort"] = ",".join(sort_by)
        if query:
            params["content"] = query
        if authors:
            params["authorId"] = ",".join(authors)
        if categories:
            params["categoryId"] = ",".join(categories)
        if colors:
            params["colorId"] = ",".join(colors)
        for idea in self._request("GET", endpoint, params=params).json()["items"]:
            yield Idea(**idea)

    def get_board_idea(self, board_id: str, idea_id: str) -> Idea:
        """https://developers.klaxoon.com/reference/v1boardideaget"""
        endpoint = f"v1/boards/{board_id}/ideas/{idea_id}"
        return Idea(**self._request("GET", endpoint).json())

    def add_idea_to_board(
        self,
        board_id: str,
        content: str,
        position: Dict[str, float | int] = None,
        category: str = None,
        color: str = None,
        dimension: str = None,
    ) -> Idea:
        """https://developers.klaxoon.com/reference/v1boardideapost
        Position is a dict with keys 'x' and 'y' and 'z'. 'x' and 'y' are float or int and 'z' is int.
        Position and all position values is optional.
        """
        endpoint = f"v1/boards/{board_id}/ideas"
        payload = {"data": {"content": content}}
        if position:
            payload["position"] = position
        if category:
            payload["data"]["category"] = category
        if color:
            payload["data"]["color"] = color
        if dimension:
            payload["data"]["dimension"] = dimension
        return Idea(**self._request("POST", endpoint, data=payload).json())

    def delete_idea_from_board(self, board_id: str, idea_id: str) -> Response:
        """https://developers.klaxoon.com/reference/v1boardideadelete"""
        endpoint = f"v1/boards/{board_id}/ideas/{idea_id}"
        return self._request("DELETE", endpoint)

    def update_idea(
        self,
        board_id: str,
        idea_id: str,
        position: Dict[str, float | int] = None,
        content: str = None,
        category: str = None,
        color: str = None,
        dimensions: List[str] = None,
    ) -> Idea:
        """https://developers.klaxoon.com/reference/v1boardideapatch"""
        payload = {"data": {}}
        if position:
            payload["position"] = position
        if content:
            payload["data"]["content"] = content
        if category:
            payload["data"]["category"] = {"id": category}
        if color:
            payload["data"]["color"] = {"id": color}
        if dimensions:
            payload["data"]["dimensions"] = [
                {"id": dimension} for dimension in dimensions
            ]
        return Idea(
            **self._request(
                "PATCH", f"v1/boards/{board_id}/ideas/{idea_id}", data=payload
            ).json()
        )
