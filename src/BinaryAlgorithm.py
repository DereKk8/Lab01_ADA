from BitonicArrayGenerator import generate_unimodal


def find_max_recursive(arr):
    """
    Recursive binary search to find maximum in unimodal array.
    Always searches the whole array.

    Args:
        arr: The unimodal array

    Returns:
        Maximum element value
    """
    def helper(left, right):
        # Base case: single element
        if left == right:
            return arr[left]
        # Calculate middle point
        mid = left + (right - left) // 2
        # Recursive case: decide which half contains the peak
        if arr[mid] < arr[mid + 1]:
            # Peak is in right half
            return helper(mid + 1, right)
        else:
            # Peak is in left half (including mid)
            return helper(left, mid)

    return helper(0, len(arr) - 1)
