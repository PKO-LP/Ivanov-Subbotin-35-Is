a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите число 3: "))
def treygolnik(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
    else:
        print("Треугольник не существует")
treygolnik(a, b, c)