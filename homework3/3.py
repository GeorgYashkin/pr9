list=[]
print("Введите числа:")
while True:
    a=input()
    if a=="end":
        break
    try:
        list.append(float(a))
    except ValueError:
        print("Ошибка при вводе числа")
print("Нечетные элементы списка:")
for i in range(len(list)):
    if list[i]%2==1:
        print(int(list[i]))
