while True:
    answer = input("pick a number from 1 to 10\n")
    answer1 = int(answer)

    if answer1 > 10:
        print("Додик только до 10")
    elif answer1 == 7:
        print("умрешь через 1 день")
        break
    elif answer1 == 6:
        while True:
            print("sex")
            should_stop = input("Остановиться?\n")
            if should_stop.lower() == "да":
                break
        break  # чтобы выйти из внешнего цикла после 6
    else:
        print("все гуд")
        break  # всё хорошо — выходим
def greeting(name: str, name2: str):
    print(f"Hello {name}, Hello second dolbaeb {name2}")
    return "чемп хардкора " + name2

# Вызов
result = greeting("Илья", "Саня")
print(result)


def counte(string):
    WORDS = "sydymanSYDYMAN"
    count = 0
    for char in string:
        if char in WORDS:
            count += 1
    return count

print(counte("sydyman batya"))




