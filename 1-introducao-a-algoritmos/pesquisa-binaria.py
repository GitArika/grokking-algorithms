def binary_search(items, target):
    low = 0
    high = len(items) -1

    while low <= high:
        middle = (low + high) // 2
        guess = items[middle]

        if guess == target:
            return middle
        if guess > target:
            high = middle -1
        else:
            low = middle +1

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 1))

print(binary_search(my_list, -1))

