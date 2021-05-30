from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        companyName = [name["nome_da_empresa"] for name in products]
        companies = Counter(companyName)

        quantityProductCompany = ""
        for company in companies:
            quantityProducts = companyName.count(company)
            quantityProductCompany += f"- {company}: {quantityProducts}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{quantityProductCompany}"
        )
