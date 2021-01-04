def triple_m(tuple_ints):

    list_ints = list(tuple_ints)
    length = len(list_ints)


    for i in range(length - 1):
        for j in range(i, length):
            if list_ints[j] < list_ints[i]:
                list_ints[i] , list_ints[j] = list_ints[j] , list_ints[i]

    if length % 2 != 0:
        median = list_ints[length//2]
    else:
        median = (list_ints[length//2] + list_ints[length//2 - 1]) / 2


    pre_count  = 0
    cur_count = 0
    mode = list_ints[0]
    sum = list_ints[0]

    for i in range(1, length):
        sum += list_ints[i]
        if list_ints[i] != list_ints[i - 1]:
            cur_count = 1
        else:
            cur_count += 1

        if cur_count > pre_count:
            pre_count = cur_count
            mode = list_ints[i]

    mean = sum / length

    return (mean, median, mode)

print(triple_m((1,9,3,9,4,6,4,5,6,6)))

