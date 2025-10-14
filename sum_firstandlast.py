num=int(input("enter the number"))
last_dig=num%10
while num>=10:
    num=num//10
first_dig=num

sumofdig=first_dig+last_dig
print(f"sum of first and last digit in the given number is: {sumofdig}")