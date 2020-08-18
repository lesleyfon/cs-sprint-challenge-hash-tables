def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dictionary = {}
    for i in range(len(a)):
        if a[i] > 0:
            dictionary[a[i]] = None

    for i in range(len(a)):
        if a[i] < 0:
            negative_to_positive = abs(a[i])
            if negative_to_positive in dictionary:
                result.append(negative_to_positive)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
