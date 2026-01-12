def get_lowest_index(arr):
    lowest = arr[0]
    lowest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]
            lowest_index = i
    return lowest_index

def selection_sort(arr):
    sortedArr = []
    for _ in range(len(arr)):
        lowest_index = get_lowest_index(arr)
        sortedArr.append(arr.pop(lowest_index))
    return sortedArr

print(selection_sort([5, 3, 6, 2, 10]))
