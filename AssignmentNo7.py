def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence


nums = [100, 4, 200, 1, 3, 2]
print("The longest consecutive sequence length is:", longest_consecutive_sequence(nums))
