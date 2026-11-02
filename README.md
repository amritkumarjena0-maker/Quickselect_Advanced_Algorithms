
# Quickselect Advanced Algorithms

## Description

This project implements eight advanced selection algorithms using Python. It focuses on efficient order-statistic selection, deterministic pivot selection, memory optimization, external-memory processing, adaptive strategies, and GPU computing.

## Features

- Multi-Selection Algorithm
- Median-of-Medians Algorithm
- Memory-Efficient Quickselect
- Weighted Median Algorithm
- External-Memory Quickselect
- Adaptive Pivot Selection
- Median of Two Unsorted Arrays
- GPU-Accelerated Quickselect
- In-place partitioning
- Randomized and deterministic selection
- CPU and GPU computation support

## Technologies

- Python 3
- PyTorch
- CUDA
- Heap Queue
- Random
- File Handling

## Requirements

- Python 3.10 or higher
- PyTorch

## Project Structure

```text
Quickselect_Advanced_Algorithms/
│
├── multi_selection.py
├── median_of_medians.py
├── memory_efficient_quickselect.py
├── weighted_median.py
├── external_memory_quickselect.py
├── adaptive_pivot.py
├── median_two_unsorted_arrays.py
├── gpu_quickselect.py
│
├── README.md
└── requirements.txt
```

## Algorithms

### 1. Multi-Selection Algorithm

Finds multiple K-th smallest elements in an array using recursive partitioning.

### 2. Median-of-Medians Algorithm

Uses groups of five to select a deterministic pivot and guarantees worst-case linear selection time.

### 3. Memory-Efficient Quickselect

Uses randomized in-place partitioning to reduce additional memory requirements.

### 4. Weighted Median Algorithm

Finds the weighted median using sorted values and cumulative weights.

### 5. External-Memory Quickselect

Processes large datasets using chunks, temporary files, and a min-heap.

### 6. Adaptive Pivot Selection

Uses median-of-three and randomized pivot strategies to improve partition quality.

### 7. Median of Two Unsorted Arrays

Combines two unsorted arrays and uses Quickselect to find their median.

### 8. GPU-Accelerated Quickselect

Uses PyTorch tensor sorting with CUDA support when available and CPU fallback otherwise.

## Algorithm Complexity

| No. | Algorithm | Expected / Worst-Case Time |
|---|---|---|
| 7 | Multi-Selection | O(n log q) average for balanced partitions |
| 8 | Median-of-Medians | O(n) worst case |
| 11 | Memory-Efficient Quickselect | O(n) expected / O(n²) worst |
| 12 | Weighted Median | O(n log n) |
| 15 | External-Memory Selection | O(n log M + K log r) |
| 16 | Adaptive Pivot Selection | O(n) expected / O(n²) worst |
| 18 | Median of Two Unsorted Arrays | O(n) expected / O(n²) worst |
| 19 | GPU-Accelerated Selection | O(n log n) |

## How to Run

Run the Python programs from the main project folder.

### Multi-Selection

```powershell
python multi_selection.py
```

### Median-of-Medians

```powershell
python median_of_medians.py
```

### Memory-Efficient Quickselect

```powershell
python memory_efficient_quickselect.py
```

### Weighted Median

```powershell
python weighted_median.py
```

### External-Memory Quickselect

```powershell
python external_memory_quickselect.py
```

### Adaptive Pivot Selection

```powershell
python adaptive_pivot.py
```

### Median of Two Unsorted Arrays

```powershell
python median_two_unsorted_arrays.py
```

### GPU-Accelerated Quickselect

```powershell
python gpu_quickselect.py
```

## Algorithm Flowchart

```text
                 START
                   |
              Input Array
                   |
          Select Algorithm
                   |
             Process Input
                   |
          Apply Selection Method
                   |
          Find Required Element
                   |
            Display Result
                   |
                  END
```

## Applications

- Database query processing
- Large dataset analysis
- Statistical computation
- Machine learning
- Memory-constrained systems
- GPU-based data processing
- Order-statistic problems

## Note

This project contains educational implementations of advanced selection techniques. Actual performance depends on input size, pivot strategy, memory constraints, and available hardware.

## Author

Amrit Kumar Jena
