# We are building from the knowledge gained from test5.py
# The use of the format characters and strings which are for the time been d, s and r.
# Previously we used pounds and inches
# In here, we would write variables that converts inches to centimeters
# Pounds to kilos 

inches = '1 cm'
pounds = '10 kilos'
cm = '1 m'
size = 25000
land = 'acres of land'
kilometers = '1000 m'
code = 'Dawn'
black_node = 'Darkest Black Hat'
white_frog = 'Cobra7'

print "%s has %d %s and still counting" % (code, size, land)
print "So %s is very cool." % code # If the format character %s is used, it can work with all sentences
print "Mathematically, 10 inches make", inches # If there is no % sign, use (,) comma instead
print "So also 100 pounds make", pounds # You cant use both % and , sign all together. You need only one of them
print "And then 100 cm makes", cm # Either you use the (,) comma symbol then the variable or the % and the variable
print "Lastly if we could remember 100 kilometers makes", kilometers
print "%r impulse would not be a bad idea" % black_node # 'Darkest Black Hat' is in single quotes when printed? 
print "Just maybe %r would be our next code name :)-" % white_frog # Notice this one too has quotes around it?

# Whenever the format character %r is used, it brings a single quote around the partnered variable
# As in Darkest Black Hat and Cobra7
# Remember that anytime you use the %d format character, it should have a number as a partner
# Anytime you use the %d format character, you know obviously that you are going to use a number right?
# When using the numbers with %d, do not put them in quotes
# Whether single or double

