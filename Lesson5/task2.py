def is_valid_date(date_str):
    # Разделяем строку по точке
    day, month, year = map(int, date_str.split('.'))

    # Проверяем, что год, месяц и день в пределах допустимых значений
    if not (1 <= month <= 12):
        return False  # Месяц должен быть от 1 до 12

    # Список количества дней в каждом месяце (для невисокосного года)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Функция для проверки високосного года
    def is_leap_year(year):
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

    # Если год високосный, в феврале 29 дней
    if is_leap_year(year):
        days_in_month[1] = 29

    # Проверяем, что день соответствует количеству дней в месяце
    if not (1 <= day <= days_in_month[month - 1]):
        return False

    return True

print(is_valid_date("29.02.2000"))
print(is_valid_date("29.02.2001"))
print(is_valid_date("31.04.1962"))
print(is_valid_date("01.01.2024"))