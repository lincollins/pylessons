# We are going to use Names, Variables, Code, Functions
# Functions more importantly
# FUnctions do 3 things;
# They name piece of code the way variables name strings and numbers
# They take arguments the way your scripts thake argv
# Using #1 and #2 they let you make your own "mini scripts" or "tiny vommands"

# this one is like our scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

# this is Dawn's own. We are just using any word :)
def output(demo, demo2):
    print "This demo is %s, the other is %s" % (demo, demo2)

# another Dawn's work. Lets try blacknode :)
def black_node(*node):
    node1, node2 = node
    print "Dawn's code name is %s, well, is it %s?" % (node1, node2)

# Mice84 at work. Lol its Dawn :) 
# Lets use just one argument ok?
def mice84(mice84):
    print "Ok, so our new codename would maybe be %s" % mice84

# We give it no argument Dawn
def reg_sec():
    print "Regent Security would be our Company's name someday. Yes!"

# Ok, so we have realised that functions help reduce repeated works
# For instance, for us to type...print "This demo %s, the other is %s" % (demo, demo2)
# Several times, all we need to do is to use the function module. :)
# Der nor ur guy guy come :) :) :) swear
# Anyway, we define (def) it at the start of the script :)
# Then we tend to use it later, so as where ever there is 'output', the defined words go

# As in just down here. One print sentence, four words. So the function generates 
# A second one for us. All we need is just to give 
# Some partnering variables to 'output'. Bingo, we a re good to go.
# The word 'output' is been used randomly, any one could do. Like 'dawn' :)

output("better", "good")
output("worse", "worst")

black_node("Cobra7","Whitefrog") # If you repeat the defined function twice, it comes 2
black_node("Black_node","Mice84") # If for a 1000 times, it will come as such

mice84("Mice84")

reg_sec()

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")

print_none()
