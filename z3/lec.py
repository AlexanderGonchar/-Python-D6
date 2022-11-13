# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число '))

numbers = [0,1]
for i in range(2, n + 1):
    numbers.append(numbers[i - 1] + numbers [i - 2])

numbers1 = list(map(lambda j: j[1] * (-1)**j[0], enumerate(numbers[1:])))

numbers1.reverse()
print (numbers1 + numbers)
