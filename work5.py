def IsPointInSquare(x, y):
    return abs(x) + abs(y) <=1

x = float(input("введите x: "))
y = float(input("введите y: "))

if IsPointInSquare(x, y):
    print("да")
else:
    print("нет")