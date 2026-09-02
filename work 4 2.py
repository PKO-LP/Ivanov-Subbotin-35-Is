def tocka(x, y):
    return abs(x) <=1 and abs(y) <=1
x=float(input("Введите число x: "))
y=float(input("Введите число y: "))
if tocka(x, y):
    print("Точка входит в область")
else:
    print("Точка не входит в область")