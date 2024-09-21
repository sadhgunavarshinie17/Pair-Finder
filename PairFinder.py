def find_id_pair(nums, target):
    # Initialize an empty dictionary to store numbers and their indices
    numMap = {}

    # Get the length of the nums list
    n = len(nums)

    # Iterate over all elements in the nums list
    for i in range(n):
        # Calculate the complement of the current number to reach the target
        complement = target - nums[i]

        # Check if the complement is already in the dictionary
        if complement in numMap:
            # If the complement is found, return the indices of the complement and the current number
            return [numMap[complement], i]

        # If the complement is not found, store the current number and its index in the dictionary
        numMap[nums[i]] = i

    # Return an empty list if no two numbers add up to the target
    return []

# Example usage:
nums = [3, 2, 4]
target = 6
result = find_id_pair(nums, target)
print(result)  # Output: [1,2]