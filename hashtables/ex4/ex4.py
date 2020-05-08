def has_negatives(a):

    """
    YOUR CODE HERE
    """
    num = dict()
    result = list()

    for x in a:
        if num.get(abs(x)):
            if(num.get(abs(x)) + x) == 0:
                result.append(abs(x))
        else:
            num[abs(x)] = x

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
