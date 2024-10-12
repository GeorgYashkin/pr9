import random

def rand():
    colvo=random.randint(5,30)
    randnum=[random.randint(-100,100) for j in range(colvo)]
    return randnum


list=rand()
print("Список чисел: ", list)
print("Элементы списка, которые больше прыддущего элемента: ")
for i in range(1,len(list)):
    if list[i]>list[i-1]:
        print(list[i])
