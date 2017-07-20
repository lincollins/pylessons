# We are dealing with functions and files
# A build on functions, variables and a bit of Maths :)
# Always remember with functions def, always add a colon
# We should research online for the more usage of the 'seek' module

from sys import argv # We are importing an argument variable

script, input_file = argv # We would need one argument thus a file

def print_all(f): # We decided to use print_all def and 'f' as a partnering variable
    print f.read() # 'f' here is used for the file. Where 'read' prints the contents on the screen

def rewind(f): # Same here, we rewind the file
    f.seek(0) # Instead the module 'seek' is used to do that

def print_a_line(line_count, f): # Another definition though for 'print_a_line' with 2 variables
    print line_count, f.readline() # Attempts to read line by line using var 'line_count' of 'f'

current_file = open(input_file) # File tends to be opened

print "First lets print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:\n"

current_line = ">>>" # This command prints the first line in the file
print_a_line(current_line, current_file) # 'current_line' equals to the first line in the file

current_line = ">>>" # This moves to the second line in the file
print_a_line(current_line, current_file) # 'current_line' equals to print second line in the file

current_line = ">>>" # This moves to the third line
print_a_line(current_line, current_file) # 'current_line' equals to print third line in the file
