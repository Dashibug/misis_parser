from download import Downloader
from parse import Parser
from data import DataAnalyzer, DataLoader

def process(url, web_page_path = None, data_path = None):
    downloader = Downloader(url=url)
    downloader.save(web_page_path)
    parser = Parser(web_page_path)
    data = parser.parse()
    data1 = DataAnalyzer(data)
    return data1.get_total_records(data)

URL = "https://misis.ru/applicants/admission/baccalaureate-and-specialty/faculties/"
TEXT_FILE_PATH = "data.html"
JSON_FILE_PATH = "data.json"
print(process(URL,TEXT_FILE_PATH, JSON_FILE_PATH))


