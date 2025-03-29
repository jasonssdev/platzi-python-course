from utils.path_utils import project_root
import json

file_path = project_root / 'data' / 'raw' / 'products.json'

# Read the JSON file
with open(file_path, mode='r', encoding='utf-8') as file:
    products = json.load(file)

# print content of the JSON file
for product in products:
    print(product)

new_product = {
    'name': 'Wire Charger',
    'price': 55,
    'quantity': 10,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-07'
}

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)
