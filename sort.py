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


