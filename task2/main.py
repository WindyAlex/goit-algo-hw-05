def binary_search_upper_bound(arr, x):
    left = 0
    right = len(arr) - 1
    iterations = 0

    upper = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] >= x:
            upper = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return iterations, upper


def main():
    arr = [0.5, 1.0, 1.5, 2.0, 2.0, 3.7, 5.2]
    print(binary_search_upper_bound(arr, 2.0))  # 2.0
    print(binary_search_upper_bound(arr, 2.6))  # 3.7
    print(binary_search_upper_bound(arr, 6.0))  # None


main()
