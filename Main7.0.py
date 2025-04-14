try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
finally:
    print("Завершение работы программы")