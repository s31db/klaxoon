import os
import requests
from typing import Dict, Any

from requests import Response


class KlaxoonAPI:
    def __init__(self, api_token: str, base_url: str):
        self.api_token = api_token
        self.base_url = base_url

    @classmethod
    def from_config_file(
        cls,
        config_file: str = os.path.expanduser("~/.api_klaxoon/.token"),
        base_url: str = "https://api.klaxoon.com",
    ) -> "KlaxoonAPI":
        try:
            with open(config_file, "r") as f:
                api_token = f.read().strip()
            return cls(api_token, base_url)
        except FileNotFoundError:
            raise ValueError("Fichier de configuration du token introuvable")

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Dict[str, Any] = None,
        data: Dict[str, Any] = None,
        verify: bool = True,
    ) -> Response:
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(
            method, url, headers=headers, params=params, json=data, verify=verify
        )
        response.raise_for_status()
        return response
