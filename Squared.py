number = int(input('Введите пожалуйста целое число N: '))
sqr = 1
val = 1
n = 2                       # квадрат
while True:                 # Если пользователь ввел не правильно натуральное число, запрос на ввод повторится
    if number <= 0:
        number = int(input('Введите пожалуйста целое число N: '))
    else:
        break
print(number, end='\t''\t')
while number >= sqr:        # Поиск квадратов натуральных чисел, не превосходящие N (number)
    print(sqr, end=' ')
    val += 1
    sqr = val ** n





