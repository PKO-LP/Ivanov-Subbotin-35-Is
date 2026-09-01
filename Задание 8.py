try:
    file = open("Hello.txt", "r", encoding="utf-8")
    text = file.read()
    file.close()

    print(text)
except FileNotFoundError:
    print("ошибка не тот")