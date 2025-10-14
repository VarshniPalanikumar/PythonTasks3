even_list=[]
odd_list=[]
num_list = [10, 501, 22, 37, 100, 999, 87, 351]
for num in num_list:
    if num % 2 == 0:
        #even_list=even_list+[num]
        even_list.append(num)

    else:
        odd_list=odd_list+[num]
print(f"Even numbers in the given list are {even_list}")
print(f"Odd numbers in the given list are {odd_list}")


