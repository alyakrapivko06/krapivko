m = int(input()) # получаем число и сохраняем в m
m1 = m // 1000 # цифра в позиции тысяч
m2 = (m // 100 ) % 10 # цифра в позиции сотен
m3 = (m // 10) % 10 # цифра в позиции десятков
m4 = m % 10 # цифра в позиции единиц
print("цифра в позиции тысяч равна " , m1) # выводим результат согласно условиям
print("цифра в позиции сотен равна ", m2)
print("цифра в позиции десятков равна ", m3)
print("цифра в позиции единиц равна " , m4)