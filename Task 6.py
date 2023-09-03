C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
print("Сумма С_1:", sum((C_1)))
print("Сумма С_2:", sum((C_2)))
print(("Сумма больше в кортеже %s") % ("C_1" if sum(C_1) > sum(C_2) else "C_2"))
min = max = C_1[0]
min_num = max_num = 0
for i in range(len(C_1)):
    if C_1[i] > max:
        max = C_1[i]
        max_num = i
    if C_1[i] < min:
        min = C_1[i]
        min_num = i
print("Порядковый номер минимального элемента в первом кортеже: ", min_num)
print("Порядковый номер максимального элемента в первом кортеже:", max_num)
min = max = C_2[0]
min_num = max_num = 0
for i in range(len(C_2)):
    if C_2[i] > max:
        max = C_2[i]
        max_num = i
    if C_2[i] < min:
        min = C_2[i]
        min_num = i
print("Порядковый номер минимального элемента во втором кортеже: ", min_num + 1)
print("Порядковый номер максимального элемента во втором кортеже:", max_num + 1)
