import math
print("Введите два числа a и b:")
a=int(input())
b=int(input())
list=[]
if a<b:
    for i in range(a+1,b):
        if math.sqrt(abs(i))%1==0:
            list.append(abs(i))
if a>b:
    for i in range(b+1,a):
        if math.sqrt(abs(i))%1==0:
            list.append(abs(i))
print("Квадраты целых чисел расположенных между a и b:",list)
