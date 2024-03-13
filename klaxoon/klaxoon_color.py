from requests import Response

from klaxoon.klaxoon_api import KlaxoonAPI

from typing import Dict, Any, List


class KlaxoonColor(KlaxoonAPI):

    def get_board_colors(self, board_id: str) -> List[str]:
        """https://developers.klaxoon.com/reference/v1boardcolorgetcollection"""
        return self._request("GET", f"v1/boards/{board_id}/colors").json()

    def get_board_color(self, board_id: str, color_id: str) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardcolorget"""
        return self._request("GET", f"v1/boards/{board_id}/colors/{color_id}").json()

    def add_board_color(
        self, board_id: str, label: str | None, value: str
    ) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardcolorpost"""
        data = {value: value}
        if label:
            data["label"] = label
        return self._request("POST", f"v1/boards/{board_id}/colors", data=data).json()

    def update_board_color(
        self,
        board_id: str,
        color_id: str,
        label: str | None = None,
        value: str | None = None,
    ) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boardcolorpatch"""
        data = {}
        if label:
            data["label"] = label
        if value:
            data["value"] = value
        return self._request(
            "PATCH", f"v1/boards/{board_id}/colors/{color_id}", data=data
        ).json()

    def delete_board_color(self, board_id: str, color_id: str) -> Response:
        """https://developers.klaxoon.com/reference/v1boardcolordelete"""
        return self._request("DELETE", f"v1/boards/{board_id}/colors/{color_id}")
