var_input = input("Введите число: ")
result = True
if not var_input or var_input == ".":
    result = False
elif var_input.count('.') == 1:
    before_decimal, after_decimal = var_input.split('.')
    if not (before_decimal.isdigit() or before_decimal == "") and (after_decimal.isdigit() or after_decimal == ""):
        result = False
elif not var_input.isdigit():
    result = False
    
print(result)
