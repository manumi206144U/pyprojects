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
