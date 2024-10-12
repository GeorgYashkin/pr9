import re 

while True:
    pattern = r'([^@]+)@(.+)'
    a='0123456789'
    email=input()
    match=re.match(pattern,email)
    try:
        if email[0] in a:
            print("Ошибка, введите корректный email адресс")
        elif match:
            username = match.group(1)
            domain = match.group(2)
            if domain.count('.')==0:  
                print("Ошибка, введите корректный email адресс")
                continue 
            print("Имя пользователя: ", username)
            print("Доменное имя почты: ",domain)
            break
        else:
            print("Ошибка, введите корректный email адресс")
    except ValueError:
        print("Ошибка, введите корректный email адресс")
