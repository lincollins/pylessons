# Dawn, sources say that the variables we used in our functions at test18.py
# Are not connected to the variables in our script :(
# What do you make of it? 
# Well this is an exercise to get us thinking

# Dawn do you remember test18.py? Its a similar to the one we ve here
# Here, cheese_crackers is defined. Any word could be used instead
# And now the variables (cheese_count, boxes_of_crackers)
def cheese_and_crackers(cheese_count, boxes_of_crackers): # This is a function too
    print "You have %d cheeses!" % cheese_count # This is the variable % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers # This too
    print "Man thats enough for a party!"
    print "Get a blanket.\n" # Remember this? It allows spacing in sentences

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) # And well, we can use numbers too
                            # Same thing as previous. 
                            # The first number goes to 'You have %d cheeses!'
                            # The second number applies to 'You have %d boxes of crackers!"

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # You would realise that the
							  # The Main def is always used
                                                          # cheese_and_crackers
							  # It matters most
                                                          # Dont forget please Dawn

print "We can even do math inside too:" # Lets do some Maths. Hope you dont mind :)
cheese_and_crackers(10 + 20, 5 + 6) # As additions are used here, 
                                    # We can use other symbols as well (-, /, x, +)

print "And we can combine the two, variables and math:" # Variables and Maths
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # Pure sample

# This is Dawn inputs :)
print "Dawn loves coding and hacking. Its in his DNA"
cheese_count = 87
boxes_of_crackers = 250

cheese_and_crackers(cheese_count, boxes_of_crackers) # When using a def, dont use '='

def halo(code, clients, warrior): # Remember to always add the colon: when using def please
         print "Boss Dawn, congratulations! You are the richest man on earth!"
         print "Ok guys, lets %s" % code
         print "Champ Dawn, we heard you got %s" % clients
         print "Ok, no problem. By God's grace we are on course"
         print "Cobra7 aka Dawn, real %s are you" % warrior
         print "Game on boys, we ain't stopping yet!\n"
   
halo("code","clients","warrior") # Over here, we give real values to the variables

def c(c, g, p): # We define a new function 'c' which would take 3 arguments (c, g, p)
    print "Welcome my people to Dawn's world of %s!" % c
    print "Well its all good %s!" % g
    print "This is what he has %s for!" % p
    print "No stopping Eagle99"
    print "Hurray! We are on course!\n"

c("coding","guys","passion")

print "Hi guys" # This is optional, without it, still 3 statemens would be printed
c("Reg_Sec","yeah","always killed himself") # If function 'c' has the needed arguments

# Interestingly, we can use as many functions as we want
# All we needed is to to define it and add the variables as many as we want
# Then 'edit' the content for other structures if we want repeated ones as in 'def c'
# Bingo, we should be done and dusted
# Yes Boss Dawn






