# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 10:07:33 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/12 10:52:27 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def 	main():
	x = int(input("What's x? "))
	print("x squared is", square(x))

def		square(n):
	return n * n

if __name__== "__main__":
	main()
