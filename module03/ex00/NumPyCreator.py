# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 09:42:31 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/13 11:37:48 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import warnings

class NumpyCreator:
	def from_list(self, lst):
		if not isinstance(lst, list):
			return ("None")
		warnings.simplefilter("error", np.VisibleDeprecationWarning)	
		try:
			a = np.array(lst)
		except np.VisibleDeprecationWarning:
			return ("None")
		return (a)
	
	def from_tuple(self, tpl):
		if not isinstance(tpl, tuple):
			return ("None")
		return (np.array(tpl))
		
	def from_iterable(self, itr):
		try:
			iter(itr)
		except TypeError:
			return ("None")
		return (np.array(itr))
	def from_shape(self, shape, value=0):
		return (np.full(shape, value))
	def random(self, shape):
		rng = np.random.default_rng()
		return (np.random.rand(*shape))
	def identity(self, n):
		return (np.identity(n))
		
			