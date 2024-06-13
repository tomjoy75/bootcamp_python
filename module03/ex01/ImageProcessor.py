# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 11:40:48 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/13 14:35:41 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor:
	def	load(self, path):
		image = Image.open(path)
		print (f"Loading image of dimensions {image.width} * {image.height} in mode {image.mode}")
		if image.mode != 'RGB':
			image = image.convert('RGB')
		# plt.imshow(image)
		# plt.title("Image chargee")
		# plt.show()
		array = np.array(image)

		# Afficher des statistiques sur le tableau NumPy
		print(f"Array shape: {array.shape}")
		print(f"Array dtype: {array.dtype}")
		print(f"Array min value: {array.min()}")
		print(f"Array max value: {array.max()}")
		print(f"Array mean value: {array.mean()}")
		
		return array 
	def display(self, array):
		plt.imshow(array)
		plt.show()