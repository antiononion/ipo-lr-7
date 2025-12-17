import json

def load_data():
    with open("main.json", 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(data):
    with open("main.json", 'w', encoding='utf-8') as file:
        json.dump(data, file)

def show_fish(riba):
    id = riba["id"]
    name = riba["name"]
    latin_name = riba["latin_name"]
    is_salt_water_fish = riba["is_salt_water_fish"]
    sub_type_count = riba["sub_type_count"]
    
    print(f"---------------------- Рыба {id} -----------------------------------")
    print(f" Название: {name}, Латинское название: {latin_name}") 
    print("                 Живет в соленой воде" if is_salt_water_fish else "                 Живет в пресной воде")
    print(f" -------------------- {sub_type_count} видов ---------------------------------\n")

def all_fish(data):
    for riba in data:
        show_fish(riba)

def one_fish(data):
    try:
        aidi = int(input("Введите айди рыбы, которую хотите увидеть: "))
        found = False
        for riba in data:
            if riba["id"] == aidi:
                show_fish(riba)
                found = True
                break
        if not found:
            print("Записи не существует")
    except:
        print("Неправильный ввод")

def add_fish(data):
    try:
        fish.append({
            "id": int(input("Введите айди рыбы, которую хотите добавить: ")),
            "name": input("Впишите название рыбы: "),
            "latin_name": input("Впишите название рыбы на латинице: "),
            "is_salt_water_fish": input("Впишите любит ли рыба соленую воду True/False: "),
            "sub_type_count": int(input("Количество видов рыбы: "))
        })
        save_data(data)
        print("Рыба добавлена")
    except:
        print("Неправильный ввод")

def del_fish(data):
    try:
        del_id = int(input("Айди записи, которую надо удалить: "))
        for riba in data:
            if riba["id"] == del_id:
                data.remove(riba)
                save_data(data)
                print("Рыба удалена ✔")
                return
        print("Запись не найдена")
    except:
        print("Неправильный ввод")

fish = load_data()
operations = 0
menu = {
    "/all": lambda: all_fish(fish),
    "/one": lambda: one_fish(fish),
    "/add": lambda: add_fish(fish),
    "/del": lambda: del_fish(fish)
}

while True:
    print("Введите, что хотите совершить?")
    print("Вывести все записи /all\nВывести определенную запись /one")
    print("Добавить запись /add\nУдалить определенную запись /del")
    print("Выйти из программы /exit")
    
    work = input()
    if work == "/exit":
        print("Выход из программы")
        print(f"Всего проделано {operations} операций")
        break
    elif work in menu:
        menu[work]()
        operations += 1



