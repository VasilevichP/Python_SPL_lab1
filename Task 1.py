counter=0
num=2
while counter<1001:
    n=0
    for div in range (2,num):
        if num%div==0:
            n+=1
    if n==0:
        print(num)
        counter+=1
    num+=1
print("    Конец")
