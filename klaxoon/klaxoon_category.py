from requests import Response
from klaxoon.category import Category
from klaxoon.klaxoon_api import KlaxoonAPI

from typing import Iterator


class KlaxoonCategory(KlaxoonAPI):

    def get_board_categories(self, board_id: str) -> Iterator[Category]:
        """https://developers.klaxoon.com/reference/v1boardcategorygetcollection"""
        for category in self._request("GET", f"v1/boards/{board_id}/categories").json()[
            "items"
        ]:
            yield Category(**category)

    def get_board_category(self, board_id: str, category_id: str) -> Category:
        """https://developers.klaxoon.com/reference/v1boardcategoryget"""
        return Category(
            **self._request(
                "GET", f"v1/boards/{board_id}/categories/{category_id}"
            ).json()
        )

    def add_board_category(self, board_id: str, label: str) -> Category:
        """https://developers.klaxoon.com/reference/v1boardcategorypost"""
        data = {"label": label}
        return Category(
            **self._request(
                "POST", f"v1/boards/{board_id}/categories", data=data
            ).json()
        )

    def update_board_category(
        self, board_id: str, category_id: str, label: str
    ) -> Category:
        """https://developers.klaxoon.com/reference/v1boardcategorypatch"""
        data = {"label": label}
        return Category(
            **self._request(
                "PATCH", f"v1/boards/{board_id}/categories/{category_id}", data=data
            ).json()
        )

    def delete_board_category(self, board_id: str, category_id: str) -> Response:
        """https://developers.klaxoon.com/reference/v1boardcategorydelete"""
        return self._request("DELETE", f"v1/boards/{board_id}/categories/{category_id}")
