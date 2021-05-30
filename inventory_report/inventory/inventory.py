from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from xml_to_dict import XMLtoDict
import csv
import json


class Inventory:

    def __init__(self):
        print("Inventory Report criado")

    @classmethod
    def readCsvFile(cls, filePath):
        with open(filePath) as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=",")
            products = [row for row in csvReader]
        return products

    @classmethod
    def readJsonFile(cls, filePath):
        with open(filePath) as jsonFile:
            products = json.load(jsonFile)
        return products

    @classmethod
    def readXmlFile(cls, filePath):
        with open(filePath) as xmlFile:
            parser = XMLtoDict()
            jsonReader = xmlFile.read()
            container_tag = "record"
            products = parser.value_from_nest(container_tag, jsonReader)
        return products

    @classmethod
    def getProducts(cls, filePath):
        if filePath.endswith(".csv"):
            return cls.readCsvFile(filePath)
        elif filePath.endswith(".json"):
            return cls.readJsonFile(filePath)
        elif filePath.endswith(".xml"):
            return cls.readXmlFile(filePath)

    @classmethod
    def import_data(cls, filePath, report_type):
        products = cls.getProducts(filePath)
        if report_type == "simples":
            return SimpleReport.generate(products)
        elif report_type == "completo":
            return CompleteReport.generate(products)
