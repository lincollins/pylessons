# Loops and Lists
# In here Dawn, we do some Loops and Lists
# Remeber your game
# Cheatad and well the Cheat itself
# Well I guess we can expand it you know
# Thumbs up any way
# Thumbs up to God too :) He's been amazing so far
# I guess we owe him Big :)

# Ok Dawn, we're going to do some list in here you know
# We are going to store stuffs.
# Do some repeated works and who knows just maybe :)
# We are getting closer you know

# Now lets make a list

hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

# Just a  reminder Dawn, things will get just maybe tricky
# Interestingly, we have it worked out :)
# We now will buld some lists using some loops and print them out

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this fist kind of for-loop goes through a list
for number in the_count: # the 'for' used here is known as a for-loop
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
 
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 20 counts
for i in range(0,7):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
	fruits.append(i) # We added this too but trust me guys, we still dont get it clearer

# Dawn own assessment 
for i in fruits:
	print "Some test you know"

# now we can print them out too
for i in elements:
	print "Element was: %d" % i
	
# Ok, Dawn for the loop. We got loads of things to do
# Trust me yeah, we really need to understand this for loop thing
# Well it seems it prints out some repeated stuffs as dicussed earier on
# We will work with it :)
