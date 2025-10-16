list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 4, 5, 7]
norepeat = []

for i in range(len(list1)):
    count=0
    for j in range(len(list1)):
        if list1[i] == list1[j]:
            count += 1
    if count==1:
        norepeat.append(list1[i])
print(norepeat)


