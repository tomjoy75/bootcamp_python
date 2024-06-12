# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_calculator.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 10:32:33 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/12 10:34:50 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from calculator import square

def test_square():
	assert square(2) == 4
	assert square(3) == 9
	assert square(-2) == 4
	assert square(-3) == 9
	assert square(0) == 0
	