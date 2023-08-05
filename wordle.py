# green = 1, yellow = 0, gray = -1

from colorama import Fore, Back, Style
from random import randrange

words = ['hello', 'world', 'spade', 'joker', 'spree', 'trace', 'scold']

def green(char):
	print(Fore.GREEN + char, end="")

def yellow(char):
	print(Fore.YELLOW + char, end="")

def white(char):
	print(Fore.WHITE + char, end="")

def reset():
	print(Style.RESET_ALL)

def check_guess(guess, word):
	char_cts = get_word_info(word)
	res = [0 for i in range(0, 5)]
	for i in range(0, len(guess)):
		if guess[i] in word:
			if guess[i] == word[i]:
				if char_cts[guess[i]] > 0:
					res[i] = 1
					char_cts[guess[i]] -= 1
	
	for i in range(0, len(guess)):
		if guess[i] in word:
			if guess[i] != word[i]:
				if char_cts[guess[i]] > 0:
					res[i] = 0
					char_cts[guess[i]] -= 1
				else:
					res[i] = -1
	
	for i in range(0, len(guess)):
		if guess[i] not in word:
			res[i] = -1
	
	return res

def print_res(res, guess):
	for i in range(0, len(res)):
		if res[i] == 1:
			green(guess[i])
		elif res[i] == 0:
			yellow(guess[i])
		elif res[i] == -1:
			white(guess[i])
	reset()

def check_for_solve(res, guess):
	if res == [1 for i in range(0, 5)]:
		return 1
	else:
		return 0

def get_word_info(word):
	chars = []
	res = {}
	for i in range(0, len(word)):
		if not (word[i] in chars):
			chars.append(word[i])
			res[word[i]] = 1
		else:
			res[word[i]] += 1
	return res

# pick words, create list of characters
word = words[randrange(0, len(words) - 1)]

guess_number = 0

guesses = []

while(guess_number < 6):

	# validate user input - make sure it's alphabetic and 5 chars
	while(True):
		guess = input(f"guess {guess_number + 1}: ")
		if (len(guess) == 5) and (guess.isalpha() == True):
			guesses.append(guess)
			guess_number += 1
			break
		else:
			print("Invalid guess. Try again.")

	# check guess
	guess = guesses[guess_number - 1]

	res = check_guess(guess, word)
	
	print_res(res, guess)

	if check_for_solve(res, guess):
		print('You got the word!')
		break