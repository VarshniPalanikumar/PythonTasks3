num = [4,2,-3,1,6]
tag = False
for i in range (len(num)):
    total=0
    for j in range(i,len(num)):
        total+=num[j]
        if total==0:
            print("Sublist with 0 found",num[i:j+1])
            tag = True

if not tag:
    print("sublist with 0 not found")
    
