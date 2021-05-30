import time
class SimpleReport:
    def generate(products):
        currentTime = time.strftime("%Y-%m-%d")
        manufacturingDate = currentTime
        expiringDate = "2030-01-01"
        companies = {}
        for product in products:
            productManufacture = product['data_de_fabricacao']
            productExpire = product['data_de_validade']
            productName = product['nome_da_empresa']

            if productManufacture < manufacturingDate:
                manufacturingDate = productManufacture
            if productExpire > currentTime and productExpire < expiringDate:
                expiringDate = productExpire

            if (companies.get(productName) is None):
                companies[productName] = 1
            else:
                companies[productName] += 1
        
        largestStock = max(companies, key=companies.get)

        response = (f"Data de fabricação mais antiga: {manufacturingDate}\n"
                    f"Data de validade mais próxima: {expiringDate}\n"
                    "Empresa com maior quantidade de produtos estocados: "
                    f"{largestStock}\n")

        return response
            