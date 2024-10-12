import random

def rand(ticket):
    randnum=[random.choice(row) for row in ticket]
    return randnum

ticket = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
for i in range(len(ticket)):
    print(ticket[i])
print("Выберите по одному числу из каждой строки")
s=0
l=[]
while True:
    a=input()
    try:
        if int(a) in ticket[s]:
            l.append(int(a))
            s+=1
        else:
            print("Введите число из списка ",s+1)
        if s==5:
            break
    except ValueError:
        print("Введите число из списка", s+1)
print("Ваши числа",l)
print("Рандомные числа", rand(ticket))
