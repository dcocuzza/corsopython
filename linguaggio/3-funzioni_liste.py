
def laptop_nuovo(ram, cpu, antivirus = False):
    print("Il laptop ha le seguenti caratteristiche:")
    print("RAM: ", ram)
    print("CPU ", cpu)
    if antivirus == True:
        print("Hai comprato anche l'antivirus!")

    print()

laptop_nuovo("16GB", "i7")
laptop_nuovo("32GB", "i9", True)

x = 15

def esempio():
    #x += 2 da errore, l'ulizzo è limitato al suo scope dobbiamo fare prima così:

    global x
    x += 2

    y = x
    y += x
 
    return x

print(esempio())

my_list = [9.81, "pasta", 22, 44, 3.14]
print(my_list)
new_list = ["asd", "poker", "luna", my_list]
print(new_list)
print(my_list[0])
print(my_list[-1])

primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print(primi[4:10]) #il primo elemento è incluso il secondo no
print(primi[:5]) #dall'elemento 0 all'elemento 4

match = 11

for i in primi:
    if i == match:
        output = str(i) + " == " + str(match)
        print("Mathc! " + output)
    else:
        print(i)


spesa = ["riso", "pollo", "verdura"]
print(spesa)
spesa.append("sapone")
print(spesa)

spesa_extra = ["camicia", "copri volante"]
spesa.extend(spesa_extra)
print(spesa)

spesa.sort()
print(spesa)

print(spesa.index("sapone"))

spesa[1] = "tacchino"
print(spesa)

del spesa[0]
print(spesa)

new_list = [True, None, 'poker', 4.2, 1945]
print(new_list.pop()) #ritorna l'ultimo elemento che lo estrae
print(new_list)

new_list.remove(None) #rimuove dal valore
print(new_list)
