a = int(input()) #  получаем три целых числа и сохраняем их в перемменых a , b , c
b = int(input())
c = int(input())
d = 0 #  инициализируем переменную d  с значением 0
if a > 0: # проверяем если a ,больше 0 то добавляем его к  сумме d
    d = d + a
if b > 0: # проверяем если b  больше 0 то добавляем его в сумме d
    d = d + b
if c > 0: # проверяем если c больше 0 то добавляем его к сумме d
    d = d + c
print(d) # выводим сумму положительных чисел (d)