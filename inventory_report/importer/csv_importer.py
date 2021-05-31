from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, filePath):
        if not filePath.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(filePath) as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=",")
            products = [row for row in csvReader]

        return products
