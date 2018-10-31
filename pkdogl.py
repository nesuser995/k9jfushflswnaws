number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

if (number1 == 0 and number2 == 0): # проверка на глупость
    print ("Ошибка. Оба числа не могут иметь нуль!")
else:
    operator = int(input("Введите номер операции: "))
    if (operator == 1):
        print ("1. Сумма двух чисел: ", number1 + number2)

    if (operator == 2):
        if (number1 < number2): # чтобы не ушло значение в минус
            print ("2. Возведение в куб разности двух чисел: ", (number2 - number1) ** 3)
        else:
            print ("2. Возведение в куб разности двух чисел: ", (number1 - number2) ** 3)

    if (operator == 3):
        print ("3. Произведение двух чисел: ", number1 * number2)

    if (operator == 4): # не понятно, оба по отдельности возводить или сначала складывать
        print ("4. Возведение числа в степень: ")

    if (operator == 5):
        print ("5. Возведение в квадрат суммы двух чисел: ", (number1 + number2) ** 2)

    if (operator == 6):
        if (number1 < number2): # снова проверяем, чтобы в минус не ушёл
            print ("6. Возведение в квадрат разности двух чисел: ", (number2 - number1) ** 2)
        else:
            print ("6. Возведение в квадрат разности двух чисел: ", (number1 - number2) ** 2)

    if (operator == 7):
        print ("7. Возведение в квадрат произведения двух чисел: ", (number1 * number2) ** 2)

    if (operator == 8):
        if (number1 < number2):
            print ("8. Разность двух чисел: ", number2 - number1)
        else:
            print ("8. Разность двух чисел: ", number1 - number2)

    if (operator == 9):
        print ("9. Возведение в квадрат частного двух чисел: ", (number1 / number2) ** 2)

    if (operator == 10):
        print ("10. Возведение в куб суммы двух чисел: ", (number1 + number2) ** 3)

    if (operator == 11):
        print ("11. Возведение в куб частного двух чисел: ", (number1 / number2) ** 3)

    if (operator == 12):
        print ("12. Возведение в куб произведения двух чисел: ", (number1 * number2) ** 3)

    if (operator == 13):
        if (number2 == 0): # проверка что второе число не ноль
            print ("13. Ошибка! Второе число не может быть 0!")
        else:
            print ("13. Частное двух чисел: ", number1 / number2)

    # 14-й оператор - экспонент числа
