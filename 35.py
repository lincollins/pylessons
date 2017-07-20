# We are dealing with branches and functions in here
# Oh yeah, I guess we're going to bend our mind a little
# Trying something new as alwasy you know
# Hullay!
# Elm, sorry. Hurray
# So fra we've learnt how to do if-statments, boolens and arrays
# Lets try something else

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door"
	print "How are you going to move the bear?"
	bear_moved = False

	while True: # And here too. We would need it in Cheatad Game Boss Dawn
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then pimp slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can move now"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your croctch off")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."	

def cthulu_room(): # We would need this place in cheatad Game Dawn
	print "Here you see the great evil Cthulu"
	print "He it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat yor head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start(): # We will need here too. For the start of the game
	print "You're in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")

start()