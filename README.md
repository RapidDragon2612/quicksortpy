# QuickSortPy

**QuickSortPy** (by RapidDragon2612) is a Python implementation of the **Quick Sort** algorithm.

Quick Sort is widely regarded as one of the fastest and most efficient general-purpose sorting algorithms.

---

## Installation

Install QuickSortPy using pip:

```bash
pip install quicksortpy
```

---

## Usage

Import the library in your Python file:

```python
import quicksortpy
```

### Sort an array (in-place)

```python
quicksortpy.sort(example_array)
```

This will sort `example_array` in place.

---

### Sort into a new array

```python
sorted_arr = quicksortpy.sort(example_array, True)
```

This returns a new sorted array without modifying the original.

---

## Visualization

For educational purposes, you can visualize how the Quick Sort algorithm works step by step:

```python
quicksortpy.visualize(example_array)
```

or:

```python
quicksortpy.visualise(example_array)
```

This will display each step the algorithm takes while sorting the array.

---

## Notes

- The `sort()` function accepts:
  - `array`: The list to sort  
  - `new_arr` (optional): Set to `True` to return a new sorted list instead of modifying the original  