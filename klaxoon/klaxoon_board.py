from klaxoon.board import Board
from klaxoon.klaxoon_api import KlaxoonAPI

from typing import Dict, Any, List


class KlaxoonBoard(KlaxoonAPI):
    def get_boards(
        self,
        page: int = None,
        per_page: int = None,
        sort_by: List[str] = None,
        query: str = None,
    ) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardgetcollection"""
        endpoint = "v1/boards"
        params = {}
        if page:
            params["page"] = page
        if per_page:
            params["perPage"] = per_page
        if sort_by:
            params["sort"] = ",".join(sort_by)
        if query:
            params["q"] = query
        return self._request("GET", endpoint, params=params).json()

    def create_board(self, title: str, description: str = None) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardpost"""
        payload = {"title": title}
        if description:
            payload["description"] = description
        return self._request("POST", "v1/boards", data=payload).json()

    # def get_board(self, board_id: str) -> Dict[str, Any]:
    def get_board(self, board_id: str) -> Board:
        """https://developers.klaxoon.com/reference/v1boardget"""
        endpoint = f"v1/boards/{board_id}"
        # return self._request("GET", endpoint).json()
        return Board(self._request("GET", endpoint).json())

    def get_board_by_access_code(self, access_code: str) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardgetbyaccesscode"""
        endpoint = f"v1/boards/by-access-code/{access_code}"
        return self._request("GET", endpoint).json()
