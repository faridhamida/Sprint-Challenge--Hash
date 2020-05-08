#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    trips = dict()
    route = list()

    for x in tickets:
        trips[x.source] = x.destination

    index = 0 
    dest = "NONE"

    while index < length:
        dest = trips.get(dest)
        route.append(dest)
        index += 1
        
    return route
