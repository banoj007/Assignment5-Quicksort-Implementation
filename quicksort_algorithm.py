

import random
import time
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# 1️⃣ DETERMINISTIC QUICKSORT
# -----------------------------------------------------------
def quicksort_deterministic(arr):
    """Implements the deterministic version of Quicksort."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  # Choose last element as pivot
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return quicksort_deterministic(left) + [pivot] + quicksort_deterministic(right)

# -----------------------------------------------------------
# 2️⃣ RANDOMIZED QUICKSORT
# -----------------------------------------------------------
def quicksort_randomized(arr):
    """Implements the randomized version of Quicksort."""
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
        return quicksort_randomized(left) + [pivot] + quicksort_randomized(right)

# -----------------------------------------------------------
# 3️⃣ PERFORMANCE TESTING FUNCTION
# -----------------------------------------------------------
def measure_time(sort_func, arr):
    """Measure execution time of a sorting function."""
    start = time.time()
    sort_func(arr.copy())
    end = time.time()
    return end - start

def run_experiments():
    """Compare deterministic and randomized quicksort on different inputs."""
    sizes = [100, 500, 1000, 5000, 10000]
    results = {"Deterministic": [], "Randomized": []}

    for n in sizes:
        print(f"\nTesting with input size: {n}")
        random_data = [random.randint(0, 100000) for _ in range(n)]

        # Random data
        t1 = measure_time(quicksort_deterministic, random_data)
        t2 = measure_time(quicksort_randomized, random_data)

        results["Deterministic"].append(t1)
        results["Randomized"].append(t2)

        print(f"Deterministic QuickSort: {t1:.5f}s | Randomized QuickSort: {t2:.5f}s")

    # Plot the results
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, results["Deterministic"], marker='o', label='Deterministic Quicksort')
    plt.plot(sizes, results["Randomized"], marker='o', label='Randomized Quicksort')
    plt.title("Performance Comparison of Deterministic vs Randomized Quicksort")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

# -----------------------------------------------------------
# 4️⃣ COMPLEXITY ANALYSIS (THEORETICAL SUMMARY)
# -----------------------------------------------------------
def print_analysis():
    print("\n===== TIME COMPLEXITY ANALYSIS =====")
    print("Best Case: O(n log n)  → When pivot splits array evenly")
    print("Average Case: O(n log n) → On average, good pivot selection")
    print("Worst Case: O(n²) → When pivot always smallest/largest (e.g., sorted input)")
    print("\n===== SPACE COMPLEXITY =====")
    print("Space: O(log n) due to recursion stack (in-place variant)")
    print("\n===== RANDOMIZED QUICKSORT ADVANTAGE =====")
    print("Randomization reduces the chance of worst-case partitioning by ensuring pivot choice is random.\n")

# -----------------------------------------------------------
# 5️⃣ MAIN FUNCTION
# -----------------------------------------------------------
if __name__ == "__main__":
    print("Assignment 5: Quicksort Implementation and Analysis\n")
    print_analysis()
    run_experiments()

