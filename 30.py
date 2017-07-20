# Ok, Here we are again Dawn
# What we did previously in 29.py was some boolean expressions
# We introduce Else and If boolean functions
# Or you would prefer to call statements :)
# One more thing, Python expects us to indent something after using a colon 
# Yes Python wants us to :)

people = 30
cars = 40
buses = 15

if buses > cars or people < buses: # We are having some fun Dawn :)
	print "Good work done Dawn"
elif buses < cars or people > buses: # Yes we are. And well we saw you clapping hands
	print "Happy home"
else: print "Bad boy init."

if cars > people and buses > cars:
	print "Lets do some test Dawn"
elif cars < people and buses > cars:
	print "Ok Dawn. lets see if it would work out"
else: 
	print "Hmm, lets see what happens" 

if cars > people: # If there are 3 statements going to be used, add 'elif'
	print "We should take the cars." # So it goes from 'if', 'elif' and 'else'
elif cars < people:  
	print "We should not take the cars."
else: # Else does not take any argument. 'elif' always serves as a middle man.
	print "We can't decide."

if buses > cars: 
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else: 
	print "We still can't decide."

if people > buses: # This always take an argument
	print "Alright, let's just take the buses."
else: # This does not take any argument please. Take note
	print "Fine, lets stay home then."
