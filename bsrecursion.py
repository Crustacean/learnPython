
def binary_search_recursive(arr, search, left, right):

    if left > right:
        return

    mid = (left + right) // 2

    if search != arr[mid]:

        if search > arr[mid]:

            return binary_search_recursive(arr, search, mid + 1, right)

        elif search < arr[mid]:

            return binary_search_recursive(arr, search, left, mid - 1)

    else:
        return arr[mid]
    

def binary_search(arr, search):
    arr.sort()
    arr_length = len(arr) - 1
    return binary_search_recursive(arr, search, 0, arr_length)

numbers = [1, 3, 4,2, 6, 7,8,12,5]
target = 9

print(binary_search(numbers, target))