# This is a test file
# We want to get an extension from a different file
# Would see if it would work

from sys import exit


def file_import():
	print "Are you ready"

	while True:

		que = raw_input(">>> ")

		if que == "Yes":
			from init import single_axe
			single_axe()
		elif que == "No":
			from kline import dope
			dope()
		else:
			from soft1 import script 
			return 'file_import'



	