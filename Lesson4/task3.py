var_input = input("Введите строку: ")

if len(var_input) == 0:
    print("Некорректный ввод")
else:
    counter = 0
    result = []
    prev = var_input[0]
    
    for s in var_input:
        if prev != s:
            result.append(f"{counter}{prev}")
            counter = 1
            prev = s
        else:
            counter+=1

    result.append(f"{counter}{prev}")
    
    print(''.join(result))