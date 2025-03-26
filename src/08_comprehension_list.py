# List Comprehension
# [Expression - Iterable - Condition]

# Example 1 [Expression - Iterable]
squares = [x**2 for x in range (1,11)]
print("Squares:",squares)

celsius = [0 , 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(f'Temperature {fahrenheit}')

# Example with Comprehensions List
matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed Matriz", transposed)

# Example without Comprehensions List
transposed_2 = []

for i in range(len(matrix[0])):
    transposed_2.append([])

for row in matrix:
    for i in range(len(row)):
        transposed_2[i].append(row[i])
print("Transposed_2 Matriz", transposed_2)

# Example 2 [Expression - Iterable - Condition]
evens = [x for x in range(1,21) if x % 2 == 0]
print("evens numbers", evens)