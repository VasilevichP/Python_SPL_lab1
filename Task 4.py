str = 'Enjoy every moment'
dict = {}
for i in str:
    try:
        dict[i] += 1
    except KeyError:
        dict[i] = 1
print(dict)
