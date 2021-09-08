task = 0
amount = 0
suma = 0
rav_max = 0
rav_min = 0
even = 0
odd = 0
while True:
    enter = int(input('Введите пожалуйста целое число: '))
    suma = suma + enter
    if enter == task:
        break
    else:
        amount = amount + 1     # Подсчет введенных чисел
    if rav_max == 0:
        rav_max = enter
    if enter > rav_max:         # Поиск максимального значения
        rav_max = enter
    if rav_min == 0:
        rav_min = enter
    if enter < rav_min:         # Поиск минимального значения
        rav_min = enter
    if enter % 2 == 0:          # Подсчет четных и нечетных чисел
         even = even + 1
    else:
        odd = odd + 1

average = suma / (amount+1)      # Подсчет среднего арифметическое всех введённых чисел

print('Kоличество введённых чисел: ', amount)
print('Сумма введённых чисел: ', suma)
print('Cреднее арифметическое всех введённых чисел: ', average)
print('Максимальное и минимальное значение: ', rav_max, '\t', rav_min)
print('Kоличество чётных и не чётных значений: ', even, '\t', odd)