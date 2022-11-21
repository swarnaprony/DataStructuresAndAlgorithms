def split_character(value):
    value_list = list(value)
    return value_list

def check_brackets(value):
    open_perentheses = "("
    close_parentheses = ")"
    open_curly_bracket = "{"
    close_curly_bracket = "}"
    open_square_bracket = "["
    close_square_bracket = "]"
    perentheses_length = 0
    curly_length = 0
    square_length = 0

    for i in split_character(value):
        if perentheses_length == 0:
            if i == close_parentheses:
                return print("False")
            if i == open_perentheses:
                perentheses_length += 1

        if curly_length == 0:
            if i == close_curly_bracket:
                return print("False")
            if i == open_curly_bracket:
                curly_length += 1
        
        if square_length == 0:
            if i == close_square_bracket:
                return print("False")
            if i == open_square_bracket:
                square_length += 1

        if perentheses_length < 0 or curly_length < 0 or square_length < 0:
            return print("False")
        else:
            if i == open_perentheses:
                perentheses_length += 1
            if i == close_parentheses:
                perentheses_length -= 1
                
