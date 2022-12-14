def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def pivot(list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if list[i] < list[pivot_index]:
            swap_index += 1
            swap(list, swap_index, i)
    swap(list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right: 
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index -1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

my_list = [4, 6, 1, 7, 3, 2, 5]
print(quick_sort(my_list))
