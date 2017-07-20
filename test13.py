# Parameters, Unpacking, Variables
# We will cover one more input type in here Dawn
# You can  use to pass variables to a script (script being another name for # Your .py files)
# The test3.py part of the command is called an "argument"
# What we'll do now is write a script that also accepts accepts arguments

from sys import argv

script, Dawn, Lin, Collins = argv

print "The script is called:", script
print "Your first variable is:", Dawn
print "Your second variable is:", Lin
print "Your third variable is:", Collins

print "\nWho are you?"
name = raw_input()

print "\nWhats your mission?"
purpose = raw_input()

print "\nWho is your prime target?"
entity = raw_input()

print "\nSo you are %s and your mission is to %s. And well prime target is %s" % (name, purpose, entity)

print "\nReally?"
answer = raw_input()


