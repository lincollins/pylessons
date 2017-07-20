# More practice Dawn
# We are building some stamina
# I guess you have enough Python 'under your fingers'
# To move onto learning about how programming really works

print "Lets practice everything."
print 'You\'d need to know \'bout escapes with \\ that do newlines and \tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------------"
print poem
print "------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000 # Defining the start_point
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10 # This format string has a partner already '10000'

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# There is some maths in here
# Obviously the symbols too would count :)
