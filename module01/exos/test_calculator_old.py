# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_calculator.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 10:13:07 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/12 10:23:06 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from calculator import square

def	main():
	test_square()

def test_square():
	# if square(2) != 4:
	# 	print("2 squared was not 4")
	# if square(3) != 9:
	# 	print("3 squared was not 9")
	try:
		assert square(2) == 4
		assert square(3) == 9
	except AssertionError:
			
if __name__ == "__main__":
	main()