# Pseudocode: Linear Algorithm for Finding the Peak in a Unimodal Array

## Problem
Given a unimodal (bitonic) array, find the peak (maximum) element using a linear scan.

## Pseudocode

```
function find_peak_linear(arr):
    if arr is empty:
        raise error "Array cannot be empty"
    peak = arr[0]
    for each num in arr:
        if num > peak:
            peak = num
    return peak
```

## Explanation
- The algorithm iterates through the array once.
- It keeps track of the largest value found so far (`peak`).
- At the end, it returns the maximum value, which is the peak of the unimodal array.
- Time complexity: O(n).