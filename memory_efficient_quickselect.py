
import random


def partition(arr, low, high):
    """In-place Lomuto partitioning."""

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


def memory_efficient_quickselect(arr, k):
    """Find the 1-based k-th smallest element in-place."""

    if not arr:
        raise ValueError("Array cannot be empty.")

    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("K must be an integer.")

    if k < 1 or k > len(arr):
        raise ValueError("K must be between 1 and array size.")

    low = 0
    high = len(arr) - 1
    target = k - 1

    while low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == target:
            return arr[pivot_index]

        elif pivot_index < target:
            low = pivot_index + 1

        else:
            high = pivot_index - 1

    raise RuntimeError("Selection failed.")


def main():
    print("=" * 60)
    print("       MEMORY-EFFICIENT QUICKSELECT")
    print("=" * 60)

    try:
        arr = list(map(
            int,
            input("Enter array elements: ").split()
        ))

        k = int(input("Enter K (1-based): "))

        original = arr.copy()

        result = memory_efficient_quickselect(arr, k)

        print("\nOriginal Array:", original)
        print("Modified Array:", arr)
        print("Sorted Array:  ", sorted(original))
        print(f"\n{ k }-th smallest element = {result}")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
