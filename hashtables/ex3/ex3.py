def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    hash_map = {}
    length = len(arrays)
    for i in range(length):
        for k in range(len(arrays[i])):

            if arrays[i][k] in hash_map:
                hash_map[arrays[i][k]] += 1
            else:
                hash_map[arrays[i][k]] = 1
    # Your code here
    for key, value in hash_map.items():
        if value == length:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = [[1, 2, 3],
              [1, 4, 5, 3],
              [1, 6, 7, 3]]

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
