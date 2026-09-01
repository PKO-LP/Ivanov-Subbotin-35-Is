word = "Gold"
try:
    a = int(input("Введите Номер буквы: "))
    print(f"символ: {word[a]}")
except ValueError:
    print("Ошибка нет ничего")