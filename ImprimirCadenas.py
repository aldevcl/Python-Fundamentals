nombre = "Zen"
print("Mi nombre es", nombre)

nombre = "Zen"
print("Mi nombre es " + nombre)

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"mi nombre es {first_name} {last_name} y tengo {age} años")

first_name = "Zen"
last_name = "Coder"
age = 27
print("Mi nombre es {} {} y tengo {} años.".format(first_name, last_name, age))
# salida: Mi nombre es Zen Coder y tengo 27 años.
print("Mi nombre es {} {} y tengo {} años.".format(age, first_name, last_name))
# salida: Mi nombre es 27 Zen y soy Coder años.

hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3 
print(hw, py)
# salida: Hola mundo Me encanta Python 3
name = "Zen"
age = 27
print("Mi nombre es %s y soy %d" % (nombre, age))		# o con variables
# Salida: Mi nombre es Zen y tengo 27

x = "hola mundo"
print(x.title())
# Salida:
"Hello World"
