import sys

def canStaff(weights, t, max_weight):
    """Checks if we can distribute shifts among TAs without exceeding max_weight."""
    numTAs = 1  # Start with one TA
    current_weight = 0  # Workload of the current TA

    for weight in weights:
        if current_weight + weight > max_weight:
            numTAs += 1  # Assign a new TA
            current_weight = weight  # Start new workload
            if numTAs > t:  # More TAs needed than available
                return False
        else:
            current_weight += weight  # Add shift to current TA
    
    return True

def minMaxWeight(weights, t):
    """Uses binary search to determine the minimum possible max workload per TA."""
    left, right = max(weights), sum(weights)

    while left < right:
        mid = (left + right) // 2
        if canStaff(weights, t, mid):  
            right = mid  # Try a smaller max workload
        else:
            left = mid + 1  # Increase max workload since TAs are not enough

    return left

# This reads in the input from stdin -- you can always assume that the input is valid
def main():
    test_cases = int(sys.stdin.readline().strip())
    
    for _ in range(test_cases):
        s, t = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        
        print(minMaxWeight(arr, t))

if __name__ == "__main__":
    main()
