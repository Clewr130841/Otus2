var_input = input("Введите сколько дней осталось до ближайшего отпуска: ")

if len(var_input) > 0 and var_input.isdigit():
    days = int(var_input)
    weeks = days // 7
    weekends = weeks * 2
    remaining = days % 7
    
    if remaining == 6:
        weekends += 1
    
    print(weekends)
else:
    print("Введено некорректное число")