try:
    number = int(input("Введите число от 1 до 5: "))
    if number == 5:
        print("Five")
    elif number == 4:
        print("Four")
    elif number == 3:
        print("Three")
    elif number == 2:
        print("Two")
    elif number == 1:
        print("One")
    else:
        print("Введено число не из заданного диапазона")
except ValueError:
    print("Введено не число")

