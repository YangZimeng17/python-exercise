def insert(L,e):
    if len(L) == 0:
        return [e]
    for i in range(len(L)):
        if e <= L[i]:
            return L[:i] + [e] + L[i:]
    return L + [e]


def bi_insert(L,e):
    if len(L) == 0:
        return [e]
    if e < L[0]:
        return [e] + L
    if e > L[len(L)-1]:
        return L + [e]

    low = 0
    mid = len(L) // 2
    high = len(L) - 1

    while True:
        if L[mid] == e:
            return L[:mid] + [e] + L[mid:]
        elif L[mid] < e:
            low = mid
        else:
            high = mid
        mid = (high + low) // 2
        if mid == low:
            return L[:low+1] + [e] + L[low+1:]
        if mid == high:
            return L[:high] + [e] + L[high:]
