# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 17:46:09 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/11 13:39:55 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



#.pop


cookbook = {
	'sandwich' : {
		'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
		'meal' : 'lunch',
		'prep_time' : 10,
	},
	'cake' : {
		'ingredients' : ['flour', 'sugar', 'eggs'],
		'meal' : 'dessert',
		'prep_time' : 60,
	},
	'salad' : {
		'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
		'meal' : 'lunch',
		'prep_time' : 15,
	},
}

def	print_all_recipes():
	for key in cookbook:
		print (key)

def	print_details(name):
	recipe = f"""\
Recipe for {name}
	Ingredients list: {cookbook[name]['ingredients']}
	To be eaten for {cookbook[name]['meal']}.
	Takes {cookbook[name]['prep_time']} of cooking.
"""
	print (recipe)
	
def delete_recipe(name):
	cookbook.pop(name) 

def add_recipe():
	recipe = input('Enter a name:\n')
	ingredients = []
	print ('Enter ingredients:')
	while 1:
		val = input()
		if val == '':
			break
		ingredients.append(val)
	meal = input('Enter a meal type:\n')
	time = int(input('Enter a peparation time:\n'))
	cookbook[recipe] = {
			'ingredients' : ingredients,
			'meal' : meal,
			'prep_time' : time,
			}

def	display_menu():
	menu = """\
List of available option:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit
"""
	print (menu)

def	display_recipe(name):
	recipe = f"""\
Recipe for {name}
	Ingredients list:{cookbook[name]}
"""
			

if __name__== "__main__":
	print ("Welcome to the Python Cookbook !")
	display_menu()
	while (1):
		try:
			choice = int(input("Please select an option:\n>> "))
		except ValueError:
			print ('Sorry, this option does not exist.')
			display_menu()
			continue
		print()
		if choice == 1:
			add_recipe()
		elif choice == 2:
			choice2 = input("Please enter a recipe name to delete:\n>> ")
			try:
				delete_recipe(choice2)
			except KeyError:
				print ('Sorry, this meal doesn\'t exist\n')
				continue
		elif choice == 3:
			try:
				choice2 = input("Please enter a recipe name to get its details:\n>> ")
				print_details(choice2)
			except KeyError:
				print ('Sorry, this meal doesn\'t exist\n')
				continue
		elif choice == 4:
			print_all_recipes()
			print()
		elif choice == 5:
			print ("Cookbook closed. Goodbye !")
			break
			

