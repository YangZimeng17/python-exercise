def two_smallest(L):
    first = L[0]
    second = L[0]


    for e in L[2:]:
        if e < first:
            first, second = e, first
        elif e < second:
            second = e
        elif first == second:
            second = e

    return [second, first]

L = [2,5,3,4,7]
print(two_smallest(L))
