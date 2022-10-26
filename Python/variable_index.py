
number_1 = 10
number_2= number_1


print('Index of number 1: ', id(number_1))
print('Index of number 2: ', id(number_2))

number_3 = 10
number_4= 10


print('Index of number 3: ', id(number_3))
print('Index of number 4: ', id(number_4))


dict_1 = {
    'value': 2
}

dict_2 = dict_1

dict_3 = dict_2

print('Index of dict 1: ', id(dict_1))
print('Index of dict 2: ', id(dict_2))
print('Index of dict 3: ', id(dict_3))