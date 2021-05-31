from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    @classmethod
    def import_data(cls, filePath):
        if not filePath.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(filePath) as jsonFile:
            products = json.load(jsonFile)

        return products
