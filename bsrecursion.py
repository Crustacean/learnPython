
def binary_search(arr, search):

    arr.sort()

    mid = len(arr)//2

    if search != arr[mid]:

        if search > arr[mid]:

            binary_search(arr[mid:], search)

        elif search < arr[mid]:

            binary_search(arr[:mid], search)

    else:
        return arr[mid]

numbers = [1, 3, 4,2, 6, 7,8,12,5]
target = 9

print(binary_search(numbers, target))