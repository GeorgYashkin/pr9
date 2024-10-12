list=[]
print("Введите числа:")
while (True):
    a=input()
    if a=="end":
        break
    elif a.isalpha():
        print("Ошибка при вводе числа")
    else:
        list.append(float(a))
print("Нечетные элементы списка:")
for i in range(len(list)):
    if list[i]%2==1:
        print(list[i])
