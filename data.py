import json
import yaml
import pandas as pd
import matplotlib as plt


class DataLoader:
    def __init__(self, filename):
        self.filename = filename

    def data_loads(self):  # будет словарь
        with open(self.filename, 'r') as data:
            result = json.load(data)
        return result

    # def data_yaml(self):
    #     with open(self.filename, 'r') as data:
    #         result = yaml.safe_load(data)
    #     return result


class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_total_records(self, data):  # общее кол-во записей
        return len(self.data)

    def get_records_by_category(self, category):  # кол-во записей по категориям
        records = []
        for i in self.data:
            if i["category"] == category:
                records.append(i)
            return records

    def get_max_score(self):
        # поиск максимального балла
        max_score = max([i["score"] for i in self.data])
        return max_score

    def get_min_score(self):
        # поиск минимального балла
        min_score = min([i["score"] for i in self.data])
        return min_score

    def get_mean_score(self):
        # поиск среднего значения баллов
        mean_score = sum([i["score"] for i in self.data]) / len(self.data)
        return mean_score
