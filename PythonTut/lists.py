luckyNumbers = [4, 8, 9, 2, 7]

friends = ["Alva", "Beto", "Karla", "Ana", "Oscar", "Juan"]


print(friends[2:4]) #Agarra del rango dato 2 al 4

print(friends[2:]) #Agarra del dato 2 en adelante

print(friends[:2]) #Agarra del dato 2 para atras

print(friends[2]) #Agarra el dato 2

friends.insert(1, "Francis") #Añade un dato en la pocision estipulada en este caso la numero 1

print(friends)

friends.append("Chris") #Añade un dato
print(friends)

friends.extend(luckyNumbers) #Añade una array entera

print(friends)

friends.remove("Beto") #Elimina un dato de la lista
print(friends)

friends.pop() #Destruye el ultimo dato
print(friends)

print(friends.index("Oscar")) #Da el numero del dato buscado

print(friends.count("Alva")) #Me dice cuantos alvas hay en mi lista

luckyNumbers.sort()
print(luckyNumbers)

luckyNumbers.reverse()
print(luckyNumbers)

friends2 = (friends.copy())#copia la lista

friends.clear() #Destruye la lista
print(friends)
