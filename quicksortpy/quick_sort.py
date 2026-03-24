def partition(arr, low, high):
    pivot = arr[high]

    swap_idx = low - 1

    for curr_idx in range(low, high):
        if arr[curr_idx] <= pivot:
            swap_idx += 1
            arr[swap_idx], arr[curr_idx] = arr[curr_idx], arr[swap_idx]

    arr[swap_idx + 1], arr[high] = arr[high], arr[swap_idx + 1]

    return swap_idx + 1


def sort(arr, new_arr=False, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if not low >= high:
        if new_arr:
            sorted_arr = arr
            pivot_idx = partition(sorted_arr, low, high)
            sort(sorted_arr, False, pivot_idx + 1, high)
            sort(sorted_arr, False, low, pivot_idx - 1)
        else:
            pivot_idx = partition(arr, low, high)
            sort(arr, False, pivot_idx + 1, high)
            sort(arr, False, low, pivot_idx - 1)
