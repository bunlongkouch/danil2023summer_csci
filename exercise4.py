def chunking_by(lst, chunk_size):
    if not lst or chunk_size <= 0:
        return []

    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
print(chunking_by([3, 4, 5], 1))
