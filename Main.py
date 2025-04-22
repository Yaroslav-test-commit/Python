try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation =  input("Введите операцию (+, -, *, /): ")
    number = num1.is_integer() and num2.is_integer()

    if operation == "+":
        if number:
            print(f"Результат сложения: {int(num1 + num2)}")
        else: print(f"Результат сложения: {num1 + num2}")
    elif operation == "-":
        if number:
            print(f"Результат вычитания: {int(num1 - num2)}")
        else: print(f"Результат вычитания: {num1 - num2}")
    elif operation == "*":
        if number:
            print(f"Результат умножения: {int(num1 * num2)}")
        else: print(f"Результат умножения: {num1 * num2}")
    elif operation == "/":
        if (num1 / num2).is_integer:
            print(f"Результат деления: {int(num1 / num2)}")
        else: print(f"Результат деления: {num1 / num2}")
    else:
        print("Ошибка: неизвестная операция")

except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")