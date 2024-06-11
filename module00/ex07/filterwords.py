# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 13:42:49 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/11 14:59:32 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def error_msg():
    print ('ERROR')
    exit()

if  len(sys.argv) != 3:
   error_msg()
if  not isinstance(sys.argv[1], str):
    error_msg()
try:
    n = int(sys.argv[2])
except ValueError:
    error_msg()
for punctuation in string.punctuation:
    sys.argv[1] = sys.argv[1].replace(punctuation, '')
new = [word for word in sys.argv[1].split() if len(word) > n]
print (new)
