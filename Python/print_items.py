#Big-O O(n)

def print_items_o(n):
    for i in range(n):
        print(i)
print_items_o(10)


#Big-O 2O(n)
def print_items_2o(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items_2o(10)


#Big-O(n^2)

def print_items_n2(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items_n2(10)