a = int(input()) # получаем целое число и сохраняем его в переменной a
first = a // 1000 # вычисляем первую чифру числа , разделив на 1000
second = a // 100 - (a // 1000 * 10) # вычесляем вторую цифру числа вычитая сначала первую цифру и затем умножая на 10 для получения десятков
third = (a % 100 - a % 10) / 10 # вычисляем третью цифру числа , вычитая сначала последнюю цифру и затем делая целочисленное деление на 10
last = a % 10 # вычисляем последнюю цифру числа остаток от деления на 10
if first + last == second - third:
    print("да")
else:
    print("нет")