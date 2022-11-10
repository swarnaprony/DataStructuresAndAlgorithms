def split_character(value):
    value_list = list(value)
    return value_list

def check_perentheses(value):
    open_perentheses = "("
    close_parentheses = ")"
    open_length = 0
    close_length = 0

    for i in split_character(value):

        if open_length < close_length:
            return print("False")
        else:
            if i == "(":
                open_length += 1
            if i == ")":
                close_length += 1

    if open_length == close_length:
        return print("True")
    else:
        return print("False")



check_perentheses("astu, how are you doing())(")