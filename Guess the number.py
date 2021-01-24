PROGRAM THAT COMPUTER GENERATES RANDOM NUMBER BETWWEN 1 TO 20.THAT USER NEEDS TO TELL THEM GUESS WHAT IS THE NUMBER IS.
------------------
import random
hid=random.randrange(1,201)
guess=int(input("PLEASE ENTER YOUR NUMBERs:\n"))
if guess==hid:
	print("CORRECT GUESS\n")
elif guess<hid:
	print("GUESSED NUMBER IS HIGH\n")
else:
	print("YOUR GUESS IS LOW\n")
print("THE NUMBER IS :-",hid)