import random

def rand():
    colvo=random.randint(5,10)
    randnum=[random.randint(-100,100) for j in range(colvo)]
    return randnum

list=rand()
l=[list[len(list)-1]]
print("Дан список:",list)
for i in range(len(list)-1):
    l.append(list[i])
print("Измененный список со сдвигом в право: ",l)
    
