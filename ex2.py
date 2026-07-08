pets = {}
next_id = 1  # Начальный ID


n = int(input("Сколько питомцев добавить? "))

for _ in range(n):
    name = input("Кличка питомца: ")

    pets[next_id] = {
        name: {
            "Вид питомца": input("Введите вид питомца: "),
            "Возраст питомца": int(input("Введите возраст питомца: ")),
            "Имя владельца": input("Введите имя владельца: ")
        }
    }

    next_id += 1  # Увеличение ID

# Просмотр информации
while True:
    selected_input = input("Выберите ID питомца (q для выхода): ")

    if selected_input.lower() == "q":
        break


    selected_id = int(selected_input)

    # Проверка: есть ли такой ID?
    if selected_id not in pets:
        print("Такого ID нет")
        continue

    # Получаем данные
    pet_data = pets[selected_id]
    name = list(pet_data.keys())[0]
    data = pet_data[name]

    age = data["Возраст питомца"]
    if age % 10 == 1 and age != 11:
        per = "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age <= 14):
        per = "года"
    else:
        per = "лет"

    answer = (
        f"Это {data['Вид питомца']} по кличке '{name}'. "
        f"Возраст питомца: {age} {per}. "
        f"Имя владельца: {data['Имя владельца']}"
    )

    print(answer)