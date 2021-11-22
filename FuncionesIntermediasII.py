#1.- Actualiza los valores en diccionarios y listas
print("**********   Actualiza los valores en diccionarios y listas  **********")
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
print("Ejercicio 1")
def listax(x):
    print(x)
    x[1][0]=15
    return x  
print(listax(x))

#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
print("Ejercicio 2")
def estudiante(x):
    print(x)
    students[0]['last_name']="Bryant"
    return x
print(estudiante(students))

#En el directorio sports_directory, cambia 'Messi' a 'Andres'
print("Ejercicio 3")
def deporte(x):
    for i in sports_directory:
        print (i, ":", x[i]) 
    x["soccer"][0]="Andres"
    for i in sports_directory:
        print (i, ":", x[i])
deporte(sports_directory)


#Cambia el valor 20 en z a 30
print("Ejercicio 4")
def lista(x):
    print(x)
    x[0]['y']=30
    return x
print(lista(z)) 

#2.-Itera a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. 
#Por ejemplo, dada la siguiente lista:
print("**********   Itera a través de una lista de diccionarios  **********")
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionaryotro(x):
    print("\n")
    for i in x:
        #print("first_name -", i["first_name"], "," ,"last_name -", i["last_name"]) 
        for j,b in i.items(): #recorro el diccionario
            print(j,b, " ", end="")
        print()    
iterateDictionaryotro(students)

#3.-Obtén valores de una lista de diccionarios
print("**********   Obtén valores de una lista de diccionarios  **********")
def iterateDictionary2(key_name,some_list):
    for i in some_list:
        print(i[key_name])
iterateDictionary2('first_name', students)

def iterateDictionary2(key_name,some_list):
    for j in some_list:
        print(j[key_name])
iterateDictionary2('last_name', students)

#4.-Itera a través de un diccionario con valores de listas
print("**********   Itera a través de un diccionario con valores de listas  **********")
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(len(some_dict['locations']),"LOCATIONS")
    for location in some_dict['locations']:
        print(location)
    print("\n")
    print(len(some_dict['instructors']),"INSTRUCTORS")
    for instructors in some_dict['instructors']:
        print(instructors)
printInfo(dojo)