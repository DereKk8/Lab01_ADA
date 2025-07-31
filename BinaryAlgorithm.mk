## Pseudocode: Recursive Binary Search for Maximum in Unimodal Array

1. Define a helper function that takes `left` and `right` as parameters.
2. If `left` equals `right`, return `arr[left]` (base case: only one element).
3. Calculate `mid` as the middle index between `left` and `right`.
4. If `arr[mid]` is less than `arr[mid + 1]`:
    - The peak is in the right half. Recursively search from `mid + 1` to `right`.
5. Else:
    - The peak is in the left half (including `mid`). Recursively search from `left` to `mid`.
6. The main function calls the helper with `left = 0` and `right = len(arr) - 1