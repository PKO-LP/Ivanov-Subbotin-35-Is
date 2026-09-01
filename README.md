Задание 1
```py
try:    
    a=int(input("Введите число: " ))
    print(a)
except ValueError:
    print("Ошибка нет числа в строке"
Задание 2
```py
try:
    a=int(input("Первое число: "))
    b=int(input("Второе число: "))
    print(a/b)
except ValueError:
    print("Ничего не выводит")
Задание 3
```py
animals = ["Кот", "Медведь", "Пантера", "Енот"]

print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])
Задание 4
```py
try:
    a=int(input("Число: "))
    print(a ** 2)
except ValueError:
    print("Ошибка")
Задание 5
```py
food = {"Коля": "Шаурма", "Владимир": "Щи", "Рома": "Картопля", "Глеб": "Бургер"}

print(food["Коля"])
print(food["Рома"])
print(food["Владимир"])
print(food["Глеб"])
Задание 6
```py
try:
    a=int(input("Первое число: "))
    b=int(input("Второе число: "))
    print(a+b)
except ValueError:
    print("Ошибка")
Задание 7
```py
word = "Gold"
try:
    a = int(input("Введите Номер буквы: "))
    print(f"символ: {word[a]}")
except ValueError:
    print("Ошибка нет ничего")
Задание 8
```py
try:
    file = open("Hello.txt", "r", encoding="utf-8")
    text = file.read()
    file.close()

    print(text)
except FileNotFoundError:
    print("ошибка не тот")
Задание 9
```py
asdf = input("Введите пароль: ")
if asdf [3:4] != "":
    print("Пароль Принят")
else:
    print("Пароль неподходит")
