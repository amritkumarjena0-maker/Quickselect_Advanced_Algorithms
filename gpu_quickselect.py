
import time
import torch


def gpu_quickselect(arr, k):
    """
    GPU-based K-th smallest selection using PyTorch sorting.
    Uses CUDA when available; otherwise CPU.
    """

    if not arr:
        raise ValueError("Array cannot be empty.")

    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("K must be an integer.")

    if k < 1 or k > len(arr):
        raise ValueError("K must be between 1 and array size.")

    # Select computation device.
    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    # Transfer data to selected device.
    tensor = torch.tensor(
        arr,
        dtype=torch.int64,
        device=device
    )

    # Sort elements on GPU or CPU.
    sorted_tensor = torch.sort(tensor).values

    # Extract K-th smallest element.
    result = sorted_tensor[k - 1].item()

    return result, device.type


def main():
    print("=" * 60)
    print("       GPU-ACCELERATED QUICKSELECT")
    print("=" * 60)

    try:
        arr = list(map(
            int,
            input("Enter array elements: ").split()
        ))

        k = int(input("Enter K (1-based): "))

        start_time = time.perf_counter()

        result, device = gpu_quickselect(arr, k)

        end_time = time.perf_counter()

        print("\nOriginal Array:", arr)
        print("Sorted Array:  ", sorted(arr))
        print("Processing Device:", device.upper())

        print(f"\n{ k }-th smallest element = {result}")

        print(
            f"Execution Time: "
            f"{(end_time - start_time) * 1000:.4f} ms"
        )

        if device == "cuda":
            print("GPU Acceleration: ENABLED")
        else:
            print("GPU Acceleration: NOT AVAILABLE")
            print("CPU fallback was used.")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
