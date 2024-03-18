from requests import Response
from klaxoon.color import Color
from klaxoon.klaxoon_api import KlaxoonAPI


class KlaxoonColor(KlaxoonAPI):

    def get_board_colors(self, board_id: str) -> Color:
        """https://developers.klaxoon.com/reference/v1boardcolorgetcollection"""
        for color in self._request("GET", f"v1/boards/{board_id}/colors").json()[
            "items"
        ]:
            yield Color(**color)

    def get_board_color(self, board_id: str, color_id: str) -> Color:
        """https://developers.klaxoon.com/reference/v1boardcolorget"""
        return Color(
            **self._request("GET", f"v1/boards/{board_id}/colors/{color_id}").json()
        )

    def add_board_color(self, board_id: str, label: str | None, value: str) -> Color:
        """https://developers.klaxoon.com/reference/v1boardcolorpost"""
        data = {value: value}
        if label:
            data["label"] = label
        return Color(
            **self._request("POST", f"v1/boards/{board_id}/colors", data=data).json()
        )

    def update_board_color(
        self,
        board_id: str,
        color_id: str,
        label: str | None = None,
        value: str | None = None,
    ) -> Color:
        """https://developers.klaxoon.com/reference/v1boardcolorpatch"""
        data = {}
        if label:
            data["label"] = label
        if value:
            data["value"] = value
        return Color(
            **self._request(
                "PATCH", f"v1/boards/{board_id}/colors/{color_id}", data=data
            ).json()
        )

    def delete_board_color(self, board_id: str, color_id: str) -> Response:
        """https://developers.klaxoon.com/reference/v1boardcolordelete"""
        return self._request("DELETE", f"v1/boards/{board_id}/colors/{color_id}")
