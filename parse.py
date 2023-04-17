"""
URL = "https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/"
PARAMS = None
METHOD = "GET"
TEXT_FILE_PATH = "data.txt"
JSON_FILE_PATH = "data.json"
"""

from bs4 import BeautifulSoup
import json


class Parser:
    def __init__(self, source):
        self.source = source

    def parse(self):
        with open(self.source, 'r') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find('table', {'class': 'data with-hover'})
        rows = table.find_all('tr')

        data = []

        cells = rows[0].find_all('td', class_=['p0 a_m', 'p2 a_c a_m', 'p4 a_c a_m', 'p5 a_c a_m', 'p7 a_c a_m'])  # head of table
        data.append({
            "name": cells[0].text.strip(),
            "institute": cells[1].text.strip(),
            "form": cells[2].text.strip(),
            "cost": cells[3].text.strip(),
            "sum": cells[4].text.strip()
        })

        for row in rows[2:14]:
            name = row.find('p', {'class': 'first_child'})
            cells = row.find_all('td', class_=['p2 a_m a_c', 'p4 a_m a_c', 'p5 a_c a_m', 'p7 a_m a_c'])
            if len(cells) == 4:  # if all cells were found
                data.append({
                    "name": name.text.strip(),
                    "institute": cells[0].text.strip(),
                    "form": cells[1].text.strip(),
                    "cost": cells[2].text.strip(),
                    "sum": cells[3].text.strip()
                    })
            elif len(cells) == 3:  # if the cell "sum" wasn't found by default parameter
                cells3 = row.find('td', {'class': 'p7 a_c a_m'})
                data.append({
                    "name": name.text.strip(),
                    "institute": cells[0].text.strip(),
                    "form": cells[1].text.strip(),
                    "cost": cells[2].text.strip(),
                    "sum": cells3.text.strip()
                    })

        return data

    def save(self, file_path):
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(self.parse(), f, ensure_ascii=False)
