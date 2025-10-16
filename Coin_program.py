total=10
count=0
for i in range(0,total//10+1):
    for j in range(0, total//5+1):
        for k in range(0, total//2+1):
            for l in range(0, total+1):
                if (i*10)+(j*5)+(k*2)+(1*l)==total:
                    coins = i*[10]+j*[5]+k*[2]+l*[1]
                    print(coins)
                    count+=1
print("Total No of ways:",count)

