

# importing sys
import sys

# adding Folder_2/subfolder to the system path
sys.path.insert(6, '/Users/swarnasarker/Documents/DataStructureAlgorithm/Python')

from stacks import Stack;


def split_character(value):
    value_list = list(value)
    return value_list

def check_brackets(string):
    validity = "Valid"
    open_brackets = [ "(", "{", "[" ]
    close_brackets = [")", "}", "]"]
    perentheses = ["(", ")"]
    curly = ["{", "}"]
    square = ["[", "]"]
    height = 0

    bracket_list = split_character(string)

    for i in bracket_list:
        if height == 0:    
            if i in open_brackets:
                brackets_stack = Stack(i)
                height += 1
            if i in close_brackets:
                validity = "Invalid"
                return validity

        if height > 0:
            top_element = brackets_stack.top.value
            if i in open_brackets:
                brackets_stack.stack_push(i)
                height += 1
            if i in close_brackets:
                if top_element in perentheses and i in perentheses:
                    print("peren called")
                    brackets_stack.stack_pop()
                    height -= 1
                if top_element in curly and i in curly:
                    print("curly called")
                    brackets_stack.stack_pop()
                    height -= 1
                if top_element in square and i in square:
                    print(" square called")
                    brackets_stack.stack_pop()
                    height -= 1
            if height == 0:
                validity = "valid"

            if height > 0:
                validity = "invalid"
        
        return validity

print(check_brackets("{{}}"))