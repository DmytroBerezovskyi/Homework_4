Number = int(input('Введите пожалуйста натуральное число N:  '))
exp = 2
i = 2
exp_1 = 2
amount = 0
while True:         # Если пользователь ввел не правильно натуральное число, запрос на ввод повторится
    pass
    if Number == 0 or Number < 0:
        Number = int(input('Введите пожалуйста натуральное число N:  '))
    else:
        break

while True:
    pass
    if Number == 1:
        exp_1 = 1
        print(Number,'\t','\t', amount, exp_1, '\t','\t', '2 **', amount, '=', exp_1)
        break
    if Number < exp:
        print(Number,'\t','\t', amount, exp_1, '\t','\t', '2 **', amount, '=', exp_1)
        break
    amount += 1     # Количество возведений в степень
    exp_1 = exp     # Сохранение предыдущего значение, меньшего заданного натурального числа
    exp = exp * i   # Возведение в степень




