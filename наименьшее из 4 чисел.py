a = int(input()) # разбить 4 числа a , b ,c , d на 2 пары : a , b, c ,d далее находим минимум в каждой паре а затем среди этих двух минимальных выбираем минимальное
b = int(input()) # получаем 4 целых числа и сохраняем их в переменных a , b , c , d
c = int(input())
d = int(input())
if a > b: # сравниваем a c b и присваиваем a значение b если b меньше a
    a = b
if c > d:  # сравниваем c и d и присваиваем c значение d , если d меньше c
    c = d
if a > c: # сравниваем a и c присваиваем a значение c  если c  меньше a
    a = c
print(a) # выводим наименьшее из четырех введенных чисел, которые теперь хранится в переменной a
