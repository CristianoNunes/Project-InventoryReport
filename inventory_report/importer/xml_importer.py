from inventory_report.importer.importer import Importer
from xml_to_dict import XMLtoDict


class XmlImporter(Importer):

    @classmethod
    def import_data(cls, filePath):
        if not filePath.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(filePath) as xmlFile:
            parser = XMLtoDict()
            jsonReader = xmlFile.read()
            container_tag = "record"
            products = parser.value_from_nest(container_tag, jsonReader)

        return products
