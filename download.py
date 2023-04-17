"""
URL = "https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/"
PARAMS = None
METHOD = "GET"
TEXT_FILE_PATH = "data.txt"
JSON_FILE_PATH = "data.json"
"""

import requests
from bs4 import BeautifulSoup


class Downloader:
    def __init__(self, url, params=None, method='get'):
        self.url = url
        self.params = params
        self.method = method.lower()

    def get_html(self):
        if self.method == 'get':
            response = requests.get(self.url, params=self.params)
        elif self.method == 'post':
            response = requests.post(self.url, data=self.params)
        else:
            raise ValueError(f"Неподдерживаемый метод: {self.method}")

        response.raise_for_status()

        return BeautifulSoup(response.text, 'html.parser').prettify()  # return html

    def save(self, file_path):
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(self.get_html())
