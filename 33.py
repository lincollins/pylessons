# Hmm, we're moving forward
# From the other excersise
# We did some 'for-loop' thing
# In here, may just be similar
# Game on Dawn

# Introducing While Loops :)
# A while-loop will keep executing the code
# Block under it as long as a boolean expression is True.

# The while-loop can make sentences run several times unless an 'if' statement is False
# To avoid that, you need to follow this 3 steps
# Make sure you use 'while-loops' sparingly. Usually for-loops is better
# Review your while statement and make sure the thing you're testing will become False as some point
# When in doubt, print out the test variable at the bottm of the whil-loop to what it does

i = 0
numbers = []



while i < 6: # the 'while' used here is a while-loop
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Number now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers:"

for num in numbers:
	print num