#Anteriormente, definimos la función square() que toma un parámetro (num), lo ajusta al cuadrado y luego lo devuelve
def square(num):
    x = num ** 2
    return x
#Ahora podemos reescribir esta función como una función lambda (sin nombre):
lambda num: num ** 2
lambda num1, num2: num1+num2

#Una lambda podría ser:
#un elemento en una lista:
#crea una nueva lista, como lambda como elemento
my_list = ['test_string', 99, lambda x : x ** 2]
#accede al valor de la lista
print(my_list[2]) # imprime el objeto en memoria
# invoca la función lambda, pasando un 5 como arugmento
print(my_list[2](5))

#pasó a otra función como devolución de llamada:
# defina una función que tome una entrada que sea una función
def invoker(callback):
    # invoque el input pasando 2 como argumento
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

#almacenado en una variable:
add10 = lambda x: x + 10 # almacene la expresión lambda en una variable
print(add10(2))  # retorna 12
print(add10(98)) # retorna 108

#devuelto por otra función:
def incrementor(num):
    start = num
    return lambda x: num + x

print(incrementor(10))