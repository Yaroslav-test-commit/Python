total_sum = 0 # сумма всех четных чисел от 1 до 100
for i in range(1, 100):
    if i % 2 == 0:
        total_sum += i

total_sum_new = 0 # сумма всех четных чисел от 1 до 100 включительно
for i in range(1, 101):
    if i % 2 == 0:
        total_sum_new += i

squares = [n ** 2 for n in range(0, 10) if n % 2 != 0]

counter = 0
while (number := int(input("Введите число: ")) > 0):
    counter += 1

print(total_sum)
print(total_sum_new)
print(squares)
print(counter)
