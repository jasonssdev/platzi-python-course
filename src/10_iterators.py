numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aquí i es igual a:",i+1)

for i in range(3,10):
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")

x = 0
while x<5:
    if x ==3:
        break
    print(x) 
    x +=1

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i ==3:
        break
    print("Aquí i es igual a:",i)

# Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))

# Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print(num)

# Iterar en cadenas
#Creando la cadena
text = "Hola mundo"
#Creando el iterador
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)
