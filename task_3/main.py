import json
file = open("main.json", 'r', encoding='utf-8')
fish = json.load(file)
file.close()
operations = 0
while True:
    # Создаем меню с командами
    print("Введите, что хотите совершить?")
    print("Вывести все записи /all")
    print("Вывести определенную запись /one")
    print("Добавить запись /add") #data.appent(item)  
    print("Удалить определенную запись /del") #data.remove(item)
    print("Выйти из программы /exit")
    work = input()
#------------------------------------------------------------------------------------------------------------------
    # Создаем условие для каждой команды
    if work == "/all": 
        # Получаем значения из словаря с помощью цикла
        for riba in fish:
            id = riba["id"]
            name = riba["name"]
            latin_name = riba["latin_name"]
            is_salt_water_fish = riba["is_salt_water_fish"]
            sub_type_count = riba["sub_type_count"]

            print(f"---------------------- Рыба {id} -----------------------------------")
            print(f" Название: {name}, Латинское название: {latin_name}") 
            if is_salt_water_fish == True:
                print("                 Живет в соленой воде")
            else:
                print("                 Живет в пресной воде")
            print(f" -------------------- {sub_type_count} видов ---------------------------------")
            print() # Пустая строка для разделения записей
            operations+=1
#------------------------------------------------------------------------------------------------------------------
    # Делаем цикл и выводим айди только той рыбы, чей айди был вписан
    elif work == "/one":
        aidi = int(input("Введите айди рыбы, которую хотите увидеть: "))
        for riba in fish:
            id = riba["id"]
            if id == aidi:
                name = riba["name"]
                latin_name = riba["latin_name"]
                is_salt_water_fish = riba["is_salt_water_fish"]
                sub_type_count = riba["sub_type_count"]

                print(f"---------------------- Рыба {id} -----------------------------------")
                print(f" Название: {name}, Латинское название: {latin_name}") 
                if is_salt_water_fish == True:
                    print("                 Живет в соленой воде")
                else:
                    print("                 Живет в пресной воде")
                print(f" -------------------- {sub_type_count} видов ---------------------------------")
                print() # Пустая строка для разделения записей
            else: print("Записи не существует")
        operations+=1
#------------------------------------------------------------------------------------------------------------------     
    # C помощью командыц append вводим и добавляем рыбу с уникальным айди
    elif work == "/add" :
        try:
            new_id = int(input("Введите айди рыбы, которую хотите добавить: "))
            new_name = input("Впишите название рыбы: ")
            new_latin = input("Впишите название рыбы на латинице: ")
            new_salt = input("Впишите любит ли рыба соленую воду True/False: ")
            new_species = int(input("Количество видов рыбы: "))
        except:
            print("Неправильный ввод")
            continue
        fish.append({
            "id": new_id,
            "name": new_name,
            "latin_name": new_latin,
            "is_salt_water_fish": new_salt,
            "sub_type_count": new_species,
    })     
        file = open("main.json", 'w', encoding='utf-8')
        json.dump(fish,file)
        print("Рыба добавлена")
        operations+=1
#------------------------------------------------------------------------------------------------------------------   
    # С помощью цикла и remove удаляем рыбу с вписанным айди
    elif work == "/del":
        try:
            del_id = int(input("Айди записи, которую надо удалить:"))
        except:
            print("Неправильный ввод")
            continue
        rem = False
        for riba in fish:
            if riba["id"] == del_id:
                fish.remove(riba)
                rem = True
                break
        if rem:
            file = open("main.json", 'w', encoding='utf-8')
            json.dump(fish,file)
            print("Рыба удалена ✔")
        else:
            print("Запись не найдена")
        operations+=1

    #------------------------------------------------------------------------------------------------------------------ 
    # Прерываем программу в случае вписывания exit и выводим кол-во операций
    elif work == "/exit":
        print("Выход из программы")
        print(f"Всего проделано {operations} операций")
        break




