
def multi_selection(arr, ranks):
    """
    Find multiple k-th smallest elements using
    recursive Quickselect-style partitioning.

    Ranks are 1-based.
    """
    results = {}

    def solve(data, requested_ranks, offset):
        if not requested_ranks:
            return

        if len(data) == 1:
            for rank in requested_ranks:
                results[rank] = data[0]
            return

        pivot = data[len(data) // 2]

        smaller = [x for x in data if x < pivot]
        equal = [x for x in data if x == pivot]
        greater = [x for x in data if x > pivot]

        left_size = len(smaller)
        equal_size = len(equal)

        left_ranks = []
        right_ranks = []

        for rank in requested_ranks:
            local_rank = rank - offset

            if local_rank <= left_size:
                left_ranks.append(rank)

            elif local_rank <= left_size + equal_size:
                results[rank] = pivot

            else:
                right_ranks.append(rank)

        if left_ranks:
            solve(smaller, left_ranks, offset)

        if right_ranks:
            solve(
                greater,
                right_ranks,
                offset + left_size + equal_size
            )

    n = len(arr)

    if not arr:
        raise ValueError("Array cannot be empty.")

    if not ranks:
        return {}

    if any(not isinstance(k, int) or isinstance(k, bool)
           or k < 1 or k > n for k in ranks):
        raise ValueError(f"Ranks must be between 1 and {n}.")

    solve(arr.copy(), ranks, 0)

    return {k: results[k] for k in ranks}


def main():
    print("=" * 55)
    print("       MULTI-SELECTION ALGORITHM")
    print("=" * 55)

    arr = list(map(int, input("Enter array elements: ").split()))

    ranks = list(map(
        int,
        input("Enter ranks (1-based, space-separated): ").split()
    ))

    try:
        answers = multi_selection(arr, ranks)

        print("\nOriginal Array:", arr)
        print("Sorted Array:  ", sorted(arr))

        print("\nMulti-Selection Results:")

        for rank, value in answers.items():
            print(f"{rank}-th smallest element = {value}")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
