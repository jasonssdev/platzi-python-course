
from utils.path_utils import project_root

file_path = project_root / 'data' / 'raw' / 'handling_txt.txt'
print(file_path)

# read a txt file line by line
# with open('../data/raw/handling_txt.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# read a txt file line by line and store in a list
# with open(file_path, 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in (line.strip() for line in lines):
#         print(line)

# add a line to the end of the file
# with open(file_path, 'a', encoding='utf-8') as file:
#     file.write("\n \nBy: ChatGPT")

# overwrite the file
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write("\n \nBy: ChatGPT")