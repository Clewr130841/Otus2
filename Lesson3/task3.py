var_input = input("Введите параметры шоколадки и кусок, который хотим отломить через запятую: ")

splitted = var_input.split(",")

if len(splitted) == 3 and splitted[0].isdigit() and splitted[1].isdigit() and splitted[2].isdigit():
    width = int(splitted[0])
    height = int(splitted[1])
    required = int(splitted[2])
    
    all = width * height
    result = True
    if all < required:
        result = False
    
    if required % width != 0 and required % height != 0:
        result = False
    
    print(result)
else:
    print("Некорректный ввод")