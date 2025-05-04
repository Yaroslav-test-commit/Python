total_sum = sum(i for i in range(1, 101) if i % 2 == 0)

squares = [n ** 2 for n in range(0, 10) if n % 2 != 0]

counter = 0
while (number := int(input("Введите число: ")) > 0):
    counter += 1

print(total_sum)
print(squares)
print(counter)
