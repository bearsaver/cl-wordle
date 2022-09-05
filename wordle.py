import random
from colorama import init
from termcolor import colored

def pick_word(words):
	index = random.randint(0, (len(words) - 1))
	return words[index]

def check_guess(guess, answer):
	response = [None] * 5
	counter = 0
	for character in guess:
		if character in answer:
			response[counter] = "y"
			if character == answer[counter]:
				response[counter] = "g"
		else:
			response[counter] = "w"

		counter += 1
	
	return response

def search_list():
	# TODO: implement this
	return

# intialize colorama
init()

# list of words that can be used
possible_words = ["hello", "joker", "place", "spade"]

# pick words, create list of characters
answer = pick_word(possible_words)

guess_number = 0

guesses = []

while(True):
	
	# increment guesses
	guess_number += 1 

	# validate user input - make sure it's alphabetic and 5 chars
	while(True):
		guess = input(f"guess {guess_number}: ")
		if (len(guess) == 5) and (guess.isalpha() == True):
			guesses.append(guess)
			break
		else:
			print("Invalid guess. Try again.")

	# check guess
	guess = guesses[guess_number - 1]
	response = check_guess(guess, answer)
	
	# print output
	print("         ")
	counter = 0
	for char in response:
		if char == "g":
			print(colored(guess[counter], "green"), end="")
		elif char == "y":
			print(colored(guess[counter], "yellow"), end="")
		else:
			print(guess[counter], end="")

		counter += 1
			
	# print newlines
	print()
	print()

	# check if word is correct
	if response == (["g"] * 5):
		print(f"you got the word in {guess_number} guesses!")
		break

	# make sure guesses aren't used up; if so, end program
	if guess_number == 6:
		print(f"the word was {answer}")
		break