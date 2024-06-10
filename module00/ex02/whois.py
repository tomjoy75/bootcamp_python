# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:34:18 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/10 11:59:40 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 2:
    print('Usage: whois.py arg1')
    sys.exit()
elif len(sys.argv) > 2:
    print('Usage: Only 1 argument')
    sys.exit()
try:
    i = int(sys.argv[1])
except ValueError:
    print('AssertionError: argument is not an integer')
    sys.exit()
if (i == 0):
    print ("I'm Zero")
elif (i % 2 == 0):
    print ("I'm Even")
else:
    print ("I'm Odd")
