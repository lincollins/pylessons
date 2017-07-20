# Making decisions Dawn
# We are making little steps
# And I tell you what, we are getting closer to what 
# We have always wanted
# Hurray!!!

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Ooooops sorry pal."
	elif bear == "2":
		print "The bear eats your leg off. Ouch! Not good to hear."
	else: # This info would apear if the user types preferred words than choose #
		print "Well, doing %s is probably better. Bear stays cool." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthuhlu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "You body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else: # This would print if the user does not choose anything at all or inputs something different
	print "You stumble around and fall on a knife and die. Good job!"
