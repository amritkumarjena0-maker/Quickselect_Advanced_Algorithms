
import random


def partition(arr, low, high):
    """Randomized in-place partition."""

    pivot_index = random.randint(low, high)

    arr[pivot_index], arr[high] = (
        arr[high], arr[pivot_index]
    )

    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    return i


def quickselect(arr, k):
    """Find the zero-based k-th smallest element."""

    low = 0
    high = len(arr) - 1

    while low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k:
            return arr[pivot_index]

        elif pivot_index < k:
            low = pivot_index + 1

        else:
            high = pivot_index - 1

    raise RuntimeError("Quickselect failed.")


def median_two_unsorted_arrays(arr1, arr2):
    """Calculate median of two unsorted arrays."""

    if not arr1 and not arr2:
        raise ValueError("Both arrays cannot be empty.")

    combined = arr1 + arr2
    n = len(combined)

    if n % 2 == 1:
        return quickselect(combined, n // 2)

    left = quickselect(combined.copy(), n // 2 - 1)
    right = quickselect(combined, n // 2)

    return (left + right) / 2


def main():
    print("=" * 60)
    print("       MEDIAN OF TWO UNSORTED ARRAYS")
    print("=" * 60)

    try:
        arr1 = list(map(
            int,
            input("Enter first array: ").split()
        ))

        arr2 = list(map(
            int,
            input("Enter second array: ").split()
        ))

        result = median_two_unsorted_arrays(arr1, arr2)

        print("\nFirst Array: ", arr1)
        print("Second Array:", arr2)
        print("Combined Sorted Array:", sorted(arr1 + arr2))
        print("\nMedian =", result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
