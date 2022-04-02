scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(len(scr) - 1):
    if scr[i] < scr[i + 1]:
        result.append(scr[i + 1])
print(result)


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print((result))
