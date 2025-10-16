num = [10,20,30,9,89]
sort1=[]
# to sort the given list in ascending order
for i in range(len(num)):
    for j in range(len(num)-1):
        if num[j]>num[j+1]:
            num[j+1],num[j]=num[j],num[j+1]
print(num)
#find the smallest element in the sorted list
for i in range(len(num)):
    if num[i]<num[i-1]:
        print(num[i])
