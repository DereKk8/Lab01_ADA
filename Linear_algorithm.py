def find_peak_linear(arr):
    """
    Finds the peak (maximum) in a unimodal (bitonic) array using a linear scan.
    Complexity: O(n)
    Parameters:
        arr (list): Unimodal array of numbers.
    Returns:
        int/float: The maximum (peak) value of the array.
    """
    if not arr:
        raise ValueError("Array cannot be empty.")
    peak = arr[0]
    for num in arr:
        if num > peak:
            peak = num
    return peak