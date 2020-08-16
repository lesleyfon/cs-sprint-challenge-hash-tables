def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_map = {}
    for i in range(length):
        for k in range(length):
            if i != k:
                total = weights[i] + weights[k]
                if total == limit:
                    hash_map[total] = (i, k)

    if len(hash_map.keys()) == 0:
        return None
    else:
        return hash_map[limit]
