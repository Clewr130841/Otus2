def is_valid_name(name):
    return name.isalpha() and name[0].isupper()

def is_valid_age(age):
    return age.isdigit() and 18 <= int(age) <= 60

def is_valid_id(user_id):
    return user_id and user_id.isdigit() and len(user_id) <= 8

def input_user_data(user_dict):
    while True:
        name = input("Введите имя (или оставьте пустым для завершения): ").strip()
        if not name:
            break
        surname = input("Введите фамилию: ").strip()
        age = input("Введите возраст: ").strip()
        user_id = input("Введите ID (8 знаков): ").strip()

        if not is_valid_name(name):
            print("Ошибка: имя должно состоять только из букв и начинаться с заглавной буквы.")
            continue
        
        if not is_valid_name(surname):
            print("Ошибка: фамилия должна состоять только из букв и начинаться с заглавной буквы.")
            continue
        
        if not is_valid_age(age):
            print("Ошибка: возраст должен быть числом от 18 до 60.")
            continue
        
        if not is_valid_id(user_id):
            print("Ошибка: ID должен быть целым числом длиной 8 знаков и уникальным.")
            continue

        user_id =user_id.zfill(8)

        if user_id in user_dict:
            print("Ошибка: пользователь с таким ID уже существует.")
            continue

        user_dict[user_id] = (name.capitalize(), surname.capitalize(), int(age))

    return user_dict

def print_user_table(user_dict):
    print(f"{'ID':<10}{'Имя':<15}{'Фамилия':<15}{'Возраст'}")
    print("="*50)
    for user_id, data in user_dict.items():
        print(f"{user_id:<10}{data[0]:<15}{data[1]:<15}{data[2]:<10}")

user_dict = {}
user_dict = input_user_data(user_dict)
print_user_table(user_dict)