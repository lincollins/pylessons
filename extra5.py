# We are doing more of strings and variables
# In here, we are going the complex way
# We have discovered another format character too
# In use of 'x' and 'y'
# We now have 5 format characters namely, 'd', 's', 'r', 'x' and 'y'

x = "There are %d types of people." % 10 # Remember %d, it goes with a number (10)
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # This is a new format I guess. Dawn is not moved :)

print x # 'x' has been defined earlier on you know. Fourth line.
print y # This has also been defined already. Dont ask us which line :)-

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # Notice there are no quotes attached, its because they are strings.

w = "This is the left side of..."
e = "a string with a right side."

print w + e # When printing strings after they have been earlier defined, do not add quotes to it.
