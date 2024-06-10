# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:17:00 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/10 11:27:04 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = len(sys.argv)
if i < 2:
    print('Usage: exec.py arg1 [arg2 ..]')
    sys.exit()
while i > 2:
    rev_word = sys.argv[i - 1][::-1]
    rev_word = rev_word.swapcase()
    print (rev_word, end = ' ')
    i -= 1
rev_word = sys.argv[i - 1][::-1]
rev_word = rev_word.swapcase()
print (rev_word)
