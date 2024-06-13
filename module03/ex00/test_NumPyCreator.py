# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_NumPyCreator.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 10:05:33 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/13 16:05:27 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from NumPyCreator import NumpyCreator

npc = NumpyCreator()
print (repr(npc.from_list([[1,2,3],[6,3,4]])), '\n')

print (repr(npc.from_list([[1,2,3],[6,4]])), '\n')

print (repr(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]])), '\n')

print (repr(npc.from_list(((1,2),(3,4)))), '\n')
print (repr(npc.from_tuple(("a", "b", "c"))), '\n')
print (repr(npc.from_tuple(["a", "b", "c"])), '\n')
print (repr(npc.from_iterable(range(5))), '\n')
shape = (3,5)
print (repr(npc.from_shape(shape)), '\n')
#print (npc.from_shape(shape, 2), '\n')
#print ( , '\n')
#print ( , '\n')
print (repr(npc.random(shape)), '\n')
print (repr(npc.identity(4)), '\n')