from requests import Response

from klaxoon.klaxoon_api import KlaxoonAPI

from typing import Dict, Any, List


class KlaxoonDimension(KlaxoonAPI):

    def get_board_dimensions(self) -> List[str]:
        """https://developers.klaxoon.com/reference/v1boarddimensiongetcollection"""
        return self._request("GET", "v1/boards/dimensions").json()

    def get_board_dimension(self, board_id: str, dimension_id: str) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boarddimensionget"""
        return self._request(
            "GET", f"v1/boards/{board_id}/dimensions/{dimension_id}"
        ).json()

    def add_board_dimension(self, board_id: str, label: str) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boarddimensionpost"""
        data = {"label": label}
        return self._request("POS", f"v1/boards/{board_id}/dimension", data=data).json()

    def update_board_dimension(
        self, board_id: str, dimension_id: str, label: str
    ) -> Dict[str, Any]:
        """https://developers.klaxoon.com/reference/v1boarddimensionpatch"""
        data = {"label": label}
        return self._request(
            "PATCH", f"v1/boards/{board_id}/dimensions/{dimension_id}", data=data
        ).json()

    def delete_board_dimension(self, board_id: str, dimension_id: str) -> Response:
        """https://developers.klaxoon.com/reference/v1boarddimensiondelete"""
        return self._request(
            "DELETE", f"v1/boards/{board_id}/dimensions/{dimension_id}"
        )
