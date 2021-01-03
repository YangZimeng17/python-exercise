def find_value(nlist, key):
    while True:
        if key == nlist[0]:
            return nlist[1]
        if nlist[2] == None:
            return None
        nlist = nlist[2]

nlist = [4, 'hi', [0, 'bye', [6, 'good', None]]]  # nlist point to the array
print(find_value(nlist, 3))

def append_nlist(nlist, key, value):
    list = nlist  # save initial pointer
    while True:
        if nlist[2] == None:
            nlist[2] = [key, value, None]
            break
        nlist = nlist[2]  # move pointer to nested list
    return list  # return initial pointer

print(append_nlist(nlist, 5, 'hohoho'))
