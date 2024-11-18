def quick_sort(arr, ascending=True):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if ascending:
        return quick_sort(left, ascending) + middle + quick_sort(right, ascending)
    else:
        return quick_sort(right, ascending) + middle + quick_sort(left, ascending)

list1 = [3, 7, 8, 5, 2, 1, 9, 6, 4]
list2 = [5, 2, 9, 1, 5, 7]

print("Сортування за зростанням:")
print(quick_sort(list1))
print(quick_sort(list2))

print("\nСортування за спаданням:")
print(quick_sort(list1, False))
print(quick_sort(list2, False))