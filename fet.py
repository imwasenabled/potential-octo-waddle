# FET - Forced-Errors Testing - fixing 4 common Python errors

# SyntaxError: EOL while scanning string literal
print("hello world)

# one is a number and one is a string
var_number = 5
var_string = "0"

# NameError: name 'var_num' is not defined
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(var_num + var_string)

# SyntaxError: invalid syntax
# missing colon (:) - the two dots
def foo(bar)
    print("bar", bar)

# IndentationError: unindent does not match any outer indentation level (line 19)
def print_three_lines(x, y, z):
    print(x)
   print(y)
    print(z)

# IndentationError: unindent does not match any outer indentation level (line 30)
def print_loop(word_list):

    for w in word_list:
        print(w)
         print("*")
