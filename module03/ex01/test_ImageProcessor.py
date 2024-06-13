# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_ImageProcessor.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 13:01:31 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/13 16:08:37 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ImageProcessor import ImageProcessor
imp = ImageProcessor()
# arr = imp.load("./42AI.png")
# arr = imp.load("./Google.png")
arr = imp.load("./img/colors.png")

imp.display(arr)