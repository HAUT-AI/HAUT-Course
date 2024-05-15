def binaray_search(array, find) -> int:
    if len(array) == 0:
        return -1
    mid = len(array)//2
    if array[mid] == find:
        return mid-1
    elif array[mid] > find:
        return binaray_search(array[:mid], find)
    else:
        return binaray_search(array[mid+1:], find)


print(binaray_search([1, 2, 3, 4, 5], 3))
