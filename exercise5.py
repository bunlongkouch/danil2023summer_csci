def reverse_ascending(numbers):
    result = []
    ascending_subseq = []
    
    for num in numbers:
        if not ascending_subseq or num > ascending_subseq[-1]:
            ascending_subseq.append(num)
        else:
            result.extend(reversed(ascending_subseq))
            ascending_subseq = [num]
    
    result.extend(reversed(ascending_subseq))
    return result

# Test cases
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
