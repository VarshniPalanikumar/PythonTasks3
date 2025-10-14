prime =[]
number_list = [10,501,22,37,100,999,87,351,3]

for num in number_list:
    if num >1:
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
                prime.append(num)

print(f"prime numbers are {prime}")

