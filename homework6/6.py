import random

def rand():
    colvo=random.randint(5,30)
    randnum=[random.randint(-100,100) for j in range(colvo)]
    return randnum


list=rand()
print("Список чисел: ", list)
maks=list.index(max(list))
mini=list.index(min(list))
list[maks],list[mini]=list[mini],list[maks]
print("Измененный список:",list)
