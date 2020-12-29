def sorted_timestamps(timestamps):
    max = 0
    list = []
    for e in timestamps:
        minute = e[0] * 60 + e[1]
        list.append(minute)
        if minute > max:
            max = minute

    count = [0 for i in range(max + 1)]
    for i in range(len(list)):
        count[list[i]] += 1

    total = 0
    for i in range(max + 1):
        count[i], total = total, count[i] + total

    output = [0 for i in range(len(timestamps))]
    for i in range(len(list)):
        output[count[list[i]]] = (list[i] // 60, list[i] % 60)
        count[list[i]] += 1

    return output

list = [[(5,10),(2,40),(22,59),(5,10),(5,11),(5,9),(11,11),(0,0)]]
for e in list:
    print(sorted_timestamps(e))
