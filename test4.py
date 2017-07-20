# We are going to learn Variables in here. Test 3 covered Maths Symbols
# All these things like the 'cars' used in here is a variable.
# Where ever 'cars' is mentioned, '100' shows up instead. Why?
# Its because 'cars = 100'. 
# So to make a variable, equate it to something. 
# Dawn = 50%
# Interestingly, with the above example wherever 'Dawn' is mentioned, '50%' 
# Appears instead
# When using variables and you need 2 or 3 words, use the underscore instead


D = "Blacknode Incoporation" # If you want to use a letter or Word as a Variable, put the variable partner in quotes "". And well, dont use an underscore :)
# If its a number, dont use any quotes ""

cars = 100
space_in_a_car = 4.0 # 4.0 is a floating point number
drivers = 30.0 # 30.0 is a floating number too because of the decimal 30.0 :)
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "Welcome to", D # As in here, where 'D' means "Blacknode Incoporation"
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each other."
