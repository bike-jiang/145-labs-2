print("testing git")

x = 1, 2, 3, 4, 5
for num in x:
    print(num)


def find_num(x):
    for num in x:
        if num == 3:
            print("Found the correct number")


find_num([1, 2, 4, 5])
