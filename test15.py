# Everything we've leant about raw_inputs and argv is so we can start reading files. We would ve to play with this exercise the most to understand what's going on. So do it carefully and remember your    Checks.Working with files is an easy way to erase our work if not careful :(
# This file involves writing two files.
# One is test15.py and the other is test15_sample.txt.
# This second file ins't a script but a plain text file we'll be reading in # Our script.

# We can 'Hard code' the file to get our results but we dont want to
# It is why we are using the argv and raw_input
# In order to ask for the file name

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "I'll also ask you to type it again:"
file_again = raw_input("\n> ")

txt_again = open(file_again)

print txt_again.read()

print "Anything else please?"
yes = raw_input("\n> ")

server = "server down"

print "Oooops, %s" % server

print "Thank you"




