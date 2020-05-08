def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    weights_dict = dict() 

    for x in range(length):
        y = weights_dict.get(limit - weights[x])
        if y != None:
            return(x, y)
        else:
            weights_dict[weights[x]] = x 
        
    return None
