# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 16:20:10 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/11 17:51:12 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def display_intro():
	intro ='''\
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!

'''

num = random.randint(1, 99)
score = 0
while True:
	score += 1
#	print(f"score : {score}, solution : {num}")
	answer = input("What's your guess between 1 and 99?\n>> ")
	if answer == 'exit':
		print ("Goodbye!")
		exit()
	try:
		guess = int(answer)
	except ValueError:
		print("That's not a number.")
		continue
	if guess > num:
		print("Too high!")
		continue
	elif guess < num:
		print("Too low!")
		continue
	else:
		if num == 42:
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		if score == 1:
			print("Congratulations! You got it on your first try!")
		else:
			print("Congratulations, you've got it!")
			print(f"You won in {score} attempts!")
		exit()	
