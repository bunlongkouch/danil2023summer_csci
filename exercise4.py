def chunking_by(numbers, chunk):
    if not numbers or chunk <= 0:
        return []

    return [numbers[i:i+chunk] for i in range(0, len(numbers), chunk)]


print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
print(chunking_by([3, 4, 5], 1))
