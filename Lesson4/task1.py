var_input = input("Введите число: ")

if var_input.isdigit():
    while len(var_input) != 1:
        res = 0
        for s in var_input:
            res += int(s)
        var_input = str(res)
        
    print(var_input)
else:
    print("Некорректный ввод")