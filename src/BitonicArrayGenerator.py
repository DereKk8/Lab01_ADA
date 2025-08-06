
import random

def generate_unimodal(n, increment):
    """
    Generate a simple unimodal array with the peak at a random position.

    Args:
        n: Size of array
        increment: Step size for increases/decreases

    Returns:
        List representing unimodal array
    """
    if n <= 0:
        return []
    if n == 1:
        return [increment]

    # Choose peak position randomly
    peak_pos = random.randint(0, n - 1)

    # Initialize array
    arr = [0] * n

    # Set peak value
    peak_value = increment * peak_pos
    arr[peak_pos] = peak_value

    # Fill left side (increasing to peak)
    for i in range(peak_pos - 1, -1, -1):
        arr[i] = arr[i + 1] - increment
        

    # Fill right side (decreasing from peak)
    for i in range(peak_pos + 1, n):
        arr[i] = arr[i - 1] - increment

    
    return arr
