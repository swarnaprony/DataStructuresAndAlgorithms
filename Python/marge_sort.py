
def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1    
    return combined
    

def merge_sort(list):
    if len(list) == 1:
        return list
    mid_index = int(len(list)/2)
    left_list = merge_sort(list[:mid_index])
    right_list = merge_sort(list[mid_index:])
    return merge(left_list, right_list)


list1 = [1, 3, 5, 7, 9, 11]
list2 = [2, 4, 1,  6, 8, 10, 12, 3, 14, 5, 16, 18]

print(merge_sort(list2))
