# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 13:00:21 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/10 16:25:59 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def nbr_upper(txt):
    i = 0
    for char in txt:
        if (str.isupper(char)):
            i += 1
    return (i)

def nbr_lower(txt):
    i = 0
    for char in txt:
        if (str.islower(char)):
            i += 1
    return (i)

def nbr_digit(txt):
    i = 0
    for char in txt:
        if (str.isdigit(char)):
            i += 1
    return (i)


def nbr_punc(txt):
    i = 0
    for char in txt:
        if (str.islower(char)):
            i += 1
    return (i)

def nbr_space(txt):
    i = 0
    for char in txt:
        if (str.isspace(char)):
            i += 1
    return (i)


def text_analyzer(txt=None):
    '''\n\tThis function counts the number of upper characters, lower characters,
\tpunctuation and spaces in a given text.'''
    if (txt == None):
        print('What is the text to analyze?')
        txt = input('>> ')
    if not isinstance(txt, str):
        print ("AssertionError: argument is not a string")
        return
    print(f"The text contains { len(txt)} character(s):")
    print(f"- {nbr_upper(txt)} upper letter(s)")
    print(f"- {nbr_lower(txt)} lower letter(s)")
    print(f"- {len(txt) - nbr_lower(txt) - nbr_upper(txt) - nbr_space(txt) - nbr_digit(txt)} punctuation mark(s)")
    print(f"- {nbr_space(txt)} space(s)")
    
if __name__ == "__main__":
    if len(sys.argv) > 2:
        print('Usage: Only 1 argument')
        sys.exit()
    text_analyzer(sys.argv[1])        

