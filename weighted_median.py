
def weighted_median(values, weights):
    """Calculate the weighted median of given values."""

    if len(values) != len(weights):
        raise ValueError("Values and weights must have equal lengths.")

    if not values:
        raise ValueError("Input cannot be empty.")

    if any(w < 0 for w in weights):
        raise ValueError("Weights cannot be negative.")

    if sum(weights) <= 0:
        raise ValueError("Total weight must be positive.")

    if any(not isinstance(w, (int, float)) or isinstance(w, bool)
           for w in weights):
        raise ValueError("Weights must be numeric.")

    if any(not isinstance(v, (int, float)) or isinstance(v, bool)
           for v in values):
        raise ValueError("Values must be numeric.")

    pairs = sorted(zip(values, weights), key=lambda x: x[0])

    total_weight = sum(weights)
    cumulative_weight = 0

    for value, weight in pairs:
        cumulative_weight += weight

        if cumulative_weight >= total_weight / 2:
            return value

    raise RuntimeError("Weighted median calculation failed.")


def main():
    print("=" * 55)
    print("          WEIGHTED MEDIAN ALGORITHM")
    print("=" * 55)

    try:
        values = list(map(
            float,
            input("Enter values: ").split()
        ))

        weights = list(map(
            float,
            input("Enter corresponding weights: ").split()
        ))

        result = weighted_median(values, weights)

        print("\nValues:  ", values)
        print("Weights: ", weights)
        print(f"\nWeighted Median = {result:g}")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
