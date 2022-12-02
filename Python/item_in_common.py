
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def item_in_common_dict(list1, list2):
    dict1 = {}

    for i in list1:
        dict1[i] = True
    for j in list2:
        if j in dict1:
            return True


    print(dict1)

print(item_in_common_dict([1, 2, 3], [2, 4, 5]))