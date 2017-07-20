# Hm. Well we should learn how to create a flow chart and use it
# Its an exercise Dawn and shouldnt be a problem
# If we can, we should work it out
# And well we sould also find out some python codes and read
# Figure out some errors in the vode
# Write possible vhanges to it and send it to the author :)
# Yeah

# This is just a one off
# Trying some class in here

class TheThing(object):

	def __init__(self):
		self.number = 0

	def some_function(self):
		print "I got called."

	def add_me_up(self, more):
		self.number += more
		return self.number

# two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print a.add_me_up(20)
print b.add_me_up(30)
print b.add_me_up(30)

print a.number
print b.number