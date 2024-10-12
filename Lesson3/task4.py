var_input = input("Введите целое положительное число: ")

if len(var_input) > 0 and var_input.isdigit() and int(var_input) > 0:
    num = int(var_input)
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    roman_num = ''
    
    for i in range(len(val)):
        count = num // val[i]
        roman_num += syms[i] * count
        num -= val[i] * count
    
    print(roman_num)
else:
    print("Некорректный ввод")
