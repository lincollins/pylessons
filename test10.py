# Doing more with backslash \ and 'n'
# They are called escape keys too
# Some other time we would search online to find out what other 
# Escape sequences we have

print "I am 6'2\" tall." # Escape double-quote inside string
print 'I am 6\'2" tall.' # Escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

single_quotes = '''
We we're using thripple single quotes
"How would it fair down here"
Down here
'''
black_node = "Dawn"
code = "White"
number = 200

print "%r Dawn" % 'Hi' 

print "Dawn says his next code name would be %s" % 'white_frog' 
print single_quotes
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "He is %s, loves %s and would live for a %d yrs" % (black_node, code, number)
