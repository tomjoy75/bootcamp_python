# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joyeux <joyeux@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 18:09:09 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/11 23:13:02by joyeux           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		self.name = self._validate_name(name)
		self.cooking_lvl = self._validate_cooking_lvl(cooking_lvl)
		self.cooking_time = self._validate_cooking_time(cooking_time)
		self.ingredients = self._validate_ingredients(ingredients)
		self.description = description
		self.recipe_type = self._validate_recipe_type(recipe_type)

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = f"Recipe for the {self.name}:\n"
		txt += f"   ingredients\t\t: {', '.join(self.ingredients)}\n"
		txt += f"   cooking time\t\t: {self.cooking_time}\n"
		txt += f"   cooking level\t: {self.cooking_lvl}\n"
		txt += f"   recipe type\t\t: {self.recipe_type}\n"
		txt += f"   description\t\t: {self.description}\n"
		return txt	
		
	def _validate_name(self, name):
		if not name:
			raise ValueError("name shouldn´t be empty")
		if not isinstance(name, str):
			raise ValueError("name should be String")
		return (name)

	def _validate_cooking_lvl(self, lvl):
		if lvl is None:
			raise ValueError("level shouldn´t be empty")
		if not isinstance(lvl, int):
			raise ValueError("cooking_lvl should be an int")
		elif lvl < 1 or lvl > 5:
			raise ValueError("cooking_lvl between 1 and 5")
		return (lvl)

	def _validate_cooking_time(self, time):
		if time is None:
			raise ValueError("cooking time shouldn´t be empty")
		if not isinstance(time, int):
			raise ValueError("cooking_time should be an int")
		elif time < 0:
			raise ValueError("cooking_lvl between 1 and 5")
		return (time)

	def _validate_ingredients(self, ingredients):
		if not ingredients:
			raise ValueError("ingredients shouldn't be empty")
		if not isinstance(ingredients, list):
			raise ValueError("ingredients should be a list")
		if not all(isinstance(item, str) for item in ingredients):
			raise ValueError("each ingredient in list should be a string")
		return (ingredients)

	def _validate_recipe_type(self, type):
		if not type:
			raise ValueError("type shouldn´t be empty")
		if not isinstance(type, str):
			raise ValueError("recipe_type should be String")
		if type not in ['starter', 'lunch', 'dessert']:
			raise ValueError("recipe_type should be starter/lunch/dessert")
		return (type)
			
	def display_info(self):
		print(f"name : {self.name}\nlevel : {self.cooking_lvl}")
		
if __name__ == "__main__":
	try:
		myRecipe = Recipe("pizza", 3, 10, ['tomates', 'pate', 'fromage'], '', 'lunch')
	except ValueError as e:
		print (f"Error : {e}")
		exit()
	#myRecipe.display_info()
	#to_print = str(myRecipe)
	print(myRecipe)
