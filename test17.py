# More files
# In here, Dawn we would do well to write a Python script to copy one file to another
# Yes, dont worry. It would end well :)
# Vhim yazo! :)
# Dawn we beg you, scripting needs lots of attention and care
# Always pay close attention even to the smallest of details
# Ayoo
# You really want to reduce bugs among others?
# Then do it
# Do well to read on Pythons import statement and start python to try it out

from sys import argv
from os.path import exists

script, from_file, to_file = argv # We nedd 2 files as compared to test16.py
				  # One is for the from_file and another is to_file
				  # We use the to_file because of the 'os.path import'

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file) # If the output file doesnt exist, its False
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input() # As usual raw_input provides us with a space to type something in.

output = open(to_file, 'w') # File is opened in the system backgroud. Ready for 'w' writing
output.write(indata) # File gets writtin to

print "Alright, all done."

output.close() # File is closed
input.close() # After writing is done, it closes
