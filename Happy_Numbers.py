num = input("Enter a number: ")
original_num = num
visited = set()

while True:
    total = 0
    for i in num:
        total += int(i) ** 2
    if total == 1:
        print(f"The entered number {original_num} is a Happy number!")
        break
    if total in visited:
        print(f"The entered number {original_num} is not a Happy number.")
        break
    visited.add(total)
    num = str(total)  # update num for next iteration