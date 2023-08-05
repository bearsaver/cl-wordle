# green = 1, yellow = 0, gray = -1

from colorama import Fore, Back, Style

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
	print(char_cts)
	ret = 0
	for i in range(0, len(guess)):
		if guess[i] in word:
			if guess[i] == word[i]:
				if char_cts[word[i]] != 0:
					green(guess[i])
					char_cts[word[i]] -= 1
					ret += 1
				else:
					white(guess[i])
			else:
				if char_cts[word[i]] != 0:
					yellow(guess[i])
					char_cts[word[i]] -= 1
				else:
					white(guess[i])
		else:
			white(guess[i])
	reset()
	
	return ret

def get_word_info(word):
	chars = []
	ret = {}
	for i in range(0, len(word)):
		if not (word[i] in chars):
			chars.append(word[i])
			ret[word[i]] = 1
		else:
			ret[word[i]] += 1
	return ret

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



	if check_guess(guess, answer) == 5:
		print('You got the word!')
		break
