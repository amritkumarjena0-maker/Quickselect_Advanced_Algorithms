
import heapq
import os
import tempfile


def create_data_file(filename, values):
    """Create an input file containing integers."""
    with open(filename, "w") as file:
        for value in values:
            file.write(f"{value}\n")


def external_quickselect(filename, k, chunk_size=1000):
    """Find the 1-based k-th smallest value using external storage."""

    if k < 1:
        raise ValueError("K must be positive.")

    if chunk_size < 1:
        raise ValueError("Chunk size must be positive.")

    temp_files = []
    total_count = 0

    try:
        # Read the input in limited-size chunks.
        with open(filename, "r") as source:
            while True:
                chunk = []

                for _ in range(chunk_size):
                    line = source.readline()

                    if not line:
                        break

                    chunk.append(int(line.strip()))

                if not chunk:
                    break

                total_count += len(chunk)
                chunk.sort()

                temp = tempfile.NamedTemporaryFile(
                    mode="w",
                    delete=False,
                    suffix=".txt"
                )

                with temp:
                    for value in chunk:
                        temp.write(f"{value}\n")

                temp_files.append(temp.name)

        if k > total_count:
            raise ValueError(
                f"K cannot exceed total elements ({total_count})."
            )

        # Open all sorted temporary files.
        files = [open(path, "r") for path in temp_files]

        try:
            heap = []

            # Insert first element from each file.
            for index, file in enumerate(files):
                line = file.readline()

                if line:
                    heapq.heappush(
                        heap,
                        (int(line.strip()), index)
                    )

            # Extract elements in sorted order.
            for position in range(1, k + 1):
                value, file_index = heapq.heappop(heap)

                if position == k:
                    return value

                line = files[file_index].readline()

                if line:
                    heapq.heappush(
                        heap,
                        (int(line.strip()), file_index)
                    )

        finally:
            for file in files:
                file.close()

    finally:
        for path in temp_files:
            if os.path.exists(path):
                os.remove(path)


def main():
    print("=" * 60)
    print("       EXTERNAL-MEMORY QUICKSELECT")
    print("=" * 60)

    filename = "large_dataset.txt"

    try:
        values = [
            45, 12, 89, 34, 67, 23, 90, 10,
            56, 78, 15, 99, 32, 5, 81, 42
        ]

        create_data_file(filename, values)

        print("Dataset file:", filename)
        print("Total elements:", len(values))

        k = int(input("Enter K (1-based): "))

        result = external_quickselect(
            filename,
            k,
            chunk_size=4
        )

        print(f"\n{ k }-th smallest element = {result}")

    except (ValueError, OSError) as error:
        print("Error:", error)

    finally:
        if os.path.exists(filename):
            os.remove(filename)


if __name__ == "__main__":
    main()
