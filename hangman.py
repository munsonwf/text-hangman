import time

#get user's name
name = raw_input("What's your name there, partner?: ")

print "\n"
print "Howdy, %s.  It's time to play hangman!" % (name)

# wait a sec
time.sleep(0.75)

# set secret word, init guesses, set turns
word = "ONION"
guesses = ""
turns = 10

# first while loop

# are turns more than 0?
while turns > 0:
	
	# counter starting at 0 - failed is unguessed chars
	failed = 0

	# for char in word:
	for char in word:
		# display character guessed, if not guessed display _
		if char in guesses:
			print char,
		else:
			print "_",
			failed += 1

	# End game from correct guesses
	if failed == 0:
		print "\nJob well done, %s.  That said, he's still a murderer and we have to hang him." % (name)
		break

	# Makes a line break
	print 

	if turns < 10:
		print "Already guessed: %s." % (guesses)


	guess = raw_input("Guess a charachter:").upper()

	# guess = guess.upper()

	guesses += guess

	# DEVELOPER TOOLS

	# print failed # number of unguessed characters
	# print turns # number of turns remaining
	# print guess # print latest guess
	# print guesses # what is already guessed

	print

	# takes care inconrrect terms - dont not count down for correct guesses.
	if guess not in word:
		turns -= 1
		print "Afraid not, %s." % (name)
		print "You have %s more chances." % (turns)
		
		# End game from bad guesses
		if turns == 0:
			print "It's over, %s.  This innocent man will be hung and it's all your fault!" % (name)
	# EXTRA FEATURE: Turn this on if you want correct guesses to decrease remaining chances. 
	# else: 
	# 	turns -= 1
	# 	print "Remaining turns >>%s<<." % (turns)
