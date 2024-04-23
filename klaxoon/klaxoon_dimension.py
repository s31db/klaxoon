from requests import Response
from klaxoon.dimension import Dimension
from klaxoon.klaxoon_api import KlaxoonAPI

from typing import Iterator


class KlaxoonDimension(KlaxoonAPI):

    def get_board_dimensions(self, board_id: str) -> Iterator[Dimension]:
        """https://developers.klaxoon.com/reference/v1boarddimensiongetcollection"""
        for dimension in self._request(
            "GET", f"v1/boards/{board_id}/dimensions"
        ).json()["items"]:
            yield Dimension(**dimension)

    def get_board_dimension(self, board_id: str, dimension_id: str) -> Dimension:
        """https://developers.klaxoon.com/reference/v1boarddimensionget"""
        return Dimension(
            **self._request(
                "GET", f"v1/boards/{board_id}/dimensions/{dimension_id}"
            ).json()
        )

    def add_board_dimension(self, board_id: str, label: str) -> Dimension:
        """https://developers.klaxoon.com/reference/v1boarddimensionpost"""
        data = {"label": label}
        return Dimension(
            **self._request(
                "POST", f"v1/boards/{board_id}/dimensions", data=data
            ).json()
        )

    def update_board_dimension(
        self, board_id: str, dimension_id: str, label: str
    ) -> Dimension:
        """https://developers.klaxoon.com/reference/v1boarddimensionpatch"""
        data = {"label": label}
        return Dimension(
            **self._request(
                "PATCH", f"v1/boards/{board_id}/dimensions/{dimension_id}", data=data
            ).json()
        )

    def delete_board_dimension(self, board_id: str, dimension_id: str) -> Response:
        """https://developers.klaxoon.com/reference/v1boarddimensiondelete"""
        return self._request(
            "DELETE", f"v1/boards/{board_id}/dimensions/{dimension_id}"
        )
