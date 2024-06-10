# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 16:32:59 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/10 16:52:54 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def sum(a, b):
    return (a + b)

def diff(a,b):
    return (a - b)

def prod(a, b):
    return (a * b)

def div(a , b):
    return (a / b)

def mod(a, b):
    return (a % b)

if len(sys.argv) < 3:
    print('Usage: python operations.py <number1> <number2>')
    sys.exit()
elif len(sys.argv) > 3:
    print('AssertionError: too many arguments')
    sys.exit()
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    print('AssertionError: argument is not an integer')
    sys.exit()
print (f"Sum:\t\t{sum (a,b)}")
print (f"Difference:\t{diff (a,b)}")
print (f"Product:\t{prod (a,b)}")
try:
    print (f"Quotient:\t{div (a,b)}")
    print (f"Remainder:\t{mod (a,b)}")
except ZeroDivisionError:
    print ("Quotient:\tERROR (division by zero)")
    print ("Remainder:\tERROR (modulo by zero)")


