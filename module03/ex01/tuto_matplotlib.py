# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tuto_matplotlib.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 14:40:28 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/13 16:40:20 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#https://matplotlib.org/stable/tutorials/images.html#sphx-glr-tutorials-images-py
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

image = Image.open("./img/stinkbug.png")
img = np.asarray(image)
print(repr(img))
lum_img = img[:, :, 0]
print(repr(lum_img))
imgplot = plt.imshow(lum_img, cmap="hot", interpolation="bicubic")
#plt.colorbar()
#plt.hist(lum_img.ravel(), bins=range(256), fc='k', ec='k')
plt.show()