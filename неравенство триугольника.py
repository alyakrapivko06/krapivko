a = int(input()) # получаем целые числа с сохраняем их в переменных a , b и c
b = int(input())
c = int(input())
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)): # проверяем выволняется ли нееравенство треугольника для заданыых сторон
    print("да")
else:
    print("нет")