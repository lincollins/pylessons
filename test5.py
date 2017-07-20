# We are going to do more variables in here. Its an update from test3.py
# In here, we are going to use format strings. Anytime we added double quotes ""
# To some variables, we were actually creating format strings :)
# A string is how you make something that your programm might give to a human. 
# You print them, save them to files, send them to web servers, all sorts of 
# Things. Strings are really handy, so in this exercise we will learn how to make # Strings that have varaiables embedded in them. You embed variables inside a 
# String by using a specialized format sequences and then putting variables at 
# The end with a special syntax that tells Python, "Hey, this is a format string,
# Put these variables in there."

# Always remember, to use the percent sign % it should first of all
# Be used in the main sentence [print "Kofi is a %s", % male]
# If not, bring a comma after the 'print' word or sentence
# Then the variable [print "Kofi is a ", male]

my_name = 'Zed A. Shaw' # As you know this is a variable.
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # ibs
my_eyes = 'Blue' # This variable involve 2 words so an underscore is  used as the others too :)
my_teeth = 'White'
my_hair = 'Brown'
nano = 'Green'
love = 'loves it though'
code = 'Dawn'
my_house = '4 Bedroom Apartment' # Notice we didn't use double quotes
my_car = "Cheverolet" # We are using it here 
first_doll = "Hundai Sonata" # We used it here too. On a lighter note guys, Dawn has always wish for Sonata :)

print "He is %s Dawner" % code

print "Lets talk about %s." % my_name # Notice that the percentage sign (%) is used 

print "He's %d inches tall." % my_height # It is used with an alphabet of any choice like the (d)

print "He's %d pounds heavy." % my_weight # This is known as a format character, remember format strings?

print "Actually that's not too heavy." # This is when a percentage sign follows a variable(s)

print "He's got %s eyes and %s hair." % (my_eyes, my_hair) # For instance % (my_eyes, my_hair)

print "His teeth are usally %s depending on the coffee." % my_teeth # The only difference with the previous

# Variables in test4.py is that the format character (%) is used in the main sentence but later on denoted 
# At the end of the sentence in an enclosed quote :)
# Notice that in the definition, there is nothing like % but used instead in the sentence? 
# That is how format strings works :)

# This line is tricky, try to get it right exactly
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
print "Dawn has a %r nose. He lives in a %r and has always dreamt of a %r. Well his first car became %r instead, %r in colour. But he %r :)" % (nano, my_house, first_doll, my_car, my_teeth, love) 

# Long statement I guess Dawn :) 
# Notice we used the letter 's' solely in the sentences. We could ve used other alphabets too.
# Fact is not all letters can make a format character. Well there are loads of them to research about Dawn :)
# In here, we ve only been introduced to 'd', 'r' and 's'
# Well, we've found out that using double quotes or single ones doesnt make a difference in variable partnering :)
# As in 'my_car' = "Cheverolet"
# Always stick to a particular character you start with through out
