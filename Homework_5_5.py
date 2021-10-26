src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src2=[]
for value in src:
    try:
        src2.index(value)
    except:
        src2.append(value)
src.clear()
print(src2)
for value in src2:
    src.append(value)
src2.clear()
print(src)
