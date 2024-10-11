var_input = input("Введите пятизначное число: ")

if len(var_input) == 5 and var_input.isdigit():
    result = var_input[0] + var_input[3:0:-1] + var_input[4]
    print(result)
else:
    print("Введено некорректное число")