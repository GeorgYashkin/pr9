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

ch=0
nch=0
for i in range(len(list)):
    if list[i]%2==0:
        ch+=1 
    elif list[i]%2==1:
        nch+=1 
print("Кол-во четных элементов в списке:",ch)
print("Кол-во нечетных элементов в списке:",nch)
