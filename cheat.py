# Ok, so this is the 'Cheaters' game
# Lets see who can get caught
# Oh yeah
# From Dawn's world
# We ain't stopping :)

# Always remember, 'if' has {if, elif, else}
# Also 'elif' has {if, else}
# And 'else' has only 'print'

print "\nHELLO AND WELCOME TO DAWNS WORLD"
print "\nPlease what do I call you?"

user = raw_input(">>> ")

print "\nWelcome %s to Dawn's World" % user

print "Elm...is that a Male's name or Female? No offense please."

gender = raw_input(">>> ")

male = "Male"

female = "Female"

if gender == "Male":
	print "Welcome my Brother."

elif gender == "Female":
	print "Awww, my Sister."

else:
	print "Oooops, I can't confirm your gender please."

print "\nHelp me find some cheaters please. I hope you are not one :)"

print "\nNow lets have fun shall we?"

print "\n'Yes' to continue the game. 'No' to quit"

ans = raw_input(">>> ")
################################################################## First A
if ans == "Yes":
	print "\nWell, are you Single or Married?"
	
	mar = raw_input(">>> ")

################################################################ Sec A
	if mar == "Single": # Single or Married? Single
		print "\nOk, thats not bad %s" % user

############################################################### Gen A		
		if gender == "Male":
			print "\nIf ever you have a girlfriend, would you kiss another lady?"
			male = raw_input(">>> ")
	
############################################################## Gen A YES
			if male == "Yes":
				print "\nWhat about phone sex, would you do that please?"
				male = raw_input(">>> ")
				
				if male == "Yes":
					print "\nOk, not the least actually %s. Would you wish you date 2 ladies at the same time?" % user
					male = raw_input(">>> ")
                                
				if male == "Yes":
					print """
\n%s? Are you saying you a cheat even before having a girlfriend?
Seriously? Yes you are! :(
So you are the cheat I ve been looking for :)
Don't worry, I won' tell your future wife :)
""" % user
############################################################# GEN A NO
			elif male == "No":
				print "\nWhat about phone sex, would you do that please?"
				male = raw_input(">>> ")
				
				if male == "No":
					print "\nOk, not the least actually %s. Would you wish you date 2 ladies at the same time?" % user
					male = raw_input(">>> ")

				if male == "No":
					print """
\nOh my goodnews! Do you see what I'm seeing %s
Seriously? If we have a 1000's of you, the world would've been a better place
Guess what, you are not a cheat %s :)
As a gift, I will take the responsibility of finding one for you
Hope you dont mind %s :)
""" % (user, user, user)

########################################################### GEN A NO INPUT
			else:
				print "\nOops, It seems you dont want me to know %s. Cheat Exiting. :(" % user					

############################################################### Gen B
		elif gender == "Female":
			print "\nIf ever you have a boyfriend, would you kiss another guy?"
			female = raw_input(">>> ")

############################################################## Gen B YES
			if female == "Yes":
				print "\nWhat about phone sex, would you do that please?"
				female = raw_input(">>> ")
				
				if female == "Yes":
					print """
\nOk, not the least actually %s. Would you wish you date 2 guys at the same time?"
""" % user
					female = raw_input(">>> ")
					
				if female == "Yes":
					print """
\n%s? Are you saying you a cheat even before having a boyfriend?
Seriously? Yes you are! :(
So you are the cheat I ve been looking for :)
Don't worry, I won' tell your future husband :)
""" % user	
############################################################### Gen B NO
			elif female == "No":
				
				if female == "No":
					print "\nWhat about phone sex, would you do that please?"
					female = raw_input(">>> ")
				
				if female == "No":
					print """
\nOk, not the least actually %s. Would you wish you date 2 guys at the same time?"
""" % user	        
					female = raw_input(">>> ")

				if female == "No":
					print """
\nOh my goodnews! Do you see what I'm seeing %s
Seriously? If we have a 1000's of you, the world would ve been a better place
Guess what, you are not a cheat %s :)
As a gift, I will take the responsibility of finding one for you
Hope you dont mind %s :)
""" % (user, user, user)
############################################################## Gen B NO INPUT
			else:
				print "Oops, It seems you don't want me to know % Cheat Exiting. :(" % user


############################################################### Gen C
		else:
			print "Oops, It seems you don't want me to know % Cheat Exiting. :(" % user

############################################################### Sec B	
	elif mar == "Married":
		print "\nSounds like a good news %s :)" % user

############################################################## Sec B GEN A YES
		if gender == "Male":
			print "\nWould you wish you have another lady who you can go out with?"
			male = raw_input(">>> ")

			if male == "Yes":
				print "\nWhat about phone sex with another lady, would you do that please?"
				male = raw_input(">>> ")
				
			if male == "Yes":
				print "\nOk, not the least actually %s. Would you wish you have some other lady as your wife?" % user
			        male = raw_input(">>> ")
					
			if male == "Yes":
				print """
\n%s? Are you saying you a cheat even while married?
Seriously? Yes you are! :(
So you are the cheat I ve been looking for :)
Don't worry, I won' tell your wife :)
""" % user	
############################################################# SEC B GEN A NO

			if male == "No":
				print "\nWhat about phone sex with another lady, would you do that please?"
				male = raw_input(">>> ")
				
			if male == "No":
				print "\nOk, not the least actually %s. Would you wish you have some other lady as your wife?" % user
			        male = raw_input(">>> ")
				
			if male == "No":
				print """
\nOh my goodnews! Do you see what I'm seeing %s
Seriously? If we have a 1000's of you, the world would be a better place
Guess what, you are not a cheat %s :)
As a gift, I will add you to the faithful list of Married men :)
Hope you dont mind %s :)
""" % user
########################################################### SEC B GEN A NO INPUT
			
			else:
				print "Elm...%s I can't confirm your input please" % user

########################################################## SEC B GEN B YES

		elif female == "Female":
			print "\nWould you wish you have another guy who you can go out with?"
			female = raw_input(">>> ")

			if female == "Yes":
				print "\nWhat about phone sex with another guy, would you do that please?"
				female = raw_input(">>> ")
				
				if female == "Yes":
					print "Ok, not the least actually %s. Would you wish you have some other guy as your husband?"
					female = raw_input(">>> ")

				if female == "Yes":
					print """
\n%s? Are you saying you a cheat even while married?
Seriously? Yes you are! :(
So you are the cheat I ve been looking for :)
Don't worry, I won' tell your Husband :)
""" % user					
########################################################### SEC B GEN B NO
			
			elif female == "No":
				print "\nWhat about phone sex with another guy, would you do that please?"
			        female = raw_input(">>> ")
				
				if female == "No":
					print "\nOk, not the least actually %s. Would you wish you have some other guy as your husband?"
				        female = raw_input(">>> ")

				if female == "No":
					print """
\nOh my goodnews! Do you see what I'm seeing %s
Seriously? If we have a 1000's of you, the world would be a better place
Guess what, you are not a cheat %s :)
As a gift, I will add you to the faithful list of Married Women :)
Hope you dont mind %s :)
""" % user					
######################################################### SEC B GEN B NO INPUT
			else: 
				print "\nOops, please I can't confirm your input %s Cheat Exiting. :(" % user


############################################################### Sec C
	else: 
		print "\nOops, please I can't confirm your input %s Cheat Exiting. :(" % user



############################################################# First B
elif ans == "No":
	print "\nOops, %s don't want to play the game" % user
	print "Sad to see you leave Dawn's world :("

############################################################ First C

else:
	print "Ooops, no input received. Cheat Exiting..."

########################################################### Ends here Dawns Incoperation c 2017 #######################################################

