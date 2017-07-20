# Prompting and Passing
# We are doing one more exercise where the usage of argv and raw_input counts
# Learning how to read and write files is important
# Dawn, we will ve raw_input print a simple > prompt. 
# This is similar to a game like Zork or Adventure :)
# Try to find out what Zork and Adventure game is and play :)
# Eeeeeish Dawn, you are laughing :)-

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you some few questions."
print "\nDo you like me %s?" % user_name
likes = raw_input (prompt)

print "\nWhere do you live %s?" % user_name
lives = raw_input(prompt)

print "\nWhat kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
