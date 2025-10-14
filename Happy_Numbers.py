num = input("Enter a number: ")
original_num = num  # store original number
visited = set()

while True:
    total = 0
    for i in num:
        total += int(i) ** 2

    # Check if number is happy
    if total == 1:
        print(f"The entered number {original_num} is a Happy number!")
        break
    # Check if number is repeating (unhappy loop)
    if total in visited:
        print(f"The entered number {original_num} is not a Happy number.")
        break
    # Add to visited **before updating num**
    visited.add(total)
    num = str(total)  # update num for next iteration