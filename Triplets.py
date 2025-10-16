num = [10,20,30,9]
triplets=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        for k in range(j+1,len(num)):
            if num[i]+num[j]+num[k]==59:
                triplets.append([num[i],num[j],num[k]])
if len(triplets)>0:
    print("triplets:",triplets)
else:
    print("no triplets found")