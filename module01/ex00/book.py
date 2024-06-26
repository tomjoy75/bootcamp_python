# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 23:00:39 by joyeux            #+#    #+#              #
#    Updated: 2024/06/12 17:52:46 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe
class Book:
	def __init__(self, name):
		self.name = self._validate_name(name)
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
		self.recipes_list = {'starter' : {},'lunch' : {}, 'dessert' :{}}

	def __str__(self):
		"""Return the string to print with the book info"""
#		creation = self.creation_date.strftime("%Y-%m-%d %H:%M:%S")
		txt = f"book for the {self.name}:\n"
		txt += f"   recipes_list:\n"
		for meal, recipes in self.recipes_list.items():
			txt += f"	{meal} : {recipes}\n"
		txt += f"   creation_date\t: {self.creation_date}\n"
		txt += f"   last_update\t\t: {self.last_update}\n"
		return txt	

	def _validate_name(self, name):
		if not name:
			raise ValueError("name shouldn´t be empty")
		if not isinstance(name, str):
			raise ValueError("name should be String")
		return (name)
	
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if recipe.recipe_type == 'starter':
			self.recipes_list['starter'][recipe.name] = recipe
		elif recipe.recipe_type == 'lunch':
			self.recipes_list['lunch'][recipe.name] = recipe
		elif recipe.recipe_type == 'dessert':
			self.recipes_list['dessert'][recipe.name] = recipe
		else:
			print("This recipe is not valid")	
		
if __name__ == "__main__":
	myRecipe = Recipe("pizza", 3, 10, ['tomates', 'pate', 'fromage'], '', 'lunch')
	try:
		my_book = Book(
			"Italian food", 
			datetime(1990, 1, 1), 
			datetime(2018, 1, 1), 
			{'starter':'pasta', 'lunch':'pizza'}
		)
	except ValueError as e:
		print (f"Error : {e}")
		exit()
	#myRecipe.display_info()
	#to_print = str(myRecipe)
#	print(my_book)
	my_book.get_recipe_by_name('pizza')


# recipes_list = {
# 		"starter": {
# 			"recipe.name": Recipe()
# 		},
# 		"dessert": [],
# 		"lunch": []

	


#book.add(Recipe("pasta",....))