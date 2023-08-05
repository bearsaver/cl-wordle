# green = 1, yellow = 0, gray = -1

from colorama import Fore, Back, Style

def check_guess(guess, answer):
	ret = []
	gre_ct = 0
	for i in range(0, len(guess)):
		if guess[i] in answer:
			if guess[i] == answer[i]:
				ret.append(1)
				gre_ct += 1
			else:
				ret.append(0)
		else:
			ret.append(-1)
	
	return ret

def search_list():
	# TODO: implement this
	return

# pick words, create list of characters
answer = "hello"

guess_number = 0

guesses = []

while(guess_number < 6):
	
	# validate user input - make sure it's alphabetic and 5 chars
	while(True):
		guess = input(f"guess {guess_number}: ")
		if (len(guess) == 5) and (guess.isalpha() == True):
			guesses.append(guess)
			guess_number += 1
			break
		else:
			print("Invalid guess. Try again.")

	# check guess
	guess = guesses[guess_number - 1]
	data = check_guess(guess, answer)

	for i in range(0, len(data)):
		if (data[i] == 1):
			print(Fore.GREEN + guess[i], end="")
		elif (data[i] == 0):
			print(Fore.YELLOW + guess[i], end="")
		else:
			print(Fore.WHITE + guess[i], end="")
		print(Style.RESET_ALL, end="")

	print()

	if data == [1, 1, 1, 1, 1]:
		print("You got the word!")
		break
	
