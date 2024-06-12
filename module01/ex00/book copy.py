# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 23:00:39 by joyeux            #+#    #+#              #
#    Updated: 2024/06/12 14:45:50 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe
class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		self.name = self._validate_name(name)
		self.last_update = self._validate_last_update(last_update)
		self.creation_date = self._validate_creation_date(creation_date)
		self.recipes_list = self._validate_recipes_list(recipes_list)

	def __str__(self):
		"""Return the string to print with the book info"""
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

	def _validate_last_update(self, last_update):
		if not last_update:
			raise ValueError("last_update shouldn't be empty")
		if not isinstance(last_update, datetime):
			raise ValueError("last_update should be a datetime")
		return (last_update)

	def _validate_creation_date(self, creation_date):
		if not creation_date:
			raise ValueError("creation_date shouldn't be empty")
		if not isinstance(creation_date, datetime):
			raise ValueError("creation_date should be a datetime")
		return (creation_date)

	def _validate_recipes_list(self, recipes_list):
		if not recipes_list:
			raise ValueError("recipes list shouldn't be empty")
		if not isinstance(recipes_list, dict):
			raise ValueError("recipes list should be a dict")
		meal_type = ['starter' , 'lunch', 'dessert']
		if not all(name in meal_type for name in recipes_list):
			raise ValueError("each recipes in the list should be in the form starter/lunch/dessert")
		return (recipes_list)
		
	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		for recipe in self.recipes_list:
#			print (recipe)
			data = self.recipes_list.get(recipe)
			if data == name:
				print (data)	
		
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		#... Your code here ...
		
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		#... Your code here ...

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


recipes_list = {
		"starter": {
			"recipe.name": Recipe()
		},
		"dessert": [],
		"lunch": []

	
}

book.add(Recipe("pasta",....))