from utils.path_utils import project_root
import csv

file_path = project_root / 'data' / 'raw' / 'products.csv'

# read file
# with open(file_path, mode='r', encoding='utf-8') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)

# with open(file_path, mode='r', encoding='utf-8') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(f"Product Name: {row['name']}, price: {row['price']}, quantity: {row['quantity']}")


# new_product = {
#     'name': 'Wireless Charger',
#     'price': 75,
#     'quantity': 100,
#     'brand': 'ChargerMaster',
#     'category': 'Accessories',
#     'entry_date': '2024-07-01'
# }

# with open('products.csv', mode='a', newline='') as file:
#     file.write('\n')
#     csv_writer = clcsv. DictWriter(file, fieldnames = new_product.keys())
#     csv_writer.writerow(new_product)

updated_file_path = project_root / 'data' / 'preprocessed' / 'products.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #Escribir los encabezados

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)