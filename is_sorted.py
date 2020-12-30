def is_sorted(L):
    if len(L) < 3:
        return True

    is_inc = True
    is_dec = True
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            is_inc = is_inc and False
            is_dec = is_dec and True
        elif L[i] < L[i+1]:
            is_inc = is_inc and True
            is_dec = is_dec and False
        else:
            is_inc = is_inc and True
            is_dec = is_dec and True

    return is_inc or is_dec

test = [[],[1],[2,3],[3,2],[1,1,3],[1,1,1],[1,2,3],[3,2,1],[3,3,2], [3,2,2], [3,1,3]]

for e in test:
    print(is_sorted(e))