rows = int(input("Enter Rows: "))

for i in range(rows+1, 0, -1):
    for j in range(0, i-1):
        print("*", end=" ")
    print()