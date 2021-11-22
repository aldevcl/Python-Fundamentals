#for
for x in range(0, 10, 1):
    print(x)
for x in range(0, 10):	# incremento de +1 está implícito
    print(x)
for x in range(10):	# incremento de +1 e inicia en 0 está inplicito
    print(x)

for x in range(0, 10, 2):
    print(x)
# salida: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# salida: 5, 2

#Listas
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# salida: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# salida: abc, 123, xyz

#Diccionarios
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# salida: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# salida: Noelle, Python

#otra forma de iterar a través de claves o llaves
capitals = {"Chile": "Santiago", "Argentina": "Buenos Aires"}
for key in capitals.keys():
     print(key)
#iterar con valores
for val in capitals.values():
     print(val)
#iterar con ambos, llaves y valores
for key, val in capitals.items():
     print(key, " = ", val)

#WhileElse
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final de sentencia else")

#break
for val in "string":
    if val == "i":
        break
    print(val)
# salida: s, t, r

#Continue
for val in "string":
    if val == "i":
        continue
    print(val)
# salida: s, t, r, n, g
# Nota, no i en el output, pero el bucle continuo después de la i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# solo se ejecuta en una salida limpia del ciclo while (es decir, no un break)
   print("Final else statement")
# salida: 3, 2, 1
