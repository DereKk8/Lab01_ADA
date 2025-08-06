import time
import random
import matplotlib.pyplot as plt
import numpy as np
from BitonicArrayGenerator import generate_unimodal
from BinaryAlgorithm import find_max_recursive
from Linear_algorithm import find_peak_linear

def test_algorithm(algorithm_func, arr, algorithm_name):
    """
    Test a single algorithm and measure execution time.
    
    Args:
        algorithm_func: Function to test
        arr: Input array
        algorithm_name: Name of the algorithm for logging
        
    Returns:
        tuple: (result, execution_time_in_seconds)
    """
    start_time = time.perf_counter()
    result = algorithm_func(arr)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return result, execution_time

def run_empirical_tests():
    """
    Run comprehensive empirical tests on both algorithms.
    """
    # Test parameters
    array_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    increment = 1
    trials_per_size = 10
    
    # Results storage
    linear_times = []
    binary_times = []
    linear_results = []
    binary_results = []
    
    print("Starting empirical tests...")
    print("=" * 60)
    
    for size in array_sizes:
        print(f"\nTesting with array size: {size}")
        print("-" * 40)
        
        size_linear_times = []
        size_binary_times = []
        size_linear_results = []
        size_binary_results = []
        
        for trial in range(trials_per_size):
            # Generate test array
            test_array = generate_unimodal(size, increment)
            
            # Test linear algorithm
            linear_result, linear_time = test_algorithm(
                find_peak_linear, test_array, "Linear"
            )
            size_linear_times.append(linear_time)
            size_linear_results.append(linear_result)
            
            # Test binary algorithm
            binary_result, binary_time = test_algorithm(
                find_max_recursive, test_array, "Binary"
            )
            size_binary_times.append(binary_time)
            size_binary_results.append(binary_result)
            
            # Verify both algorithms return the same result
            if linear_result != binary_result:
                print(f"ERROR: Results don't match! Linear: {linear_result}, Binary: {binary_result}")
                print(f"Array: {test_array}")
                return
        
        # Calculate averages for this size
        avg_linear_time = np.mean(size_linear_times)
        avg_binary_time = np.mean(size_binary_times)
        
        linear_times.append(avg_linear_time)
        binary_times.append(avg_binary_time)
        
        print(f"Average Linear time: {avg_linear_time:.6f} seconds")
        print(f"Average Binary time: {avg_binary_time:.6f} seconds")
    
    return array_sizes, linear_times, binary_times

def plot_results(array_sizes, linear_times, binary_times):
    """
    Create performance comparison plots.
    """
    plt.figure(figsize=(15, 6))
    
    # Plot 1: Execution Time Comparison
    plt.subplot(1, 2, 1)
    plt.plot(array_sizes, linear_times, 'b-o', label='Linear O(n)', linewidth=2, markersize=6)
    plt.plot(array_sizes, binary_times, 'r-s', label='Binary O(log n)', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 2: Actual vs Theoretical Performance
    plt.subplot(1, 2, 2)
    # Theoretical curves
    theoretical_linear = [size * linear_times[0] / array_sizes[0] for size in array_sizes]
    theoretical_binary = [np.log2(size) * binary_times[0] / np.log2(array_sizes[0]) for size in array_sizes]
    
    plt.plot(array_sizes, linear_times, 'b-o', label='Actual Linear', linewidth=2, markersize=6)
    plt.plot(array_sizes, theoretical_linear, 'b--', label='Theoretical Linear', linewidth=2)
    plt.plot(array_sizes, binary_times, 'r-s', label='Actual Binary', linewidth=2, markersize=6)
    plt.plot(array_sizes, theoretical_binary, 'r--', label='Theoretical Binary', linewidth=2)
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Actual vs Theoretical Performance')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    plt.tight_layout()
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

def print_detailed_results(array_sizes, linear_times, binary_times):
    """
    Print detailed results in a formatted table.
    """
    print("\n" + "=" * 80)
    print("DETAILED EMPIRICAL RESULTS")
    print("=" * 80)
    print(f"{'Size':<10} {'Linear (s)':<12} {'Binary (s)':<12}")
    print("-" * 50)
    
    for i, size in enumerate(array_sizes):
        linear_time = linear_times[i]
        binary_time = binary_times[i]
        
        print(f"{size:<10} {linear_time:<12.6f} {binary_time:<12.6f}")

def verify_algorithm_correctness():
    """
    Verify that both algorithms produce correct results on various test cases.
    """
    print("\nVerifying algorithm correctness...")
    print("-" * 40)
    
    test_cases = [
        # Simple cases
        ([1, 3, 5, 7, 6, 4, 2], 7),
        ([1, 2, 3, 4, 5, 4, 3, 2, 1], 5),
        ([5, 4, 3, 2, 1], 5),
        ([1, 2, 3, 4, 5], 5),
        ([10], 10),
        ([1, 2, 1], 2),
    ]
    
    for i, (test_array, expected_max) in enumerate(test_cases):
        linear_result = find_peak_linear(test_array)
        binary_result = find_max_recursive(test_array)
        
        print(f"Test case {i+1}: {test_array}")
        print(f"  Expected: {expected_max}")
        print(f"  Linear: {linear_result}")
        print(f"  Binary: {binary_result}")
        
        if linear_result == expected_max and binary_result == expected_max:
            print("  ✓ PASS")
        else:
            print("  ✗ FAIL")
        print()

if __name__ == "__main__":
    # Verify correctness first
    verify_algorithm_correctness()
    
    # Run empirical tests
    array_sizes, linear_times, binary_times = run_empirical_tests()
    
    # Print detailed results
    print_detailed_results(array_sizes, linear_times, binary_times)
    
    # Create plots
    plot_results(array_sizes, linear_times, binary_times)
    
    print("\nEmpirical testing completed!")
    print("Results saved to 'performance_comparison.png'") 