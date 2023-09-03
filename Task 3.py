numbers = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)
min = numbers[0]
odd = 2
for i in range(n):
    if numbers[i] % 2:
        if odd % 2 == 0 or numbers[i] > odd:
            odd = numbers[i]
    if abs(numbers[i]) < abs(min):
        min = numbers[i]
if odd % 2==0:
    print("Нет нечетных чисел")
else:
    print("Наибольшее нечетное число: ", odd)
print("Минимальное по модулю число: ", min)
