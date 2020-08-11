# For Roma

def ForRoma(my_list):
    counter = {}

    for elem in my_list:
        counter[elem] = counter.get(elem, 0) + 1

    doubles = {element: count for element, count in counter.items() if count > 1}
    return doubles


print(ForRoma([6, 2, 3, 4, 3, 5, 2, 2]))
# we have {2: 3, 3: 2}
