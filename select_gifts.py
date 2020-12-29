def select_gifts(good_ratings, want_ratings):
    dict_total = {}
    max_value = 0
    list = []


    for key,value in good_ratings.items():
        cur_value = 0
        if key not in want_ratings:
            cur_value = value
        else:
            cur_value = value + want_ratings[key]
        if cur_value > max_value:
            max_value = cur_value
            list = [key]
        elif cur_value == max_value:
            list.append(key)


    for key,value in want_ratings.items():
        if key not in dict_total:
            if value > max_value:
                max_value = value
                list = [key]
            elif value == max_value:
                list.append(key)

    for i in range(len(list)-1):
        min = list[i]
        index = i
        for j in range(i,len(list)):
            if list[j] < min:
                min = list[j]
                index = j
        list[i], list[index] = list[index],list[i]

    return list


good_ratings = {"Calc textbook":5, "iPhone":1, "Alarm clock":4,"Notebooks":4}
want_ratings = {"iPhone":4, "A+ in CSC":5, "Calc textbook":4, "Notebooks":5}
print(select_gifts(good_ratings,want_ratings))

























