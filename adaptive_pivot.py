
import random


def median_of_three(arr, low, high):
    """Choose the median of first, middle and last elements."""

    mid = (low + high) // 2

    candidates = [
        (arr[low], low),
        (arr[mid], mid),
        (arr[high], high)
    ]

    candidates.sort(key=lambda item: item[0])

    return candidates[1][1]


def adaptive_partition(arr, low, high, use_random):
    """Partition array using an adaptive pivot."""

    if use_random:
        pivot_index = random.randint(low, high)
    else:
        pivot_index = median_of_three(arr, low, high)

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


def adaptive_quickselect(arr, k):
    """Find the 1-based k-th smallest element."""

    if not arr:
        raise ValueError("Array cannot be empty.")

    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("K must be an integer.")

    if k < 1 or k > len(arr):
        raise ValueError("Invalid K value.")

    low = 0
    high = len(arr) - 1
    target = k - 1

    bad_partitions = 0
    max_bad_partitions = 2

    while low <= high:

        use_random = bad_partitions >= max_bad_partitions

        pivot_index = adaptive_partition(
            arr, low, high, use_random
        )

        left_size = pivot_index - low
        right_size = high - pivot_index

        current_size = high - low + 1

        # Detect highly unbalanced partitions.
        if min(left_size, right_size) < current_size // 10:
            bad_partitions += 1
        else:
            bad_partitions = 0

        if pivot_index == target:
            return arr[pivot_index]

        elif pivot_index < target:
            low = pivot_index + 1

        else:
            high = pivot_index - 1

    raise RuntimeError("Selection failed.")


def main():
    print("=" * 60)
    print("       ADAPTIVE PIVOT SELECTION ALGORITHM")
    print("=" * 60)

    try:
        arr = list(map(
            int,
            input("Enter array elements: ").split()
        ))

        k = int(input("Enter K (1-based): "))

        original = arr.copy()

        result = adaptive_quickselect(arr, k)

        print("\nOriginal Array:", original)
        print("Sorted Array:  ", sorted(original))
        print(f"\n{ k }-th smallest element = {result}")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
