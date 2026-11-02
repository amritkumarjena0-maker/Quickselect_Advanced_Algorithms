
def insertion_sort(arr):
    """Sort a small array using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def median_of_medians(arr):
    """Find a deterministic pivot using groups of five."""

    if len(arr) <= 5:
        sorted_arr = insertion_sort(arr.copy())
        return sorted_arr[len(sorted_arr) // 2]

    medians = []

    for i in range(0, len(arr), 5):
        group = arr[i:i + 5]
        sorted_group = insertion_sort(group)
        medians.append(sorted_group[len(sorted_group) // 2])

    return deterministic_select(
        medians, len(medians) // 2
    )


def deterministic_select(arr, k):
    """
    Find the zero-based k-th smallest element.
    Worst-case time complexity: O(n).
    """

    if not arr or k < 0 or k >= len(arr):
        raise ValueError("Invalid selection index.")

    if len(arr) <= 5:
        return insertion_sort(arr.copy())[k]

    pivot = median_of_medians(arr)

    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    if k < len(smaller):
        return deterministic_select(smaller, k)

    elif k < len(smaller) + len(equal):
        return pivot

    else:
        return deterministic_select(
            greater,
            k - len(smaller) - len(equal)
        )


def main():
    print("=" * 55)
    print("       MEDIAN-OF-MEDIANS ALGORITHM")
    print("=" * 55)

    try:
        arr = list(map(int, input("Enter array elements: ").split()))

        if not arr:
            raise ValueError("Array cannot be empty.")

        k = int(input("Enter K (1-based): "))

        if k < 1 or k > len(arr):
            raise ValueError("K must be between 1 and array size.")

        result = deterministic_select(arr, k - 1)

        print("\nOriginal Array:", arr)
        print("Sorted Array:  ", sorted(arr))
        print(f"\n{ k }-th smallest element = {result}")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
