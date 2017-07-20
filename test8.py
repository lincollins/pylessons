# More printing
# Alaways look intently with an Eagle eye.


formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", # It appears as it is becasue of (') in the sentence
	"So I said goodnight."
	)	
