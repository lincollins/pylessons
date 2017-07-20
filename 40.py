# Well, in here we learn how to use Dictionary's
# Yes, lovely dictionary's in python
# Now lets do some exercises shall we
# Dawn go find the Python documentation and read about them 
# Also do well to play around them
# Try doing a for-loop over them, and then try the items() function in a for-loop.


# Well, well well I guess we've a lot to learn Dawn
# And surely we shall

cities = {'CA': 'San Fransico', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."

# ok pay attention!
cities['_find'] = find_city

while True: # we would need this in our game
	print "State? (Enter to quit)"
	state = raw_input("> ")

	if not state: break

	# this line is the most important ever! study!
	city_found = cities['_find'](cities, state)
	print city_found