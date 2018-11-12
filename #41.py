'''
Given an unordered list of flights taken by someone, each represented
as an origin, destination pair, and a starting airport, compute the
person's itinerary. If no such itinerary exists, return null, if there is
multiple paths, return the lexicographically smallest one.
All flights must be used.

e.g.
[(SFO, HKO), (YYZ, SFO), (YUL, YYZ), (HKO, ORD)], YUL
return
[YUL, YYZ, SFO, HKO, ORD]
'''
def get_itinerary(flights, starting_airport):
    itinerary = [starting_airport]
    flights.sort(key = lambda x:x[1])
    return get_itinerary_helper(flights, itinerary)

def get_itinerary_helper(flights, current_itinerary):
    if not flights:
        return current_itinerary

    start = current_itinerary[-1]

    for idx, (origin, destination) in enumerate(flights):
        if start == origin:
            flights_minus_current = flights[:idx] + flights[idx + 1:]
            current_itinerary.append(destination)
            return get_itinerary_helper(flights_minus_current, current_itinerary)
            current_itinerary.pop()

    return None

if __name__ == '__main__':
    flights = [('a', 'c'), ('a', 'b'), ('b', 'c'), ('c', 'a')]
    starting_airport = 'a'

    itinerary = get_itinerary(flights, starting_airport)
    print(itinerary)