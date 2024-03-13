from requests import Response

from klaxoon.klaxoon_api import KlaxoonAPI

from typing import Dict, Any, List


class KlaxoonCategory(KlaxoonAPI):

    def get_board_categories(self, board_id: str) -> List[str]:
        """https://developers.klaxoon.com/reference/v1boardcategorygetcollection"""
        return self._request("GET", f"v1/boards/{board_id}/categories").json()

    def get_board_category(self, board_id: str, category_id: str) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardcategoryget"""
        return self._request(
            "GET", f"v1/boards/{board_id}/categories/{category_id}"
        ).json()

    def add_board_category(self, board_id: str, label: str) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardcategorypost"""
        data = {"label": label}
        return self._request(
            "POST", f"v1/boards/{board_id}/categories", data=data
        ).json()

    def update_board_category(
        self, board_id: str, category_id: str, label: str
    ) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardcategorypatch"""
        data = {"label": label}
        return self._request(
            "PATCH", f"v1/boards/{board_id}/categories/{category_id}", data=data
        ).json()

    def delete_board_category(self, board_id: str, category_id: str) -> Response:
        """https://developers.klaxoon.com/reference/v1boardcategorydelete"""
        return self._request("DELETE", f"v1/boards/{board_id}/categories/{category_id}")
