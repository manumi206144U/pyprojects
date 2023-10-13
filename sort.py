def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps were made in this pass
        swapped = False

        # Last i elements are already in place, so we don't need to compare them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made in this pass, the array is already sorted
        if not swapped:
            break

print("On testbranch-1")

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array is:", my_list)

# 1. Reverse sorting
def bubble_sort_reverse(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Reverse the comparison for descending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# 2. Return a new sorted list without modifying the original list
def bubble_sort_new(arr):
    sorted_arr = arr.copy()  # Create a copy to avoid modifying the original array
    n = len(sorted_arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break
    return sorted_arr